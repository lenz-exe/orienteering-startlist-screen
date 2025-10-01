import sys
import traceback
import locale
import logging
from logging.handlers import RotatingFileHandler

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLocale
from orienteering_startlist_screen.views.main_window import MainWindow
from orienteering_startlist_screen import config

logger = logging.getLogger(__name__)


# def load_stylesheet():
#     with open("./src/orienteering_startlist_screen/resources/style.qss", "r") as file:
#         return file.read()

def main():
    log_name = f"{config.module_name}.log"
    rot_log_handler = RotatingFileHandler(
        filename=log_name,
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
    logger.info(f"{'*' * 60}")
    logger.info(f"Tool-Name: {config.application_name}")
    logger.info(f"Tool-Version: {config.application_version}")
    logger.info(f"{'*' * 60}")

    app = QApplication(sys.argv)
    # app.setStyleSheet(load_stylesheet())
    app.setObjectName(config.module_name)
    app.setOrganizationName(config.application_name)
    app.setOrganizationDomain(config.organization_domain)
    app.setApplicationName(config.application_name)
    app.setApplicationVersion(config.application_version)

    language = config.application_language
    QLocale.setDefault(QLocale(language))
    locale.setlocale(locale.LC_ALL, "")

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
