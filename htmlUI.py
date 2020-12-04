from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QStatusBar, QApplication, QMainWindow
import sys 

windowName, url = 'IE', 'https://www.google.com/'

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