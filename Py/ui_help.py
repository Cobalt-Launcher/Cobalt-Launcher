# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QLabel, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(873, 483)
        self.st_mn_inside = QWidget()
        self.st_mn_inside.setObjectName(u"st_mn_inside")
        self.help_menu = QTabWidget(self.st_mn_inside)
        self.help_menu.setObjectName(u"help_menu")
        self.help_menu.setGeometry(QRect(0, 0, 871, 461))
        self.Technical_support = QWidget()
        self.Technical_support.setObjectName(u"Technical_support")
        self.share_with_log = QPushButton(self.Technical_support)
        self.share_with_log.setObjectName(u"share_with_log")
        self.share_with_log.setGeometry(QRect(10, 370, 141, 51))
        self.share_with_report = QPushButton(self.Technical_support)
        self.share_with_report.setObjectName(u"share_with_report")
        self.share_with_report.setGeometry(QRect(160, 370, 141, 51))
        self.Telegram_help_menu = QPushButton(self.Technical_support)
        self.Telegram_help_menu.setObjectName(u"Telegram_help_menu")
        self.Telegram_help_menu.setGeometry(QRect(720, 370, 141, 51))
        self.inf_logs_reports = QLabel(self.Technical_support)
        self.inf_logs_reports.setObjectName(u"inf_logs_reports")
        self.inf_logs_reports.setGeometry(QRect(10, 10, 821, 361))
        self.view_log = QPushButton(self.Technical_support)
        self.view_log.setObjectName(u"view_log")
        self.view_log.setGeometry(QRect(350, 370, 141, 51))
        self.view_report = QPushButton(self.Technical_support)
        self.view_report.setObjectName(u"view_report")
        self.view_report.setGeometry(QRect(500, 370, 141, 51))
        self.help_menu.addTab(self.Technical_support, "")
        self.Want_to_help_us = QWidget()
        self.Want_to_help_us.setObjectName(u"Want_to_help_us")
        self.inf_help_developers = QLabel(self.Want_to_help_us)
        self.inf_help_developers.setObjectName(u"inf_help_developers")
        self.inf_help_developers.setGeometry(QRect(10, -20, 401, 281))
        self.Telegram_help_menu2 = QPushButton(self.Want_to_help_us)
        self.Telegram_help_menu2.setObjectName(u"Telegram_help_menu2")
        self.Telegram_help_menu2.setGeometry(QRect(730, 10, 131, 61))
        self.help_menu.addTab(self.Want_to_help_us, "")
        DockWidget.setWidget(self.st_mn_inside)

        self.retranslateUi(DockWidget)

        self.help_menu.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"DockWidget", None))
        self.share_with_log.setText(QCoreApplication.translate("DockWidget", u"\u041f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f \u0441 \u043b\u043e\u0433\u043e\u043c", None))
        self.share_with_report.setText(QCoreApplication.translate("DockWidget", u"\u041f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f \u0441 \u0440\u0435\u043f\u043e\u0440\u0442\u043e\u043c", None))
        self.Telegram_help_menu.setText(QCoreApplication.translate("DockWidget", u"\u041d\u0430\u0448 Telegram", None))
        self.inf_logs_reports.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">\u0427\u0442\u043e \u0442\u0430\u043a\u043e\u0435 \u043b\u043e\u0433\u0438 \u0438 \u043a\u0440\u0430\u0448-\u0440\u0435\u043f\u043e\u0440\u0442\u044b?</span></p><p><span style=\" font-weight:700;\">\u041b\u043e\u0433 (log) \u2014 \u044d\u0442\u043e \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b, \u043a\u0443\u0434\u0430 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0437\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u0432\u0441\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0440\u0430\u0431\u043e\u0442\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b.</span></p><p><span style=\" font-weight:700;\">\u041a\u0440\u0430\u0448-\u0440\u0435\u043f\u043e\u0440\u0442 (crash_reports) \u2014 \u044d\u0442\u043e \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b, \u043a\u0443\u0434\u0430 \u0430\u0432"
                        "\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0437\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u0435\u0442\u0441\u044f \u043f\u0440\u0438\u0447\u0438\u043d\u0430 \u0432\u044b\u043b\u0435\u0442\u0430 \u0438\u0433\u0440\u044b.</span></p><p><span style=\" font-size:11pt; font-weight:700;\">\u0413\u0434\u0435 \u0445\u0440\u0430\u043d\u044f\u0442\u0441\u044f \u043e\u043d\u0438?</span></p><p><span style=\" font-weight:700;\">\u0413\u0434\u0435 \u0445\u0440\u0430\u043d\u044f\u0442\u0441\u044f \u043b\u043e\u0433\u0438 \u043c\u0430\u0439\u043d\u043a\u0440\u0430\u0444\u0442? \u041f\u0443\u0442\u044c \u043a \u0438\u043c \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f\u00a0/AppData/Roaming/.Cobalt_Launcher/logs</span></p><p><span style=\" font-weight:700;\">\u0413\u0434\u0435 \u0445\u0440\u0430\u043d\u044f\u0442\u0441\u044f \u043a\u0440\u0430\u0448-\u0440\u0435\u043f\u043e\u0440\u0442\u044b \u043c\u0430\u0439\u043d\u043a\u0440\u0430\u0444\u0442? \u041f\u0443\u0442\u044c \u043a \u0438\u043c \u043d"
                        "\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f\u00a0/AppData/Roaming/.Cobalt_Launcher/crash-reports</span></p><p><span style=\" font-size:11pt; font-weight:700;\">\u0417\u0430\u0447\u0435\u043c \u043e\u043d\u0438 \u043d\u0430\u043c?</span></p><p><span style=\" font-weight:700;\">\u041b\u043e\u0433\u0438 \u0438 \u0440\u0435\u043f\u043e\u0440\u0442\u044b \u043d\u0443\u0436\u043d\u044b \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043d\u044f\u0442\u044c \u043f\u0440\u0438\u0447\u0438\u043d\u0443 \u0432\u0430\u0448\u0435\u0439 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u044b, \u0431\u0435\u0437 \u043d\u0438\u0445 \u043c\u044b \u044d\u0442\u043e\u0433\u043e \u043d\u0435 \u0441\u043c\u043e\u0436\u0435\u043c! </span></p><p><span style=\" font-size:11pt; font-weight:700;\">\u041a\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u043f\u043e\u043c\u043e\u0447\u044c?</span></p><p><span style=\" font-weight:700;\">\u041b\u044e\u0434\u0438 \u0441 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c\u044e &quot;\u041f\u043e\u043c"
                        "\u043e\u0449\u043d\u0438\u043a&quot;. \u0427\u0442\u043e\u0431\u044b \u043c\u044b \u043f\u043e\u043c\u043e\u0433\u043b\u0438 \u043f\u0438\u0448\u0438\u0442\u0435 \u0432 \u0442\u0435\u043c\u0443 &quot;\u041d\u0443\u0436\u043d\u0430 \u043f\u043e\u043c\u043e\u0449\u044c?&quot;. \u0412 \u0414\u0420\u0423\u0413\u0418\u0425 \u0422\u0415\u041c\u0410\u0425 \u041d\u0415 \u041f\u041e\u041c\u041e\u0413\u0410\u0415\u041c!</span></p><p><span style=\" font-size:11pt; font-weight:700;\">\u041a\u0430\u043a \u0438\u0445 \u0447\u0438\u0442\u0430\u0442\u044c?</span></p><p><span style=\" font-weight:700;\">\u0414\u043b\u044f \u044d\u0442\u043e\u0433\u043e \u043d\u0430\u0434\u043e \u0437\u043d\u0430\u0442\u044c \u0430\u043d\u0433\u043b\u0438\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a, \u0438\u043b\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u043f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a. \u0427\u0438\u0442\u0430\u0442\u044c \u0438\u0445 \u043d\u0430\u0434\u043e \u0441\u0432\u0435\u0440"
                        "\u0445\u0443 \u0432\u043d\u0438\u0437, \u043f\u043e\u043c\u0435\u0447\u0435\u043d\u044b \u043e\u043d\u0438 \u0434\u0430\u0442\u043e\u0439 \u043a\u043e\u0433\u0434\u0430 \u044d\u0442\u043e \u0431\u044b\u043b\u043e.</span></p><p><span style=\" font-weight:700;\"><br/></span></p></body></html>", None))
        self.view_log.setText(QCoreApplication.translate("DockWidget", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043b\u043e\u0433\u0438", None))
        self.view_report.setText(QCoreApplication.translate("DockWidget", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0440\u0435\u043f\u043e\u0440\u0442", None))
        self.help_menu.setTabText(self.help_menu.indexOf(self.Technical_support), QCoreApplication.translate("DockWidget", u"\u0422\u0435\u0445\u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.inf_help_developers.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">\u0423 \u0432\u0430\u0441 \u0435\u0441\u0442\u044c \u0438\u0434\u0435\u044f?</span></p><p><span style=\" font-weight:700;\">\u041f\u0438\u0448\u0438\u0442\u0435 \u0432 \u0442\u0435\u043c\u0443 &quot;\u0418\u0434\u0435\u0438&quot;.</span></p><p><span style=\" font-size:11pt; font-weight:700;\">\u041d\u0430\u0448\u043b\u0438 \u043e\u0448\u0438\u0431\u043a\u0443 \u0432 \u043a\u043e\u0434\u0435 \u0438\u043b\u0438 \u0432 \u0441\u0442\u0430\u0442\u044c\u0435?</span></p><p><span style=\" font-weight:700;\">\u041f\u0438\u0448\u0438\u0442\u0435 \u0432 \u0442\u0435\u043c\u0443 &quot;\u041d\u0430\u0439\u0434\u0435\u043d\u0430 \u043e\u0448\u0438\u0431\u043a\u0430?&quot;.</span></p><p><span style=\" font-size:11pt; font-weight:700;\">\u041a\u0430\u043a \u043e\u0444\u043e\u0440\u043c\u043b\u044f\u0442\u044c \u0430\u043d\u043a\u0435\u0442\u044b?</span></p><p><span style=\" font-weight:700;\">1. \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a</span"
                        "></p><p><span style=\" font-weight:700;\">2. \u0422\u0435\u043a\u0441\u0442</span></p><p><span style=\" font-weight:700;\">3. \u0412 \u043a\u043e\u043d\u0446\u0435 \u043f\u0438\u043d\u0433\u0443\u0435\u0448\u044c @M1rotv0rets \u0438\u043b\u0438 @WaterBucket_smt.</span></p></body></html>", None))
        self.Telegram_help_menu2.setText(QCoreApplication.translate("DockWidget", u"\u041d\u0430\u0448 Telegram", None))
        self.help_menu.setTabText(self.help_menu.indexOf(self.Want_to_help_us), QCoreApplication.translate("DockWidget", u"\u0425\u043e\u0442\u0438\u0442\u0435 \u043f\u043e\u043c\u043e\u0447\u044c \u043d\u0430\u043c?", None))
    # retranslateUi

