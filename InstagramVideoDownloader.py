from myModules import browser as webdriver
import requests
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import filetype

driver = webdriver.Firefox()
url = input('Url: ')
filename = 'instaDnld.tmp'
img = False

driver.get(url)

try:
    src = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'FFVAD'))).get_attribute('src')
    print(src)
    img = True
except:
    src = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tWeCl'))).get_attribute('src')
    print(src)

r = requests.get(src, stream=True)

if img:
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
else:
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)

kind = filetype.guess(filename)

if kind != None:
    fname = filename.replace('.tmp', kind.extension)
    shutil.copyfile(filename, fname)
    print('Downloaded')
else:
    print('Error')

driver.close()
