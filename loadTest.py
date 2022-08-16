from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic,QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class page(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("remote.ui",self)
        self.setWindowTitle("bar hide")
        #self.setWindowOpacity(0.3)
        #self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        #self.setAttribute(Qt.WA_TranslucentBackground, True)
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__=="__main__":
    import sys
    import os
    os.chdir(r"C:\Users\14540\Desktop\QTRemote")
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = page()
    MainWindow.show()
    

    sys.exit(app.exec_())
    