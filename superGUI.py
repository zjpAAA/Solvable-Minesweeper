from PyQt5 import QtCore, QtGui, QtWidgets
import statusLabel
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)#垂直布局
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)#QFrame是基本控件的基类
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)#水平布局
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)#label是雷数
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding, 
                                           QtWidgets.QSizePolicy.Minimum)#弹簧
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = statusLabel.StatusLabel(self.frame)#label2是脸
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2, 0 , QtCore.Qt.AlignCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, 
                                            QtWidgets.QSizePolicy.Expanding, 
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.frame)#label3是时间
        self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frame)   #把frame添加到垂直布局的上面
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)  #整个局面的框
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
       
        self.verticalLayout.addWidget(self.frame_2)
        
        self.label_4 = QtWidgets.QLabel(MainWindow)#label3是时间
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        
        self.menu2 = QtWidgets.QMenu(self.menubar)
        self.menu2.setObjectName("menu2")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setCheckable(False)
        self.action.setChecked(False)
        self.action.setObjectName("action")
        self.action_B = QtWidgets.QAction(MainWindow)
        self.action_B.setCheckable(True)
        self.action_B.setObjectName("action_B")
        self.action_E = QtWidgets.QAction(MainWindow)
        self.action_E.setCheckable(True)
        self.action_E.setObjectName("action_E")
        self.action_C = QtWidgets.QAction(MainWindow)
        self.action_C.setCheckable(True)
        self.action_C.setObjectName("action_C")
        self.action_X_2 = QtWidgets.QAction(MainWindow)
        self.action_X_2.setObjectName("action_X_2")
        self.action_I = QtWidgets.QAction(MainWindow)
        self.action_I.setCheckable(True)
        self.action_I.setObjectName("action_I")
        
        self.action_N = QtWidgets.QAction(MainWindow)
        self.action_N.setObjectName("action_N")
        
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_B)
        self.menu.addAction(self.action_I)
        self.menu.addAction(self.action_E)
        self.menu.addAction(self.action_C)
        self.menu.addSeparator()
        self.menu.addAction(self.action_X_2)
        self.menu2.addAction(self.action_N)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu2.menuAction())
        
        self.frameShortcut1 = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_1), MainWindow)
        self.frameShortcut2 = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_2), MainWindow)
        self.frameShortcut3 = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_3), MainWindow)
        self.frameShortcut4 = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F2), MainWindow)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "黑猫扫雷"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "underway"))
        self.label_3.setText(_translate("MainWindow", "0.00"))
        self.menu.setTitle(_translate("MainWindow", "游戏(&G)"))
        
        self.menu2.setTitle(_translate("MainWindow", "设置(&F)"))
        
        self.action.setText(_translate("MainWindow", "新游戏(&N)"))
        self.action_B.setText(_translate("MainWindow", "初级(&B)"))
        self.action_I.setText(_translate("MainWindow", "中级(&I)"))
        self.action_E.setText(_translate("MainWindow", "高级(&E)"))
        self.action_C.setText(_translate("MainWindow", "自定义(&C)"))
        self.action_X_2.setText(_translate("MainWindow", "退出(&X)"))
        
        self.action_N.setText(_translate("MainWindow", "游戏设置(&N)"))


    
        
   



