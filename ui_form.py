# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(788, 593)
        font = QFont()
        font.setFamilies([u"High Speed"])
        font.setPointSize(28)
        Widget.setFont(font)
        Widget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-10, 0, 801, 601))
        self.stackedWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setFrameShape(QFrame.Shape.Box)
        self.MenuPage1 = QWidget()
        self.MenuPage1.setObjectName(u"MenuPage1")
        self.author_title = QLabel(self.MenuPage1)
        self.author_title.setObjectName(u"author_title")
        self.author_title.setGeometry(QRect(210, 550, 391, 31))
        font1 = QFont()
        font1.setFamilies([u"High Speed"])
        font1.setPointSize(16)
        self.author_title.setFont(font1)
        self.settings_button = QPushButton(self.MenuPage1)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(140, 340, 511, 71))
        self.createserver_button = QPushButton(self.MenuPage1)
        self.createserver_button.setObjectName(u"createserver_button")
        self.createserver_button.setGeometry(QRect(140, 140, 511, 71))
        self.help_button = QPushButton(self.MenuPage1)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setGeometry(QRect(140, 440, 511, 61))
        self.menu_title = QLabel(self.MenuPage1)
        self.menu_title.setObjectName(u"menu_title")
        self.menu_title.setGeometry(QRect(120, 20, 571, 71))
        font2 = QFont()
        font2.setFamilies([u"High Speed"])
        font2.setPointSize(26)
        font2.setBold(False)
        self.menu_title.setFont(font2)
        self.version_title = QLabel(self.MenuPage1)
        self.version_title.setObjectName(u"version_title")
        self.version_title.setGeometry(QRect(220, 80, 361, 31))
        self.version_title.setFont(font1)
        self.manageservers_button = QPushButton(self.MenuPage1)
        self.manageservers_button.setObjectName(u"manageservers_button")
        self.manageservers_button.setGeometry(QRect(140, 240, 511, 71))
        font3 = QFont()
        font3.setFamilies([u"High Speed"])
        font3.setPointSize(26)
        self.manageservers_button.setFont(font3)
        self.stackedWidget.addWidget(self.MenuPage1)
        self.CreateServerStep1 = QWidget()
        self.CreateServerStep1.setObjectName(u"CreateServerStep1")
        self.installsteamcmd_title = QLabel(self.CreateServerStep1)
        self.installsteamcmd_title.setObjectName(u"installsteamcmd_title")
        self.installsteamcmd_title.setGeometry(QRect(140, 30, 521, 61))
        self.installsteamcmd_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.installsteamcmd_button = QPushButton(self.CreateServerStep1)
        self.installsteamcmd_button.setObjectName(u"installsteamcmd_button")
        self.installsteamcmd_button.setGeometry(QRect(150, 270, 491, 81))
        font4 = QFont()
        font4.setFamilies([u"High Speed"])
        font4.setPointSize(20)
        self.installsteamcmd_button.setFont(font4)
        self.testinternet_button = QPushButton(self.CreateServerStep1)
        self.testinternet_button.setObjectName(u"testinternet_button")
        self.testinternet_button.setGeometry(QRect(160, 130, 471, 51))
        self.testinternet_button.setFont(font1)
        self.continue_button = QPushButton(self.CreateServerStep1)
        self.continue_button.setObjectName(u"continue_button")
        self.continue_button.setGeometry(QRect(260, 430, 251, 71))
        self.continue_button.setFont(font4)
        self.stackedWidget.addWidget(self.CreateServerStep1)
        self.CreateServerStep2 = QWidget()
        self.CreateServerStep2.setObjectName(u"CreateServerStep2")
        self.installserver_button = QPushButton(self.CreateServerStep2)
        self.installserver_button.setObjectName(u"installserver_button")
        self.installserver_button.setGeometry(QRect(140, 300, 501, 81))
        self.installserver_button.setFont(font4)
        self.installserver_title = QLabel(self.CreateServerStep2)
        self.installserver_title.setObjectName(u"installserver_title")
        self.installserver_title.setGeometry(QRect(110, 30, 581, 61))
        self.installserver_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.installserver_note = QLabel(self.CreateServerStep2)
        self.installserver_note.setObjectName(u"installserver_note")
        self.installserver_note.setGeometry(QRect(150, 90, 491, 121))
        font5 = QFont()
        font5.setFamilies([u"Consolas"])
        font5.setPointSize(12)
        self.installserver_note.setFont(font5)
        self.installserver_note.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.installserver_note.setWordWrap(True)
        self.stackedWidget.addWidget(self.CreateServerStep2)
        self.HelpPage = QWidget()
        self.HelpPage.setObjectName(u"HelpPage")
        self.stackedWidget.addWidget(self.HelpPage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.stackedWidget.addWidget(self.SettingsPage)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.author_title.setText(QCoreApplication.translate("Widget", u"By: @leodenglovescode", None))
        self.settings_button.setText(QCoreApplication.translate("Widget", u"Settings", None))
        self.createserver_button.setText(QCoreApplication.translate("Widget", u"Create Server", None))
        self.help_button.setText(QCoreApplication.translate("Widget", u"Help", None))
        self.menu_title.setText(QCoreApplication.translate("Widget", u"CS2 Server Manager", None))
        self.version_title.setText(QCoreApplication.translate("Widget", u"Version Beta Test 1.0.0", None))
        self.manageservers_button.setText(QCoreApplication.translate("Widget", u"Manage Servers", None))
        self.installsteamcmd_title.setText(QCoreApplication.translate("Widget", u"Install Steamcmd", None))
        self.installsteamcmd_button.setText(QCoreApplication.translate("Widget", u"Install From Steam", None))
        self.testinternet_button.setText(QCoreApplication.translate("Widget", u"Test Internet Connection", None))
        self.continue_button.setText(QCoreApplication.translate("Widget", u"Continue", None))
        self.installserver_button.setText(QCoreApplication.translate("Widget", u"Install Server", None))
        self.installserver_title.setText(QCoreApplication.translate("Widget", u"Install CS2 Server", None))
        self.installserver_note.setText(QCoreApplication.translate("Widget", u"Note: Please wait patiently for SteamCMD to download the game, as the current CS2 has no dedicated server like csgo, you will have to download the full contents of CS2 (About 43GB), please reserve at least 55 GB of free space on your PC, or else the installation will fail due to lack of cache space.", None))
    # retranslateUi

