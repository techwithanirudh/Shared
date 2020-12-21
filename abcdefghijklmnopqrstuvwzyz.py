import time
from myModules import browser
import pyqrcode 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")  
browser = browser.Firefox(options=options)
browser.get('https://web.whatsapp.com/')
time.sleep(2)
element = browser.find_element_by_class_name('_3l6Cf')
code = element.get_attribute('innerHTML')
code = code.split('data-ref="')[1]
code = code.split('"><span>')[0]
print(code)
code = pyqrcode.create(code) 
code.show() 
time.sleep(10)
wait = WebDriverWait(browser, 600)
target = 'Shalini'
string = "Hurray this worked! Python sent a message!"
x_arg = ' //span[contains(@title, ' + '\"' + target + '\"' + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()
input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
input_box.send_keys(string)
input_box.send_keys(Keys.ENTER)
