from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

path = 'C:/Users/Anirudh/AppData/Local/Programs/Python/Python38/Lib/site-packages/myModules/browser/chromedriver.exe'
query = input('Text: ')
chromeOptions = Options()
chromeOptions.headless = True
browser = webdriver.Chrome(executable_path=path, options=chromeOptions)
browser.get('https://huggingface.co/gpt2?text={}'.format(query))
time.sleep(5)
elem = browser.find_element_by_class_name('output-panel')
print(elem.text)