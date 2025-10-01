import logging

from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QMessageBox, QHBoxLayout, QVBoxLayout, QWidget,
    QLineEdit, QComboBox, QDialogButtonBox
)

from orienteering_startlist_screen.ui.start_port_select_dialog_ui import Ui_StartPortSelectDialog

logger = logging.getLogger(__name__)


class StartAndPortSelectDialog(QtWidgets.QDialog):
    def __init__(self, start_name_list: list, parent=None):
        super().__init__(parent)
        self.ui = Ui_StartPortSelectDialog()
        self.ui.setupUi(self)

        self.result_data: list[dict] = []
        self._rows: list[dict[str, QLineEdit | QComboBox]] = []

        self.ui.scrollArea.setWidgetResizable(True)
        content = self.ui.scrollAreaWidgetContents

        container_layout = content.layout()
        if container_layout is None:
            container_layout = QVBoxLayout(content)
            container_layout.setContentsMargins(0, 0, 0, 0)
            container_layout.setSpacing(6)

        choices = ['---'] + list(start_name_list)

        port = 5000
        for _ in choices:
            row_layout = QHBoxLayout()

            host_le = QLineEdit("127.0.0.1")
            host_le.setReadOnly(True)

            port_le = QLineEdit(str(port))
            port += 1

            combo = QComboBox()
            combo.addItems(choices)
            combo.setCurrentIndex(0)

            row_layout.addWidget(host_le)
            row_layout.addWidget(port_le)
            row_layout.addWidget(combo)

            row_widget = QWidget()
            row_widget.setLayout(row_layout)
            container_layout.addWidget(row_widget)

            self._rows.append({"host_le": host_le, "port_le": port_le, "combo": combo})

            # set trigger for changes at the QComboBox
            combo.currentIndexChanged.connect(self.update_apply_enabled)

        container_layout.addStretch(1)

        self.ui.buttonBox.button(QDialogButtonBox.Apply).setEnabled(False)
        self.ui.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.handle_apply)
        self.update_apply_enabled()

    def update_apply_enabled(self):
        any_selected = any(r["combo"].currentText() != "---" for r in self._rows)
        self.ui.buttonBox.button(QDialogButtonBox.Apply).setEnabled(any_selected)

    def handle_apply(self):
        errors = []
        results = []
        for row in self._rows:
            combo_box = row["combo"].currentText()
            if combo_box == "---":
                continue

            host = row['host_le'].text().strip()
            port_text = row['port_le'].text().strip()

            # simple port validation
            # port range: 1 - 65535 (16-Bit)
            # reserved ports:
            #   - 0-1023: "well-known ports" (HTTP 80, HTTPS 443, SSH 22, ...)
            # recommended ports:
            #   - 1024-49151: "registered ports"
            #   - 1024–49151 = "registered ports" – may also be occupied, but are usually unproblematic.
            #   - 49152–65535 = "ephemeral/dynamic ports" – fewest conflicts, ideal for test and development servers
            if not port_text.isdigit():
                errors.append(f"Invalid port: {port_text}")
                continue
            if not (1 <= int(port_text) <= 65535):
                errors.append(f"Port is out of range (1-65535): {port_text}")
                continue
            results.append({
                "host": host,
                "port": int(port_text),
                "combo": combo_box,
            })

        if errors:
            QMessageBox.warning(self, "Input Error", "\n".join(errors))
            return
        if not results:
            QMessageBox.information(self, "Note", "Please select at least one option.")
            return
        self.result_data = results
        self.accept()