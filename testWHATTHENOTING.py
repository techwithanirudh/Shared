import time
from myModules import browser

browser = browser.Chrome()
browser.get('https://web.whatsapp.com/')
time.sleep(3)
element = browser.find_element_by_class_name('_3l6Cf')
code = element.get_attribute('innerHTML')
