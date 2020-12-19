import os
import pyqrcode 

os.chdir(os.path.dirname(__file__))

code = open('codeOfWhatsApp.txt').read()
code = code.split('data-ref="')[1]
code = code.split('"><span>')[0]
print(code)
code = pyqrcode.create(code) 
code.show() 
