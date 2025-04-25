# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 516)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bt_play_game_main = QPushButton(self.centralwidget)
        self.bt_play_game_main.setObjectName(u"bt_play_game_main")
        self.bt_play_game_main.setGeometry(QRect(210, 320, 391, 51))
        self.bt_telegram_main = QPushButton(self.centralwidget)
        self.bt_telegram_main.setObjectName(u"bt_telegram_main")
        self.bt_telegram_main.setGeometry(QRect(10, 380, 91, 51))
        self.bt_chs_wl_main = QToolButton(self.centralwidget)
        self.bt_chs_wl_main.setObjectName(u"bt_chs_wl_main")
        self.bt_chs_wl_main.setGeometry(QRect(10, 320, 91, 51))
        self.progressbar_game_main = QProgressBar(self.centralwidget)
        self.progressbar_game_main.setObjectName(u"progressbar_game_main")
        self.progressbar_game_main.setGeometry(QRect(10, 450, 791, 23))
        self.progressbar_game_main.setValue(24)
        self.cb_chs_acc_main = QComboBox(self.centralwidget)
        self.cb_chs_acc_main.addItem("")
        self.cb_chs_acc_main.setObjectName(u"cb_chs_acc_main")
        self.cb_chs_acc_main.setGeometry(QRect(10, 10, 391, 21))
        self.cb_chs_ver = QComboBox(self.centralwidget)
        self.cb_chs_ver.addItem("")
        self.cb_chs_ver.setObjectName(u"cb_chs_ver")
        self.cb_chs_ver.setGeometry(QRect(410, 10, 391, 21))
        self.bt_help_main = QPushButton(self.centralwidget)
        self.bt_help_main.setObjectName(u"bt_help_main")
        self.bt_help_main.setGeometry(QRect(210, 380, 91, 51))
        self.bt_settigs_main = QPushButton(self.centralwidget)
        self.bt_settigs_main.setObjectName(u"bt_settigs_main")
        self.bt_settigs_main.setGeometry(QRect(310, 380, 91, 51))
        self.bt_news_main = QPushButton(self.centralwidget)
        self.bt_news_main.setObjectName(u"bt_news_main")
        self.bt_news_main.setGeometry(QRect(110, 380, 91, 51))
        self.bt_mods_main = QPushButton(self.centralwidget)
        self.bt_mods_main.setObjectName(u"bt_mods_main")
        self.bt_mods_main.setGeometry(QRect(410, 380, 91, 51))
        self.bt_tools_main = QPushButton(self.centralwidget)
        self.bt_tools_main.setObjectName(u"bt_tools_main")
        self.bt_tools_main.setGeometry(QRect(610, 380, 91, 51))
        self.bt_info_main = QPushButton(self.centralwidget)
        self.bt_info_main.setObjectName(u"bt_info_main")
        self.bt_info_main.setGeometry(QRect(510, 380, 91, 51))
        self.bt_program_main = QPushButton(self.centralwidget)
        self.bt_program_main.setObjectName(u"bt_program_main")
        self.bt_program_main.setGeometry(QRect(710, 380, 91, 51))
        self.bt_req_ver_main = QToolButton(self.centralwidget)
        self.bt_req_ver_main.setObjectName(u"bt_req_ver_main")
        self.bt_req_ver_main.setGeometry(QRect(610, 320, 191, 21))
        self.bt_up_ver_main = QToolButton(self.centralwidget)
        self.bt_up_ver_main.setObjectName(u"bt_up_ver_main")
        self.bt_up_ver_main.setGeometry(QRect(610, 350, 191, 21))
        self.wallpaper_menu_main = QLabel(self.centralwidget)
        self.wallpaper_menu_main.setObjectName(u"wallpaper_menu_main")
        self.wallpaper_menu_main.setGeometry(QRect(-20, 40, 861, 271))
        self.wallpaper_menu_main.setPixmap(QPixmap(u"../\u041d\u043e\u0432\u0430\u044f \u043f\u0430\u043f\u043a\u0430/photo_2025-01-23_21-29-06.jpg"))
        self.bt_notes_main = QPushButton(self.centralwidget)
        self.bt_notes_main.setObjectName(u"bt_notes_main")
        self.bt_notes_main.setGeometry(QRect(110, 320, 91, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 812, 21))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_play_game_main.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c!", None))
        self.bt_telegram_main.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u043e", None))
        self.bt_chs_wl_main.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043e\u0431\u043e\u0438", None))
        self.cb_chs_acc_main.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430? \u0414\u043e\u0431\u0430\u0432\u044c\u0442\u0435 \u0435\u0433\u043e \u0432 \u043c\u0435\u043d\u044e \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u044b", None))

        self.cb_chs_ver.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a\u0443\u044e \u0432\u0435\u0440\u0441\u0438\u044e \u0432\u044b\u0431\u0435\u0440\u0435\u0442\u0435?", None))

        self.bt_help_main.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.bt_settigs_main.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.bt_news_main.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0441\u0442\u0438", None))
        self.bt_mods_main.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u044b-\u0441\u0431\u043e\u0440\u043a\u0438", None))
        self.bt_tools_main.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.bt_info_main.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.bt_program_main.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.bt_req_ver_main.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441\u0438\u0442\u044c \u0432\u0435\u0440\u0441\u0438\u044e", None))
        self.bt_up_ver_main.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0432\u0435\u0440\u0441\u0438\u044e", None))
        self.wallpaper_menu_main.setText("")
        self.bt_notes_main.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
    # retranslateUi

