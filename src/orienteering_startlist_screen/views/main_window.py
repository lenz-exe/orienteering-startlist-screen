import datetime
import logging
import os
from typing import Optional, Any
import webbrowser

from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import QCoreApplication, QSettings, QFileInfo

from orienteering_startlist_screen import config
from orienteering_startlist_screen.ui.main_window_ui import Ui_MainWindow
from orienteering_startlist_screen.utils import parser
from orienteering_startlist_screen.utils.web_server import create_app, WebServerThread
from orienteering_startlist_screen.utils.generate_demo_files import generate_individual_startlist_xml
from orienteering_startlist_screen.views.start_and_port_select_dialog import StartAndPortSelectDialog

logger = logging.getLogger(__name__)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, application: QtWidgets.QApplication):
        super().__init__()
        self.app = application
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QCoreApplication.setOrganizationName(config.organization_name)
        QCoreApplication.setOrganizationDomain(config.organization_domain)
        QCoreApplication.setApplicationName(config.application_name)
        QCoreApplication.setApplicationVersion(config.application_version)

        self.q_settings = QSettings()

        self.xsd_file_path = "./src/orienteering_startlist_screen/resources/iof_v3_0.xsd"
        self.start_list = None
        self.server_running = False
        self.web_servers: dict[Any, Any] = {}

        status_bar_version_label = QtWidgets.QLabel(f"Version: {config.application_version} ")
        self.statusBar().addPermanentWidget(status_bar_version_label)
        copyright_date = datetime.date.today()
        status_bar_copyright_label = QtWidgets.QLabel(f"{copyright_date.year} {config.organization_name} ")
        self.statusBar().addPermanentWidget(status_bar_copyright_label)

        self.ui.button_push_select_file.clicked.connect(self.select_import_file)

        self.ui.button_push_start.setEnabled(False)
        self.ui.button_push_start.clicked.connect(self.start_clock)

        self.ui.button_push_stop.setEnabled(False)
        self.ui.button_push_stop.setVisible(False)
        self.ui.button_push_stop.clicked.connect(self.stop_clock)

        self.ui.action_about.triggered.connect(self.open_about_dialog)
        self.ui.action_generate_demo_fIle.triggered.connect(self.generate_demo_file)

    def generate_demo_file(self) -> None:
        file_path = generate_individual_startlist_xml(num_classes=10, participants_per_class=20)

        if not os.path.isfile(file_path):
            logger.error(f"File {file_path} not found")
            QMessageBox.critical(self, "Error", f"File {file_path} not found")
            return

        self.select_import_file(file_path)

    def open_about_dialog(self) -> None:
        QMessageBox.about(
            self,
            "About",
            (
                f"<b>{config.application_name}</b><br>"
                f"Version: {config.application_version}<br>"
                f"by: {config.organization_name}<br><br>"
                "Source code on "
                "<a href='https://github.com/lenz-exe/orienteering-startlist-screen/'>GitHub</a>."
            )
        )

    def select_import_file(self, import_file: Optional[str] = None) -> None:
        if not import_file:
            selected_file = self.open_file_dialog(
                title='Open Orienteering-Online File',
                file_extensions='XML Files (*.xml);;All Files (*)',
                default_file_extension='All Files (*)',
                use_last_used_path=True,
                settings_key='last_used_import_path',
                overwrite_last_used_path=True
            )
        else:
            if not os.path.isfile(import_file):
                logger.error(f"File {import_file} not found")
                QMessageBox.critical(self, "Error", f"File {import_file} not found")
                return
            selected_file = import_file

        if selected_file:
            logger.info(f"Selected file: {selected_file}")
            self.q_settings.setValue("last_used_import_path", QtCore.QFileInfo(selected_file).absolutePath())
            self.ui.lineEdit.setText(selected_file)
            self.app.processEvents()
            _, ext = os.path.splitext(selected_file)
            ext = ext.lower()

            try:
                if ext == ".xml":
                    start_list = parser.pars_participants_iof_xml_3_0(
                        xml_file_path=selected_file,
                        xsd_file_path=self.xsd_file_path
                    )
                else:
                    logger.warning(f"Unknown file format: {ext}")
                    QMessageBox.warning(self,"Unknown File Format",
                        f"The selected ({ext}) file format is unknown. Please use 'IOF XML 3.0' or OE2010 (.txt, .csv)")
                    return
            except Exception as e:
                logger.error(f"Failed to read the given file: {e}")
                QMessageBox.critical(self, "Error", f"The start list could not be loaded:\n{e}")
                return

            self.start_list = start_list
            self.ui.button_push_start.setEnabled(True)
            self.ui.label_status.setText("Startlist loaded. Now you can start the webserver.")

    def start_clock(self) -> None:
        if not self.start_list:
            QMessageBox.information(self, "Info", "First import a file please")
            return
        start_name_list = list(self.start_list.keys())
        dialog = StartAndPortSelectDialog(start_name_list=start_name_list)
        if dialog.exec():
            selections = dialog.result_data
            if not selections:
                QMessageBox.information(self, "Info", "No valid port selected.")
                return
        else:
            return

        if self.server_running and self.web_servers:
            self.stop_all_servers()

        slot_seconds = 60
        started_urls = []

        for item in selections:
            host = item['host']
            port = int(item['port'])
            selection = item['combo']

            start_list = self.start_list.get(selection)
            app = create_app(start_list=start_list, slot_seconds=slot_seconds)
            server = WebServerThread(app, host=host, port=port)
            try:
                server.start()
            except Exception as e:
                logger.error(f"Failed to start server ({host}:{port}): {e}")
                QMessageBox.critical(self, "Error", f"Failed to start server ({host}:{port}): {e}")
                continue
            self.web_servers[(host, port)] = server
            started_urls.append(f"http://{host}:{port}/")

        if not started_urls:
            QMessageBox.information(self, "Info", "No server started.")
            return

        self.server_running = True

        if len(started_urls) == 1:
            self.ui.label_status.setText(f"Local webserver running: {started_urls[0]}")
        else:
            joined = " | ".join(started_urls[:3])
            more = "" if len(started_urls) <= 3 else f" (+{len(started_urls)-3} more)"
            self.ui.label_status.setText(f"{len(started_urls)} Webserver running: {joined}{more}")

        try:
            for url in started_urls[:3]:
                webbrowser.open(url)
        except Exception:
            pass

        self.ui.button_push_start.setVisible(False)
        self.ui.button_push_start.setEnabled(False)
        self.ui.button_push_stop.setEnabled(True)
        self.ui.button_push_stop.setVisible(True)

    def stop_clock(self) -> None:
        if not self.server_running:
            return
        self.stop_all_servers()
        self.server_running = False
        self.ui.label_status.setText("Stopped webserver")
        self.ui.button_push_start.setVisible(True)
        self.ui.button_push_start.setEnabled(True)
        self.ui.button_push_stop.setEnabled(False)
        self.ui.button_push_stop.setVisible(False)

    def closeEvent(self, event) -> None:
        try:
            if self.server_running and self.web_servers:
                self.stop_all_servers()
        except Exception as e:
            logger.warning(f"Shutdown failed: {e}")
        super().closeEvent(event)

    def stop_all_servers(self) -> None:
        errors = []
        for key, server in list(self.web_servers.items()):
            try:
                if server:
                    server.shutdown()
            except Exception as e:
                errors.append(f"{key}: {e}")
                logger.error(f"Shutdown failed {key}: {e}")
        self.web_servers.clear()
        if errors:
            QMessageBox.critical(self, "Shutdown-Error", f"Some servers could not be shut down correctly:\n {'\n'.join(errors)}")

    def open_file_dialog(self, title: str = 'Open File', file_extensions: str = 'All Files(*)',
                         default_file_extension: str = 'All Files(*)', use_last_used_path: bool = False,
                         settings_key: Optional[str] = None, overwrite_last_used_path: bool = False) \
            -> Optional[str]:
        if use_last_used_path and settings_key:
            last_path = str(self.q_settings.value(settings_key, ""))
        else:
            last_path = ""

        dialog = QFileDialog(self, title, last_path, file_extensions)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.selectNameFilter(default_file_extension)

        if dialog.exec_():
            selected_file = dialog.selectedFiles()[0]  # This gets the selected file path
            if overwrite_last_used_path and settings_key:
                self.q_settings.setValue(settings_key, QFileInfo(selected_file).absolutePath())
            return selected_file
        return None
