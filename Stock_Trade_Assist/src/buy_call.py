
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_callGenerationWindow(object):
    def setupUi(self, callGenerationWindow, MainWindow, selectorWindow):
        callGenerationWindow.setObjectName("callGenerationWindow")
        callGenerationWindow.resize(570, 410)
        callGenerationWindow.setStyleSheet("QWidget {\n"
"    background-color: #17181c;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(callGenerationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.targetLabel = QtWidgets.QLabel(self.centralwidget)
        self.targetLabel.setGeometry(QtCore.QRect(100, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.targetLabel.setFont(font)
        self.targetLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.targetLabel.setStyleSheet("QLabel {\n"
"    color: rgb(0, 255, 255);\n"
"    \n"
"}")
        self.targetLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.targetLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.targetLabel.setLineWidth(1)
        self.targetLabel.setTextFormat(QtCore.Qt.AutoText)
        self.targetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.targetLabel.setObjectName("targetLabel")

        self.displayTargetLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayTargetLabel.setGeometry(QtCore.QRect(250, 170, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.displayTargetLabel.setFont(font)
        self.displayTargetLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displayTargetLabel.setStyleSheet("QLabel {\n"
"    color: rgb(0, 255, 255);\n"
"    \n"
"}")
        self.displayTargetLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.displayTargetLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.displayTargetLabel.setLineWidth(1)
        self.displayTargetLabel.setText("")
        self.displayTargetLabel.setTextFormat(QtCore.Qt.AutoText)
        self.displayTargetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayTargetLabel.setObjectName("displayTargetLabel")

        self.stopLossLabel = QtWidgets.QLabel(self.centralwidget)
        self.stopLossLabel.setGeometry(QtCore.QRect(100, 250, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stopLossLabel.setFont(font)
        self.stopLossLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stopLossLabel.setStyleSheet("QLabel {\n"
"    color: rgb(0, 255, 255);\n"
"    \n"
"}")
        self.stopLossLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.stopLossLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stopLossLabel.setLineWidth(1)
        self.stopLossLabel.setTextFormat(QtCore.Qt.AutoText)
        self.stopLossLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stopLossLabel.setObjectName("stopLossLabel")

        self.displayStopLossLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayStopLossLabel.setGeometry(QtCore.QRect(250, 250, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.displayStopLossLabel.setFont(font)
        self.displayStopLossLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displayStopLossLabel.setStyleSheet("QLabel {\n"
"    color: rgb(0, 255, 255);\n"
"    \n"
"}")
        self.displayStopLossLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.displayStopLossLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.displayStopLossLabel.setLineWidth(1)
        self.displayStopLossLabel.setText("")
        self.displayStopLossLabel.setTextFormat(QtCore.Qt.AutoText)
        self.displayStopLossLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayStopLossLabel.setObjectName("displayStopLossLabel")

        self.callLabel = QtWidgets.QLabel(self.centralwidget)
        self.callLabel.setGeometry(QtCore.QRect(100, 90, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.callLabel.setFont(font)
        self.callLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.callLabel.setStyleSheet("QLabel {\n"
"    color: #4CAF50;\n"
"    \n"
"}")
        self.callLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.callLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.callLabel.setLineWidth(1)
        self.callLabel.setText("")
        self.callLabel.setTextFormat(QtCore.Qt.AutoText)
        self.callLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.callLabel.setObjectName("callLabel")

        self.prevPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevPushButton.setGeometry(QtCore.QRect(40, 320, 31, 31))
        self.prevPushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255) ; \n"
"    border-radius: 15px;\n"
"    border: 3px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: rgb(255, 0, 0) ; \n"
"    color: rgb(255, 0, 0);\n"
"  color: white;\n"
"  border: 3px solid rgb(255, 255, 255);\n"
"}")
        self.prevPushButton.setObjectName("prevPushButton")

        self.nextPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextPushButton.setGeometry(QtCore.QRect(500, 320, 31, 31))
        self.nextPushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255) ; \n"
"    border-radius: 15px;\n"
"    border: 3px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #7CFF01 ; \n"
"    color: rgb(255, 0, 0);\n"
"  color: white;\n"
"  border: 3px solid rgb(255, 255, 255);\n"
"}")
        self.nextPushButton.setObjectName("nextPushButton")

        self.homePushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.go_to_main_menu(MainWindow, callGenerationWindow))
        self.homePushButton.setGeometry(QtCore.QRect(500, 20, 31, 31))
        self.homePushButton.setStyleSheet("QPushButton {\n"
                                          "    background-color: #17181c rgb(255, 255, 255) ;\n"
                                          "    color: rgb(255,255,255);  \n"
                                          "    border-radius: 15px;\n"
                                          "    border: 3px solid rgb(255, 255, 255);\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "  background-color: #7CFF01 ; \n"
                                          "    color: rgb(255, 0, 0);\n"
                                          "  color: white;\n"
                                          "  border: 3px solid rgb(255, 255, 255);\n"
                                          "}")
        self.homePushButton.setObjectName("homePushButton")

        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.go_back(selectorWindow, callGenerationWindow))
        self.backButton.setGeometry(QtCore.QRect(40, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backButton.setFont(font)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(255, 255, 255) ; \n"
                                      "    border-radius: 15px;\n"
                                      "    border: 3px solid rgb(255, 0, 0);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "  background-color: rgb(255, 0, 0) ; \n"
                                      "    color: rgb(255, 0, 0);\n"
                                      "  color: white;\n"
                                      "  border: 3px solid rgb(255, 255, 255);\n"
                                      "}")
        self.backButton.setObjectName("backButton")

        callGenerationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(callGenerationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 22))
        self.menubar.setObjectName("menubar")
        callGenerationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(callGenerationWindow)
        self.statusbar.setObjectName("statusbar")
        callGenerationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(callGenerationWindow)
        QtCore.QMetaObject.connectSlotsByName(callGenerationWindow)

    def go_back(self, screener_w, call_w):
        screener_w.show()
        call_w.hide()

    def go_to_main_menu(self, main_w, call_w):
        main_w.show()
        call_w.hide()

    def retranslateUi(self, callGenerationWindow):
        _translate = QtCore.QCoreApplication.translate
        callGenerationWindow.setWindowTitle(_translate("callGenerationWindow", "MainWindow"))
        self.targetLabel.setText(_translate("callGenerationWindow", "TARGET"))
        self.stopLossLabel.setText(_translate("callGenerationWindow", "STOP LOSS"))
        self.prevPushButton.setText(_translate("callGenerationWindow", "<"))
        self.nextPushButton.setText(_translate("callGenerationWindow", ">"))
        self.homePushButton.setText(_translate("callGenerationWindow", "^"))
        self.backButton.setText(_translate("callGenerationWindow", "<<"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    callGenerationWindow = QtWidgets.QMainWindow()
    ui = Ui_callGenerationWindow()
    ui.setupUi(callGenerationWindow)
    callGenerationWindow.show()
    sys.exit(app.exec_())
