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

from flask import Flask, redirect, url_for, render_template, request
import os

os.system('start D:\Anirudh\pythonprojects\sampleproject1\localhostApp.bat')

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

if __name__ == "__main__":
    app.run(debug=True)
