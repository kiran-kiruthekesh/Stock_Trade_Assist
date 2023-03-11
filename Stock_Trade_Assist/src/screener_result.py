
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_screenerResultWindow(object):
    def setupUi(self, screenerResultWindow, selectorWindow):
        screenerResultWindow.setObjectName("screenerResultWindow")
        screenerResultWindow.resize(570, 410)
        screenerResultWindow.setStyleSheet("QWidget {\n"
"    background-color: #17181c;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(screenerResultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resultComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.resultComboBox.setGeometry(QtCore.QRect(100, 120, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resultComboBox.setFont(font)
        self.resultComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resultComboBox.setMouseTracking(False)
        self.resultComboBox.setAutoFillBackground(False)
        self.resultComboBox.setStyleSheet("QComboBox {\n"
"    background-color: #17181c ; \n"
"    border-radius: 5px;\n"
"   color : rgb(0, 199, 199);\n"
"    border: 3px solid rgb(0, 199, 199);\n"
"}\n"
"QListView {\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border: 3px solid rgb(0, 199, 199);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.resultComboBox.setMaxVisibleItems(5)
        self.resultComboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.resultComboBox.setDuplicatesEnabled(False)
        self.resultComboBox.setFrame(True)
        self.resultComboBox.setObjectName("resultComboBox")
        self.canBuyButton = QtWidgets.QPushButton(self.centralwidget)
        self.canBuyButton.setGeometry(QtCore.QRect(210, 270, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.canBuyButton.setFont(font)
        self.canBuyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.canBuyButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255) ; \n"
"    border-radius: 15px;\n"
"    border: 3px solid #4CAF50;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #4CAF50; \n"
"  color: white;\n"
"  border: 3px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.canBuyButton.setObjectName("canBuyButton")
        self.selectAllCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.selectAllCheckBox.setGeometry(QtCore.QRect(220, 200, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectAllCheckBox.setFont(font)
        self.selectAllCheckBox.setStyleSheet("QCheckBox {\n"
"    background-color: #17181c ; \n"
"   color : rgb(0, 199, 199);\n"
"}")
        self.selectAllCheckBox.setTristate(False)
        self.selectAllCheckBox.setObjectName("selectAllCheckBox")

        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.go_back(selectorWindow, screenerResultWindow))
        self.backButton.setGeometry(QtCore.QRect(30, 20, 31, 31))
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
"}\n"
"\n"
"\n"
"\n"
"")
        self.backButton.setObjectName("backButton")
        screenerResultWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(screenerResultWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 22))
        self.menubar.setObjectName("menubar")
        screenerResultWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(screenerResultWindow)
        self.statusbar.setObjectName("statusbar")
        screenerResultWindow.setStatusBar(self.statusbar)

        self.retranslateUi(screenerResultWindow)
        QtCore.QMetaObject.connectSlotsByName(screenerResultWindow)

    def go_back(self, screener_w, result_w):
        screener_w.show()
        result_w.hide()

    def retranslateUi(self, screenerResultWindow):
        _translate = QtCore.QCoreApplication.translate
        screenerResultWindow.setWindowTitle(_translate("screenerResultWindow", "MainWindow"))
        self.canBuyButton.setText(_translate("screenerResultWindow", "BUY ?"))
        self.selectAllCheckBox.setText(_translate("screenerResultWindow", "  select  all"))
        self.backButton.setText(_translate("screenerResultWindow", "<<"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screenerResultWindow = QtWidgets.QMainWindow()
    ui = Ui_screenerResultWindow()
    ui.setupUi(screenerResultWindow)
    screenerResultWindow.show()
    sys.exit(app.exec_())
