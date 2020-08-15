from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mineSweeperGUI
import mainWindowGUI

# import sweeper
if __name__ == "__main__":
    app = QtWidgets.QApplication (sys.argv)
#    app.aboutToQuit.connect(app.deleteLater)
    mainWindow = mainWindowGUI.MainWindow ()
    ui = mineSweeperGUI.MineSweeperGUI (mainWindow)
    mainWindow.show()
    sys.exit (app.exec_())



#bug:
#    自定义模式的鲁棒性
#    生成无猜局面时增加一种鲁棒的“快速模式”
#    点不动的问题
#    增加源码链接、使用说明链接、传播许可
#    可选择的无猜局面算法（筛选算法或修改算法）
#    快速给出多变量方程的解的算法
#    计算每格概率的子函数
#    “可能在标记双击未打开局面时，按下方格的阴影没有恢复”
#    初级方格过小时崩溃
#    菜单上有些快捷键没有用
#    起手卡顿
#    雷数多一颗问题