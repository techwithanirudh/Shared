# https://www.youtube.com/watch?v=OsKQw3qTMMk

import os
from myModules import browser
from selenium.webdriver.firefox.options import Options
import time
from email.message import EmailMessage
import smtplib
import imghdr

# from selenium import webdriver

# def Firefox(options=None):
#     browser = webdriver.Firefox(executable_path='{}/geckodriver.exe'.format(os.path.dirname(__file__)), options=options)
#     browser.maximize_window()
#     return browser

_from = ''
pwd = ''
to = ''

os.chdir(os.path.dirname(__file__))
open('titles.txt', 'a').close()

def send_email(receiver, subject, message, img_data=None):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(_from, pwd)
    email = EmailMessage()
    email['From'] = _from
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    if img_data != None:
        email.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data))
    server.send_message(email)

def post_to_twitter():
    pass

def download_thumbnail(thumbnail_url, fname='thumbnail_youtube.png'):
    time.sleep(10)
    browser.get(thumbnail_url)
    open(fname, 'a')
    browser.save_screenshot(fname)
    return fname

options = Options()
options.add_argument('--headless')
browser = browser.Firefox(options)
url = 'https://www.youtube.com/channel/UCmse86kaxJ3n1dDT_bXDukg'
mins = 10

while True:
    browser.get(url)
    video = browser.find_element_by_xpath('//*[@id=\'video-title\']')
    video_title = str(video.text)

    F = open('titles.txt', 'r')
    past_title = F.readline()
    F.close()

    if past_title == video_title:
        print('Don\'t Post to twitter')
    else:
        video.click()
        video_url = str(browser.current_url)
        id = video_url.split('=', 1)[1]
        browser.get('https://www.youtube.com/')
        thumbnail_url = 'https:///img.youtube.com/vi/' + id + '/maxresdefault.jpg'
        image_path = download_thumbnail(thumbnail_url)
        img_file = 'thumbnail_youtube.png'
        with open(img_file, 'rb') as f:
            img_data = f.read()
        send_email(to, 'Youtube', 'This is the thumbnail and title of your new video', img_data)
        F = open('titles.txt', 'w')
        F.write(video_title)
        F.close()

    time.sleep(60 * mins)
