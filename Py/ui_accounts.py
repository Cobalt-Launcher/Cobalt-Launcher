
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accounts.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(873, 381)
        self.st_mn_inside = QWidget()
        self.st_mn_inside.setObjectName(u"st_mn_inside")
        self.tabWidget_3 = QTabWidget(self.st_mn_inside)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(0, 0, 871, 361))
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.account_2 = QComboBox(self.tab_4)
        self.account_2.setObjectName(u"account_2")
        self.account_2.setGeometry(QRect(10, 30, 411, 21))
        self.pushButton_8 = QPushButton(self.tab_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(670, 60, 101, 51))
        self.pushButton_9 = QPushButton(self.tab_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(560, 60, 101, 51))
        self.pushButton_6 = QPushButton(self.tab_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(440, 60, 111, 51))
        self.Enter_nickname_15 = QLineEdit(self.tab_4)
        self.Enter_nickname_15.setObjectName(u"Enter_nickname_15")
        self.Enter_nickname_15.setGeometry(QRect(440, 30, 411, 20))
        self.label_9 = QLabel(self.tab_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 161, 21))
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(440, 10, 161, 21))
        self.label_13 = QLabel(self.tab_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 210, 531, 101))
        self.tabWidget_3.addTab(self.tab_4, "")
        DockWidget.setWidget(self.st_mn_inside)

        self.retranslateUi(DockWidget)

        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"DockWidget", None))
        self.pushButton_8.setText(QCoreApplication.translate("DockWidget", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_9.setText(QCoreApplication.translate("DockWidget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_6.setText(QCoreApplication.translate("DockWidget", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.Enter_nickname_15.setText("")
        self.label_9.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">\u0421\u043f\u0438\u0441\u043e\u043a \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u043e\u0432:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("DockWidget", u"<html><head/><body><p><span style=\" font-weight:700;\">\u041f\u043e\u0434\u043e\u0439\u0434\u0435\u0442 \u0434\u043b\u044f \u0438\u0433\u0440\u043e\u043a\u043e\u0432 \u0431\u0435\u0437 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0438, \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0443 \u0432\u0430\u0441 </span></p><p><span style=\" font-weight:700;\">\u043d\u0435 \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u0441\u044f \u0437\u0430\u0445\u043e\u0434\u0438\u0442\u044c \u043d\u0430 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u043e\u043d\u043d\u044b\u0435 \u0441\u0435\u0440\u0432\u0435\u0440\u0430 \u0442\u043e\u043b\u044c\u043a\u043e \u0441 \u043f\u0438\u0440\u0430\u0442\u0441\u043a\u0438\u0445 \u0441\u0435\u0440\u0432\u0435\u0440\u043e\u0432. </span></p><p><span style=\" font-weight:700;\">\u041d\u0430\u0441\u0447\u0435\u0442 \u0441\u043a\u0438\u043d\u043e\u0432 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u0443\u044e"
                        " \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u0443\u044e \u0441\u0438\u0441\u0442\u0435\u043c\u0443 \u0441\u043a\u0438\u043d\u043e\u0432 Ely.by. </span></p><p><span style=\" font-weight:700;\">\u0414\u043b\u044f \u043f\u043b\u0430\u0449\u0435\u0439 \u043c\u043e\u0434 Cosmetica, \u0435\u0449\u0451 \u043e\u043d \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u0448\u043b\u044f\u043f\u044b, \u043d\u0430\u043f\u043b\u0435\u0447\u043d\u0438\u043a\u0438 \u0438 \u0434\u0440\u0443\u0433\u0438\u0435 \u0443\u043a\u0440\u0430\u0448\u0435\u043d\u0438\u044f.</span></p></body></html>", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), QCoreApplication.translate("DockWidget", u"\u041e\u0444\u0444\u043b\u0430\u0439\u043d \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
    # retranslateUi

