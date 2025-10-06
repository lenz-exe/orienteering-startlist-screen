# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_port_select_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import orienteering_startlist_screen.resources.resources_rc

class Ui_StartPortSelectDialog(object):
    def setupUi(self, StartPortSelectDialog):
        if not StartPortSelectDialog.objectName():
            StartPortSelectDialog.setObjectName(u"StartPortSelectDialog")
        StartPortSelectDialog.resize(473, 315)
        icon = QIcon()
        icon.addFile(u":/icons/images/logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        StartPortSelectDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(StartPortSelectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.widget_4 = QWidget(StartPortSelectDialog)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.horizontalSpacer_3 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_toolname = QLabel(self.widget_4)
        self.label_toolname.setObjectName(u"label_toolname")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(14)
        font.setBold(True)
        self.label_toolname.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_toolname)

        self.horizontalSpacer_4 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(StartPortSelectDialog)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout = QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label_max_servers = QLabel(self.widget_5)
        self.label_max_servers.setObjectName(u"label_max_servers")

        self.horizontalLayout.addWidget(self.label_max_servers)

        self.horizontalSpacer_6 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.widget_5)

        self.scrollArea = QScrollArea(StartPortSelectDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 180))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 467, 218))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(StartPortSelectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(StartPortSelectDialog)
        self.buttonBox.accepted.connect(StartPortSelectDialog.accept)
        self.buttonBox.rejected.connect(StartPortSelectDialog.reject)

        QMetaObject.connectSlotsByName(StartPortSelectDialog)
    # setupUi

    def retranslateUi(self, StartPortSelectDialog):
        StartPortSelectDialog.setWindowTitle(QCoreApplication.translate("StartPortSelectDialog", u"Start and Port Dialog", None))
        self.label_toolname.setText(QCoreApplication.translate("StartPortSelectDialog", u"Please select minimal one start", None))
        self.label_max_servers.setText(QCoreApplication.translate("StartPortSelectDialog", u"TextLabel", None))
    # retranslateUi

