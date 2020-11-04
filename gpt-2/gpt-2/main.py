from PyQt5 import QtCore, QtWidgets
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

class Ui_MainWindow(object):
    def btnCompute_clicked(self):
        path = 'C:/Users/Anirudh/AppData/Local/Programs/Python/Python38/Lib/site-packages/myModules/browser/chromedriver.exe'
        query = self.txtSent.toPlainText().replace('\n', '')
        if query != '/[set-val]/':
            chromeOptions = Options()
            chromeOptions.headless = True
            browser = webdriver.Chrome(executable_path=path, options=chromeOptions)
            browser.get('https://huggingface.co/gpt2?text={}'.format(query))
            time.sleep(self.sleepT)
            elem = browser.find_element_by_class_name('output-panel')
            self.bsrGenText.setText(self._translate('MainWindow', elem.text))
        else:
            while True:
                number, ok = QtWidgets.QInputDialog().getText(None, 'Delay',
                                         'Sleep:', QtWidgets.QLineEdit.Normal,
                                        str(self.sleepT))
                if ok and number:
                    try:
                        self.sleepT = int(number)
                        if self.sleepT > 0 and self.sleepT < 50:
                            break
                    except ValueError:
                        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(437, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.lblSent = QtWidgets.QLabel(self.centralwidget)
        self.lblSent.setGeometry(QtCore.QRect(10, 0, 81, 16))
        self.lblSent.setObjectName('lblSent')
        self.txtSent = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSent.setGeometry(QtCore.QRect(90, 0, 261, 101))
        self.txtSent.setObjectName('txtSent')
        self.btnCompute = QtWidgets.QPushButton(self.centralwidget)
        self.btnCompute.setGeometry(QtCore.QRect(360, 40, 75, 23))
        self.btnCompute.setObjectName('btnCompute')
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 331, 194))
        self.layoutWidget.setObjectName('layoutWidget')
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.bsrGenText = QtWidgets.QTextBrowser(self.layoutWidget)
        self.bsrGenText.setObjectName('bsrGenText')
        self.horizontalLayout.addWidget(self.bsrGenText)
        self.lblGenText = QtWidgets.QLabel(self.layoutWidget)
        self.lblGenText.setObjectName('lblGenText')
        self.horizontalLayout.addWidget(self.lblGenText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 21))
        self.menubar.setObjectName('menubar')
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.sleepT = 5
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate('MainWindow', 'GPT2 Playground'))
        self.lblSent.setText(self._translate('MainWindow', 'Your Sentence: '))
        self.btnCompute.setText(self._translate('MainWindow', 'Compute'))
        self.lblGenText.setText(self._translate('MainWindow', 'GenratedText'))
        self.btnCompute.clicked.connect(self.btnCompute_clicked)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())