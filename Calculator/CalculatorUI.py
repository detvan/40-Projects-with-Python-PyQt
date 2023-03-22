from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 450)
        MainWindow.setMinimumSize(QtCore.QSize(350, 450))
        MainWindow.setMaximumSize(QtCore.QSize(350, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(350, 450))
        self.centralwidget.setMaximumSize(QtCore.QSize(350, 450))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.screen = QtWidgets.QFrame(self.centralwidget)
        self.screen.setMinimumSize(QtCore.QSize(350, 100))
        self.screen.setMaximumSize(QtCore.QSize(350, 100))
        self.screen.setStyleSheet("QFrame {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #5a677b, stop:1 rgba(90, 121, 116, 255));\n"
"}")
        self.screen.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.screen.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.screen.setObjectName("screen")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.screen)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.screenLabel = QtWidgets.QLabel(self.screen)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(36)
        font.setBold(True)
        self.screenLabel.setFont(font)
        self.screenLabel.setStyleSheet("background-color: rgb(105, 151, 149);\n"
"border: 2px solid #3a5258;\n"
"border-radius: 10px;")
        self.screenLabel.setText("")
        self.screenLabel.setObjectName("screenLabel")
        self.verticalLayout_2.addWidget(self.screenLabel)
        self.verticalLayout.addWidget(self.screen)
        self.panel = QtWidgets.QFrame(self.centralwidget)
        self.panel.setStyleSheet("QFrame {\n"
"    background-color: #5a677b;\n"
"}\n"
"\n"
"QPushButton {\n"
"        background-color: #496b72;\n"
"        color: white;\n"
"        border: 2px solid #3a5258;\n"
"        border-radius: 10px;\n"
"        font-size: 30px;\n"
"        font-weight: bold;\n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        background-color: #699795;\n"
"        color: white;\n"
"        border: 2px solid #3a5258;\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #3a5258;\n"
"        color: white;\n"
"        border: 2px solid #3a5258;\n"
"    }")
        self.panel.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.panel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.panel.setObjectName("panel")
        self.gridLayout_43 = QtWidgets.QGridLayout(self.panel)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.frame_3 = QtWidgets.QFrame(self.panel)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.multiplyButton = QtWidgets.QPushButton(self.frame_3)
        self.multiplyButton.setMaximumSize(QtCore.QSize(78, 71))
        self.multiplyButton.setObjectName("multiplyButton")
        self.gridLayout_3.addWidget(self.multiplyButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_3, 2, 0, 1, 1)
        self.frame_14 = QtWidgets.QFrame(self.panel)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.oneButton = QtWidgets.QPushButton(self.frame_14)
        self.oneButton.setMaximumSize(QtCore.QSize(78, 71))
        self.oneButton.setObjectName("oneButton")
        self.gridLayout_29.addWidget(self.oneButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_14, 1, 1, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.panel)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.fourButton = QtWidgets.QPushButton(self.frame_11)
        self.fourButton.setMaximumSize(QtCore.QSize(78, 71))
        self.fourButton.setObjectName("fourButton")
        self.gridLayout_26.addWidget(self.fourButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_11, 2, 1, 1, 1)
        self.frame_26 = QtWidgets.QFrame(self.panel)
        self.frame_26.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_26.setObjectName("frame_26")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.frame_26)
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.threeButton = QtWidgets.QPushButton(self.frame_26)
        self.threeButton.setMaximumSize(QtCore.QSize(78, 71))
        self.threeButton.setObjectName("threeButton")
        self.gridLayout_41.addWidget(self.threeButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_26, 1, 3, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.panel)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plusButton = QtWidgets.QPushButton(self.frame_7)
        self.plusButton.setMaximumSize(QtCore.QSize(78, 71))
        self.plusButton.setObjectName("plusButton")
        self.gridLayout_4.addWidget(self.plusButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_7, 4, 0, 1, 1)
        self.frame_25 = QtWidgets.QFrame(self.panel)
        self.frame_25.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_25.setObjectName("frame_25")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.frame_25)
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_40.setSpacing(0)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.nineButton = QtWidgets.QPushButton(self.frame_25)
        self.nineButton.setMaximumSize(QtCore.QSize(78, 71))
        self.nineButton.setObjectName("nineButton")
        self.gridLayout_40.addWidget(self.nineButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_25, 3, 3, 1, 1)
        self.frame_20 = QtWidgets.QFrame(self.panel)
        self.frame_20.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.twoButton = QtWidgets.QPushButton(self.frame_20)
        self.twoButton.setMaximumSize(QtCore.QSize(78, 71))
        self.twoButton.setObjectName("twoButton")
        self.gridLayout_35.addWidget(self.twoButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_20, 1, 2, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.panel)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.sevenButton = QtWidgets.QPushButton(self.frame_13)
        self.sevenButton.setMaximumSize(QtCore.QSize(78, 71))
        self.sevenButton.setObjectName("sevenButton")
        self.gridLayout_28.addWidget(self.sevenButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_13, 3, 1, 1, 1)
        self.frame_23 = QtWidgets.QFrame(self.panel)
        self.frame_23.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_23.setObjectName("frame_23")
        self.gridLayout_38 = QtWidgets.QGridLayout(self.frame_23)
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_38.setSpacing(0)
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.sixButton = QtWidgets.QPushButton(self.frame_23)
        self.sixButton.setMaximumSize(QtCore.QSize(78, 71))
        self.sixButton.setObjectName("sixButton")
        self.gridLayout_38.addWidget(self.sixButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_23, 2, 3, 1, 1)
        self.frame_18 = QtWidgets.QFrame(self.panel)
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.cButton = QtWidgets.QPushButton(self.frame_18)
        self.cButton.setMaximumSize(QtCore.QSize(78, 71))
        self.cButton.setObjectName("cButton")
        self.gridLayout_33.addWidget(self.cButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_18, 0, 2, 1, 1)
        self.frame_12 = QtWidgets.QFrame(self.panel)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.ceButton = QtWidgets.QPushButton(self.frame_12)
        self.ceButton.setMaximumSize(QtCore.QSize(78, 71))
        self.ceButton.setObjectName("ceButton")
        self.gridLayout_27.addWidget(self.ceButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_12, 0, 1, 1, 1)
        self.frame_19 = QtWidgets.QFrame(self.panel)
        self.frame_19.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_34.setSpacing(0)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.eightButton = QtWidgets.QPushButton(self.frame_19)
        self.eightButton.setMaximumSize(QtCore.QSize(78, 71))
        self.eightButton.setObjectName("eightButton")
        self.gridLayout_34.addWidget(self.eightButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_19, 3, 2, 1, 1)
        self.frame_21 = QtWidgets.QFrame(self.panel)
        self.frame_21.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_36 = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_36.setSpacing(0)
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.zeroButton = QtWidgets.QPushButton(self.frame_21)
        self.zeroButton.setMaximumSize(QtCore.QSize(78, 71))
        self.zeroButton.setObjectName("zeroButton")
        self.gridLayout_36.addWidget(self.zeroButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_21, 4, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.panel)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.percentButton = QtWidgets.QPushButton(self.frame)
        self.percentButton.setMinimumSize(QtCore.QSize(78, 71))
        self.percentButton.setObjectName("percentButton")
        self.gridLayout.addWidget(self.percentButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_27 = QtWidgets.QFrame(self.panel)
        self.frame_27.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_27.setObjectName("frame_27")
        self.gridLayout_42 = QtWidgets.QGridLayout(self.frame_27)
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_42.setSpacing(0)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.equalButton = QtWidgets.QPushButton(self.frame_27)
        self.equalButton.setMaximumSize(QtCore.QSize(78, 71))
        self.equalButton.setObjectName("equalButton")
        self.gridLayout_42.addWidget(self.equalButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_27, 4, 3, 1, 1)
        self.frame_17 = QtWidgets.QFrame(self.panel)
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.fiveButton = QtWidgets.QPushButton(self.frame_17)
        self.fiveButton.setMaximumSize(QtCore.QSize(78, 71))
        self.fiveButton.setObjectName("fiveButton")
        self.gridLayout_32.addWidget(self.fiveButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_17, 2, 2, 1, 1)
        self.frame_24 = QtWidgets.QFrame(self.panel)
        self.frame_24.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_24.setObjectName("frame_24")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.frame_24)
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_39.setSpacing(0)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.backspaceButton = QtWidgets.QPushButton(self.frame_24)
        self.backspaceButton.setMaximumSize(QtCore.QSize(78, 71))
        self.backspaceButton.setObjectName("backspaceButton")
        self.gridLayout_39.addWidget(self.backspaceButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_24, 0, 3, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.panel)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.minusButton = QtWidgets.QPushButton(self.frame_9)
        self.minusButton.setMaximumSize(QtCore.QSize(78, 71))
        self.minusButton.setObjectName("minusButton")
        self.gridLayout_6.addWidget(self.minusButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_9, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.panel)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.divideButton = QtWidgets.QPushButton(self.frame_2)
        self.divideButton.setMaximumSize(QtCore.QSize(78, 71))
        self.divideButton.setObjectName("divideButton")
        self.gridLayout_2.addWidget(self.divideButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame_15 = QtWidgets.QFrame(self.panel)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.commaButton = QtWidgets.QPushButton(self.frame_15)
        self.commaButton.setMaximumSize(QtCore.QSize(78, 71))
        self.commaButton.setObjectName("commaButton")
        self.gridLayout_30.addWidget(self.commaButton, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.frame_15, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.panel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cButton, self.oneButton)
        MainWindow.setTabOrder(self.oneButton, self.twoButton)
        MainWindow.setTabOrder(self.twoButton, self.threeButton)
        MainWindow.setTabOrder(self.threeButton, self.fourButton)
        MainWindow.setTabOrder(self.fourButton, self.fiveButton)
        MainWindow.setTabOrder(self.fiveButton, self.sixButton)
        MainWindow.setTabOrder(self.sixButton, self.sevenButton)
        MainWindow.setTabOrder(self.sevenButton, self.eightButton)
        MainWindow.setTabOrder(self.eightButton, self.nineButton)
        MainWindow.setTabOrder(self.nineButton, self.zeroButton)
        MainWindow.setTabOrder(self.zeroButton, self.equalButton)
        MainWindow.setTabOrder(self.equalButton, self.backspaceButton)
        MainWindow.setTabOrder(self.backspaceButton, self.ceButton)
        MainWindow.setTabOrder(self.ceButton, self.percentButton)
        MainWindow.setTabOrder(self.percentButton, self.divideButton)
        MainWindow.setTabOrder(self.divideButton, self.multiplyButton)
        MainWindow.setTabOrder(self.multiplyButton, self.minusButton)
        MainWindow.setTabOrder(self.minusButton, self.plusButton)
        MainWindow.setTabOrder(self.plusButton, self.commaButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.multiplyButton.setText(_translate("MainWindow", "*"))
        self.multiplyButton.setShortcut(_translate("MainWindow", "*, *"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.oneButton.setShortcut(_translate("MainWindow", "1"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fourButton.setShortcut(_translate("MainWindow", "4"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.threeButton.setShortcut(_translate("MainWindow", "3"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.plusButton.setShortcut(_translate("MainWindow", "Ctrl+Shift+4, +"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.nineButton.setShortcut(_translate("MainWindow", "9"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.twoButton.setShortcut(_translate("MainWindow", "2"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.sevenButton.setShortcut(_translate("MainWindow", "7"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.sixButton.setShortcut(_translate("MainWindow", "6"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.cButton.setShortcut(_translate("MainWindow", "Space"))
        self.ceButton.setText(_translate("MainWindow", "CE"))
        self.ceButton.setShortcut(_translate("MainWindow", "Esc"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.eightButton.setShortcut(_translate("MainWindow", "8"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.zeroButton.setShortcut(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.percentButton.setShortcut(_translate("MainWindow", "Ctrl+Shift+5"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.equalButton.setShortcut(_translate("MainWindow", "Return, Enter"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.fiveButton.setShortcut(_translate("MainWindow", "5"))
        self.backspaceButton.setText(_translate("MainWindow", "⇚"))
        self.backspaceButton.setShortcut(_translate("MainWindow", "Backspace"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.minusButton.setShortcut(_translate("MainWindow", "-, -"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.divideButton.setShortcut(_translate("MainWindow", "Ctrl+Shift+7, /"))
        self.commaButton.setText(_translate("MainWindow", ","))
        self.commaButton.setShortcut(_translate("MainWindow", ",, ,"))