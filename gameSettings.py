from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self, min3BV, max3BV, timesLimit, enuLimit,gameMode):
        self.min3BV = min3BV
        self.max3BV = max3BV
        self.timesLimit = timesLimit
        self.enuLimit = enuLimit
        self.gameMode = gameMode
        
        self.alter = False
        self.Dialog = QtWidgets.QDialog ()
        self.setupUi (self.Dialog)
        self.setParameter ()
        self.Dialog.setWindowIcon (QtGui.QIcon ("media/cat.ico"))
        self.pushButton.clicked.connect (self.processParameter)
        self.pushButton_2.clicked.connect (self.Dialog.close)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(697, 386)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:\\SpyderWork\\Minesweeper_solvable_PyQt5\\media/cat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 65, 81, 31))
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 35, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 105, 101, 31))
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 145, 91, 31))
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(540, 110, 101, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 14pt \"宋体\";border-radius:4px;border:2px groove gray;\n"
"background-color: rgb(220, 220, 220);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 210, 101, 51))
        self.pushButton_2.setStyleSheet("font: 14pt \"宋体\";border-radius:4px;border:2px groove gray;\n"
"background-color: rgb(220, 220, 220);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 113, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 70, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 110, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 150, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(330, 30, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 75, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(330, 120, 115, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(330, 165, 115, 19))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setGeometry(QtCore.QRect(330, 210, 115, 19))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(Form)
        self.radioButton_6.setGeometry(QtCore.QRect(330, 255, 115, 19))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(Form)
        self.radioButton_7.setGeometry(QtCore.QRect(330, 300, 115, 19))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(Form)
        self.radioButton_8.setGeometry(QtCore.QRect(330, 345, 115, 19))
        self.radioButton_8.setObjectName("radioButton_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "游戏设置"))
        self.label.setText(_translate("Form", "3BV最大值"))
        self.label_2.setText(_translate("Form", "3BV最小值"))
        self.label_3.setText(_translate("Form", "最大尝试次数"))
        self.label_4.setText(_translate("Form", "最大枚举长度"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.radioButton.setText(_translate("Form", "标准"))
        self.radioButton_2.setText(_translate("Form", "win7"))
        self.radioButton_3.setText(_translate("Form", "竞速无猜"))
        self.radioButton_4.setText(_translate("Form", "强无猜"))
        self.radioButton_5.setText(_translate("Form", "弱无猜"))
        self.radioButton_6.setText(_translate("Form", "准无猜"))
        self.radioButton_7.setText(_translate("Form", "强可猜"))
        self.radioButton_8.setText(_translate("Form", "弱可猜"))
        
        
    def setParameter(self):
        self.lineEdit.setText (str(self.min3BV))
        self.lineEdit_2.setText (str(self.max3BV))
        self.lineEdit_3.setText (str(self.timesLimit))
        self.lineEdit_4.setText (str(self.enuLimit))
        if self.gameMode == 0:
            self.radioButton.setChecked(True)
        elif self.gameMode == 1:
            self.radioButton_2.setChecked(True)
        elif self.gameMode == 2:
            self.radioButton_3.setChecked(True)
        elif self.gameMode == 3:
            self.radioButton_4.setChecked(True)
        elif self.gameMode == 4:
            self.radioButton_5.setChecked(True)
        elif self.gameMode == 5:
            self.radioButton_6.setChecked(True)
        elif self.gameMode == 6:
            self.radioButton_7.setChecked(True)
        else:
            self.radioButton_8.setChecked(True)
        
        
    def processParameter(self):
        a = int(self.lineEdit.text())
        b = int(self.lineEdit_2.text())
        c = int(self.lineEdit_3.text())
        d = int(self.lineEdit_4.text())
        # if a != self.min3BV or b != self.max3BV or c != self.timesLimit or d!= self.enuLimit:
        self.alter = True
        self.min3BV = a
        self.max3BV = b
        self.timesLimit = c
        self.enuLimit = d
        if self.radioButton.isChecked() == True:
            self.gameMode = 0
        elif self.radioButton_2.isChecked() == True:
            self.gameMode = 1
        elif self.radioButton_3.isChecked() == True:
            self.gameMode = 2
        elif self.radioButton_4.isChecked() == True:
            self.gameMode = 3
        elif self.radioButton_5.isChecked() == True:
            self.gameMode = 4
        elif self.radioButton_6.isChecked() == True:
            self.gameMode = 5
        elif self.radioButton_7.isChecked() == True:
            self.gameMode = 6
        elif self.radioButton_8.isChecked() == True:
            self.gameMode = 7
            
            
        self.Dialog.close ()

        
        
        
        
