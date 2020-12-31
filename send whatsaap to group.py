# import time
# from myModules import browser
# import pyqrcode 
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import os
# os.chdir(os.path.dirname(__file__))
# # from selenium.webdriver.firefox.options import Options

# # options = Options()
# # options.add_argument("--headless")  
# browser = browser.Firefox()
# browser.get('https://web.whatsapp.com/')
# time.sleep(2)
# element = browser.find_element_by_class_name('_3l6Cf')
# code = element.get_attribute('innerHTML')
# code = code.split('data-ref="')[1]
# code = code.split('"><span>')[0]
# print(code)
# code = pyqrcode.create(code) 
# code.show() 
# time.sleep(10)
# with open("testofthepage.txt", "wb") as f:
#     f.write(bytes(browser.page_source, 'utf-8'))
# wait = WebDriverWait(browser, 600)
# target = input('Receiver: ')
# string = input('Message: ')
# x_arg = ' //span[contains(@title, ' + '\"' + target + '\"' + ')]'
# target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
# target.click()
# input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
# input_box.send_keys(string)
# input_box.send_keys(Keys.ENTER)
import time
from sendWhatMessage import sendMessage, init

def sendwhatmsg(message, time_hour, time_min):
    if time_hour not in range(0,25) or time_min not in range(0,60):
        print('Invalid time format')
    
    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600)+(time_min*60)
    
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr * 3600) + (currmin * 60) + (currsec)
    lefttm = callsec - currtotsec

    if lefttm <= 0:
        lefttm = 86400 + lefttm

    time.sleep(lefttm)
    init()
    sendMessage('Kk Kittu', message)

sendwhatmsg('Happy new year', 0, 0)
