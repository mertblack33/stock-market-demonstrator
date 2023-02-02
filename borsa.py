import sys
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 249)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons8-coins-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#centralwidget{\n"
"border-image: url(:/Arka plan/BistKYDKarsilama.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget.setStyleSheet("#\n"
"background-image: url(:/Arkaplan/DijitalVarlık_Görsel_2.jpg);")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 91, 81))
        self.widget.setStyleSheet("border-image: url(:/dolar/3211282.png);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(150, 10, 91, 81))
        self.widget_2.setStyleSheet("border-image: url(:/dolar/dollar-sign-icon-png-22.png);")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(280, 10, 81, 81))
        self.widget_3.setStyleSheet("border-image: url(:/dolar/Euro-Symbol-PNG-Clipart.png);")
        self.widget_3.setObjectName("widget_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 140, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton{\n"
"    color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 90, 351, 71))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Borsa Programı"))
        self.pushButton.setText(_translate("MainWindow", "Güncelle"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "0"))

    def borsa(self):
        dolar = []
        euro = []
        btc = []
        url = "https://bigpara.hurriyet.com.tr/doviz/dolar/"
        mert = requests.get(url)
        sayfa_içerigi = mert.content
        soup = BeautifulSoup(sayfa_içerigi, "html.parser")
        for e in soup.find_all("span", {"class": "value up"}):
            dolar.append(e.text)
        url1 = "https://bigpara.hurriyet.com.tr/doviz/euro/"
        mert1 = requests.get(url1)
        sayfa_içerigi1 = mert1.content
        soup = BeautifulSoup(sayfa_içerigi1, "html.parser")
        for a in soup.find_all("span", {"class": "value up"}):
            euro.append(a.text)
        url2 = "https://coinmarketcap.com/tr/currencies/bitcoin/"
        mert2 = requests.get(url2)
        sayfa_içerigi2 = mert2.content
        soup = BeautifulSoup(sayfa_içerigi2, "html.parser")
        for w in soup.find_all("div", {"priceValue smallerPrice"}):
            btc.append(w.text)
        euro1 = str(euro[0])
        btc1 = str(btc).strip("[]',₺")
        dolar1 = str(dolar[0])
        self.label.setText(euro1)
        self.label_2.setText(dolar1)
        self.label_3.setText(btc1)
import dosya_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(pencere)
    ui.pushButton.clicked.connect(ui.borsa)
    pencere.show()
    sys.exit(app.exec_())