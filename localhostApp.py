from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QStatusBar, QApplication, QMainWindow
import sys 
import os

os.chdir(os.path.dirname(__file__))

open('running.log', 'a')
file = open('running.log', 'r').read()
if file == '0':
    file = open('running.log', 'w')
    file.write('1')
    # port = sys.argv[-1:][0]
    port = 5000
    windowName, url = 'IE', f'http://localhost:{port}/web/amazon'

    class HtmlFile(QMainWindow):
        def __init__(self, url):
            self.url = url
            if self.url != None:
                super(HtmlFile, self).__init__() 
                qurl = QUrl(self.url) 
                browser = QWebEngineView() 
                browser.setUrl(qurl) 
                self.setCentralWidget(browser) 
                self.status = QStatusBar() 
                self.setStatusBar(self.status) 

    app = QApplication(sys.argv) 
    app.setApplicationName(windowName) 
    window = HtmlFile(url) 
    window.show() 
    app.exec_()
else:
    file = open('running.log', 'w')
    file.write('0')