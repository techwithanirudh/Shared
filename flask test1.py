# from flask import Flask, redirect, url_for, render_template
# from selenium import webdriver

# app = Flask(__name__)
# browser = webdriver.Chrome(executable_path='D:\Anirudh\pythonprojects\sampleproject1\chromedriver.exe')

# @app.route('/<open_website>')
# def open(open_website):
#     return render_template('index.html', open_website=open_website)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/homepage')
# def goToHome():
# 	return redirect(url_for('home'))

# @app.route('/navbar')
# def navBar():
#     return render_template('base.html')

# if __name__ == '__main__':
#     browser.maximize_window()
#     browser.get('http://localhost:5000/')
#     app.run()

# import os

# os.system('start D:\Anirudh\pythonprojects\sampleproject1\localhostApp.bat')

from flask import Flask, redirect, url_for, render_template, request
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QStatusBar, QApplication, QMainWindow
import sys 
import os
import threading

os.chdir(os.path.dirname(__file__))

start = True
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

def run():
    app = QApplication(sys.argv) 
    app.setApplicationName(windowName) 
    window = HtmlFile(url) 
    window.show() 
    app.exec_()

thread = threading.Thread(target=run)
thread.start()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("getpost.html")

@app.route("/verifylogin", methods=["POST", "GET"])
def verifylogin():
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))

@app.route("/usr/<usr>")
def user(usr):
    return f"<h1>Hello {usr}</h1>"

@app.route('/web/<open_website>')
def open(open_website):
    return render_template('index.html', open_website=open_website)

start = False

if __name__ == "__main__":
    app.run(debug=True)
