import time
import tkinter
from myModules import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tkinter import messagebox

tkinter.Tk().withdraw()

options = Options()
options.add_argument('use-fake-ui-for-media-stream')
options.add_argument('--headless')
browser = browser.Chrome(options=options)
browser.get("https://www.aha-music.com/")
time.sleep(5)
messagebox.showinfo('Recording', 'Click This When You Would Like To Recognize The Song')
browser.find_element(By.XPATH, "//div[@id='__layout']/div/div/div[2]/div/button").click()
messagebox.showinfo('Recording', 'Click This When Your Done Recording')
print(browser.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div[1]/div/div[1]").text)
browser.close()
