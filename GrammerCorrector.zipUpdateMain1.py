# RUN THIS ON COLAB

'''# !sudo apt install openjdk-8-jdk
# !sudo update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
# !pip install language-check
# !pip install pycontractions
!pip install flask_ngrok

import language_check 
from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)
tool = language_check.LanguageTool('en-US') 

@app.route('/api/req/<sentence>')
def apiReq(sentence):
  sentence = sentence.replace('-', ' ')
  matches = tool.check(sentence) 
  mistakes = ''
  print(sentence)
  for mistake in matches: 
    mistake = str(mistake)
    mistake = mistake.split('Message: ')[1]
    print(mistake)
    if '^' in mistake:
      mistakes += '\n'  
    mistakes += mistake
  return mistakes

if __name__ == '__main__':
  app.run()'''

from PyQt5 import QtCore, QtWidgets
import requests

class Ui_MainWindow(object):
    def btnCheck_clicked(self):
        self.text = self.txtSentence.toPlainText().replace(' ', '-')
        # TODO-Fake: The id should be changed by seeing colab You should copy id from url and paste
        self.id = '3e986e04abe1'
        if self.text.replace('\n', '').replace('-', '') != '':
            res = requests.get(f'https://{self.id}.ngrok.io/api/req/{self.text}').text
            print(res)
            if res != '':
                self.lblShowgrammatical_rules.setStyleSheet('background-color: red')
            else:
                res = self.text
                self.lblShowgrammatical_rules.setStyleSheet('background-color: green')

            self.lblShowgrammatical_rules.setText(_translate('MainWindow', res))
            self.lblShowSuggestion.setText(_translate('MainWindow', res))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(800, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.lblHelpText = QtWidgets.QLabel(self.centralwidget)
        self.lblHelpText.setGeometry(QtCore.QRect(6, 10, 141, 21))
        self.lblHelpText.setObjectName('lblHelpText')
        self.lblSentence = QtWidgets.QLabel(self.centralwidget)
        self.lblSentence.setGeometry(QtCore.QRect(30, 60, 161, 21))
        self.lblSentence.setObjectName('lblSentence')
        self.txtSentence = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSentence.setGeometry(QtCore.QRect(70, 100, 431, 61))
        self.txtSentence.setObjectName('txtSentence')
        self.btnCheck = QtWidgets.QPushButton(self.centralwidget)
        self.btnCheck.setGeometry(QtCore.QRect(240, 180, 81, 31))
        self.btnCheck.setObjectName('btnCheck')
        self.lblSuggestion = QtWidgets.QLabel(self.centralwidget)
        self.lblSuggestion.setGeometry(QtCore.QRect(40, 250, 61, 16))
        self.lblSuggestion.setObjectName('lblSuggestion')
        self.lblShowSuggestion = QtWidgets.QLabel(self.centralwidget)
        self.lblShowSuggestion.setGeometry(QtCore.QRect(10, 270, 781, 141))
        self.lblShowSuggestion.setObjectName('lblShowSuggestion')
        self.lblgrammatical_rules = QtWidgets.QLabel(self.centralwidget)
        self.lblgrammatical_rules.setGeometry(QtCore.QRect(40, 460, 181, 16))
        self.lblgrammatical_rules.setObjectName('lblgrammatical_rules')
        self.lblShowgrammatical_rules = QtWidgets.QLabel('Light green', self.centralwidget)
        self.lblShowgrammatical_rules.setGeometry(QtCore.QRect(10, 480, 781, 161))
        self.lblShowgrammatical_rules.setObjectName('lblShowgrammatical_rules')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName('menubar')
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        global _translate
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'MainWindow'))
        self.lblHelpText.setText(_translate('MainWindow', '?<Put Your Help Text Here>'))
        self.lblSentence.setText(_translate('MainWindow', 'Please type your sentences here:'))
        self.btnCheck.setText(_translate('MainWindow', 'Check'))
        self.btnCheck.clicked.connect(self.btnCheck_clicked)
        self.lblSuggestion.setText(_translate('MainWindow', 'Suggestion:'))
        self.lblShowSuggestion.setText(_translate('MainWindow', 'Label'))
        self.lblgrammatical_rules.setText(_translate('MainWindow', 'The grammatical rules needed to use:'))
        self.lblShowgrammatical_rules.setText(_translate('MainWindow', 'Label'))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
