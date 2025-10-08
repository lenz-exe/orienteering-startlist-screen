import sys
import traceback
import locale
import os
import logging
from logging.handlers import RotatingFileHandler
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLocale, QSettings, QStandardPaths, QCoreApplication
from orienteering_startlist_screen.views.main_window import MainWindow
from orienteering_startlist_screen import config
from qt_material import apply_stylesheet
from pathlib import Path

logger = logging.getLogger(__name__)


def main():
    app = QApplication(sys.argv)
    QCoreApplication.setOrganizationName(config.organization_name)
    QCoreApplication.setOrganizationDomain(config.organization_domain)
    QCoreApplication.setApplicationName(config.application_name)
    QCoreApplication.setApplicationVersion(config.application_version)

    QSettings.setDefaultFormat(QSettings.IniFormat)
    q_settings = QSettings()
    q_settings.setValue("language", "en_EN")

    app_dir = Path(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation))
    app_dir.mkdir(parents=True, exist_ok=True)
    log_path = app_dir / f"{config.module_name}.log"
    rot_log_handler = RotatingFileHandler(
        filename=str(log_path),
        maxBytes=750000,
        backupCount=2,
        delay=False,
        errors=None)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s:%(funcName)s(%(lineno)d): %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        encoding='utf-8',
        handlers=[rot_log_handler]
    )
    logger.info(f"Tool started | Version: {config.application_version}")

    language = config.application_language
    QLocale.setDefault(QLocale(language))
    locale.setlocale(locale.LC_ALL, "")

    extra = {
        "danger": "#b00020",
        "warning": "#ffb300",
        "success": "#4caf50",
        'density_scale': '-1',
    }

    theme_path = "src/orienteering_startlist_screen/resources/theme_forest.xml"
    if not os.path.exists(theme_path):
        theme_path = "theme_forest.xml"
    apply_stylesheet(app, theme=theme_path, extra=extra)

    main_window = MainWindow(application=app)
    try:
        main_window.show()
        main_window.repaint()
        sys.exit(app.exec())
    except Exception as e:
        logger.error(f"Error in MainWindow: {str(e)}")
        raise Exception(e)


if __name__ == "__main__":
    try:
        main()
    except Exception as error_message:
        print(f"Critical failure: {error_message}")
        logger.error(str(error_message))
        logger.error(traceback.format_exc())
        sys.exit(1)
