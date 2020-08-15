from PyQt5 import QtCore, QtGui, QtWidgets
import configparser
# 重写QMainWindow
class MainWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        conf = configparser.ConfigParser()
        conf.read("gameSetting.ini")
        conf.set("DEFAULT", "mainWinTop", str(self.x()))
        conf.set("DEFAULT", "mainWinLeft", str(self.y()))
        conf.write(open('gameSetting.ini', "w"))