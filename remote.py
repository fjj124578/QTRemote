# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remote.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 495)
        MainWindow.setStyleSheet("\n"
"QWidget{\n"
"background:rgba(66,250,1,0)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"    background:rgba(31,219,167,0.86);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("QLabel{\n"
"    font-size:20px;\n"
"    font-weight: bold;\n"
"    \n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("QPushButton{\n"
"    background:rgba(46,121,242,1)\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("QPushButton{\n"
"    background:rgba(46,121,242,1)\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setStyleSheet("QFrame{\n"
"    background:rgba(21, 219, 167,0.5);\n"
"}\n"
"QLabel{\n"
"    background:rgba(127,31,219,1);\n"
"    color:white;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setMaximumSize(QtCore.QSize(30, 30))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame_4)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_2.addWidget(self.lcdNumber_2, 2, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_4)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setMaximumSize(QtCore.QSize(30, 30))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setStyleSheet("QPushButton{\n"
"    background:rgba(46,121,242,1)\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setMaximumSize(QtCore.QSize(300, 160))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Republic_of_China_Army_(ROCA)_Logo.svg.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "自宅総合コントロールパネル"))
        self.pushButton.setText(_translate("MainWindow", "部屋点灯"))
        self.pushButton_2.setText(_translate("MainWindow", "部屋消灯"))
        self.pushButton_3.setText(_translate("MainWindow", "HKStudio"))
        self.pushButton_4.setText(_translate("MainWindow", "AC除湿"))
        self.pushButton_6.setText(_translate("MainWindow", "AC停止"))
        self.pushButton_5.setText(_translate("MainWindow", "AC冷房"))
        self.label_2.setText(_translate("MainWindow", "室内温度"))
        self.label_3.setText(_translate("MainWindow", "室内湿度"))
        self.label_5.setText(_translate("MainWindow", "%"))
        self.label_4.setText(_translate("MainWindow", "度"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
