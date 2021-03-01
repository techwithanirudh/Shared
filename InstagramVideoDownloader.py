from myModules import browser as webdriver
import requests
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import filetype
import os

os.chdir(os.path.dirname(__file__))

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
url = input('Url: ')
filename = 'instaDnld.tmp'
img = bool(input('Is this url for an image or not? (Y/N): '))

driver.get(url)

if img == 'Y':
    src = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'FFVAD'))).get_attribute('src')
    print(src)
else:
    src = WebDriverWait(driver, 20).until(
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
    fname = filename.replace('tmp', kind.extension)
    shutil.copyfile(filename, fname)
    os.system(f'start {fname}')
    print('Downloaded')
else:
    print('Error')

driver.close()
