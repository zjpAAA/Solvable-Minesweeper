from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QCursor


class mineLabel (QtWidgets.QLabel):
    leftRelease = QtCore.pyqtSignal (int, int)  # 定义信号
    rightRelease = QtCore.pyqtSignal (int, int)
    leftPressed = QtCore.pyqtSignal (int, int)
    rightPressed = QtCore.pyqtSignal (int, int)
    leftAndRightPressed = QtCore.pyqtSignal (int, int)
    leftAndRightRelease = QtCore.pyqtSignal (int, int)
    mouseMove = QtCore.pyqtSignal (int, int)
    

    def __init__(self, i, j, num, pixSize, parent=None):
        super (mineLabel, self).__init__ (parent)
        self.num = num
        self.i = i
        self.j = j
        self.leftAndRightClicked = False
        self.status = 0  # 0、1、2、3代表没挖开、挖开、标雷、踩到雷的红雷
        self.pixSize = pixSize
        # self.setMouseTracking(True)

    def mousePressEvent(self, e):  ##重载一下鼠标点击事件
        if e.buttons () == QtCore.Qt.LeftButton | QtCore.Qt.RightButton:
            self.leftAndRightPressed.emit (self.i, self.j)
            self.leftAndRightClicked = True
        else:
            if e.buttons () == QtCore.Qt.LeftButton:
                self.leftPressed.emit (self.i, self.j)
            elif e.buttons () == QtCore.Qt.RightButton:
                self.rightPressed.emit (self.i, self.j)

    def mouseReleaseEvent(self, e):
        #每个标签的鼠标事件发射给槽的都是自身的坐标
        #所以获取释放点相对本标签的偏移量，矫正发射的信号
        xx = e.localPos().x()
        yy = e.localPos().y()
        if self.leftAndRightClicked:
            self.leftAndRightRelease.emit (self.i + yy//self.pixSize, self.j + xx//self.pixSize)
            self.leftAndRightClicked=False
        else:
            if e.button () == QtCore.Qt.LeftButton:
                self.leftRelease.emit (self.i + yy//self.pixSize, self.j + xx//self.pixSize)
            elif e.button () == QtCore.Qt.RightButton:
                self.rightRelease.emit (self.i + yy//self.pixSize, self.j + xx//self.pixSize)
    
    def mouseMoveEvent(self, e):
        #每个格子变成阴影的信号不是由这个格子自身发出的
        xx = e.localPos().x()
        yy = e.localPos().y()
        self.mouseMove.emit (self.i + yy//self.pixSize, self.j + xx//self.pixSize)
    
    
    
            
            
            
            
        