import random
from myModules import browser
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

Username_Default = 'B/16467'
Password_Default = 'As23422866'

Username = input('\nUsername: ')
Password = input('Password: ')

Username = Username.lower()
Password = Password.lower()

if Username and Password == 'default' or Username and Password == 'd':
    Username = Username_Default
    Password = Password_Default

browser = browser.Chrome()
pyautogui.moveTo(1565, 97)
pyautogui.click()
pyautogui.moveTo(random.randint(0, 1000), random.randint(0, 1000))
browser.get('https://entrar.in/login/login')

username = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
username.send_keys(Username)

password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
password.send_keys(Password)

sign_in_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(.,\'Log-In with Entrar\')]')))
sign_in_button.click()

browser.execute_script('alert(\'Close Any Popups  Time: 10 Seconds\')')
time.sleep(10)

online_classroom = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id=\'mCSB_1_container\']/ul/li[8]/a/span/img')))
online_classroom.click()

search_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'filter')))

def search():
    Repeat = True
    while Repeat:
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//table[@id=\'basic-btn\']/tbody/tr/td[4]/a'))).click()
            Repeat = False
        except:
            search_button.click()

def end():
    Repeat = True
    while Repeat:
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'button--Z2dosza md--Q7ug4 primary--1IbqAO button--Z1j2w3P'))).click()
            close = browser.find_element_by_tag_name('body')
            close.send_keys(Keys.CONTROL + 'w')
            break
        except:
            pass

while True:
    search()
    end()