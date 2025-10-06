# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)
import orienteering_startlist_screen.resources.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(400, 300))
        MainWindow.setMaximumSize(QSize(700, 500))
        icon = QIcon()
        icon.addFile(u":/icons/images/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName(u"action_help")
        self.action_help.setEnabled(False)
        icon1 = QIcon(QIcon.fromTheme(u"help-faq"))
        self.action_help.setIcon(icon1)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        icon2 = QIcon(QIcon.fromTheme(u"help-about"))
        self.action_about.setIcon(icon2)
        self.action_generate_demo_fIle = QAction(MainWindow)
        self.action_generate_demo_fIle.setObjectName(u"action_generate_demo_fIle")
        icon3 = QIcon(QIcon.fromTheme(u"document-new"))
        self.action_generate_demo_fIle.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.horizontalSpacer_3 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_toolname = QLabel(self.widget_4)
        self.label_toolname.setObjectName(u"label_toolname")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(17)
        font.setBold(True)
        self.label_toolname.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_toolname)

        self.horizontalSpacer_4 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(11)
        self.lineEdit.setFont(font1)
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.button_push_select_file = QPushButton(self.widget)
        self.button_push_select_file.setObjectName(u"button_push_select_file")
        self.button_push_select_file.setFont(font1)

        self.horizontalLayout_2.addWidget(self.button_push_select_file)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(145, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_push_start = QPushButton(self.widget_2)
        self.button_push_start.setObjectName(u"button_push_start")
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(14)
        self.button_push_start.setFont(font2)

        self.horizontalLayout.addWidget(self.button_push_start)

        self.button_push_stop = QPushButton(self.widget_2)
        self.button_push_stop.setObjectName(u"button_push_stop")
        self.button_push_stop.setFont(font2)

        self.horizontalLayout.addWidget(self.button_push_stop)

        self.horizontalSpacer_2 = QSpacerItem(144, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(161, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.label_status = QLabel(self.widget_3)
        self.label_status.setObjectName(u"label_status")
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(10)
        self.label_status.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_status)

        self.horizontalSpacer_5 = QSpacerItem(160, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(145, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.listWidget_running_servers = QListWidget(self.widget_5)
        self.listWidget_running_servers.setObjectName(u"listWidget_running_servers")
        self.listWidget_running_servers.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_5.addWidget(self.listWidget_running_servers)

        self.horizontalSpacer_8 = QSpacerItem(144, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addWidget(self.widget_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 33))
        self.menubar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_help.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_help)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.action_generate_demo_fIle)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple-Pre-Start-Clock", None))
        self.action_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.action_help.setToolTip(QCoreApplication.translate("MainWindow", u"Opens a help page in the browser", None))
#endif // QT_CONFIG(tooltip)
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.action_about.setToolTip(QCoreApplication.translate("MainWindow", u"Get informations about the program", None))
#endif // QT_CONFIG(tooltip)
        self.action_generate_demo_fIle.setText(QCoreApplication.translate("MainWindow", u"Generate Demo FIle", None))
        self.label_toolname.setText(QCoreApplication.translate("MainWindow", u"Orienteering-Startlist-Screen", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path to file", None))
        self.button_push_select_file.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.button_push_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.button_push_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Status...", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

