import requests
import base64
import os

os.chdir(os.path.dirname(__file__))
fname = 'bookpage.jpg'

with open(fname, 'rb') as img_file:
    my_string = base64.b64encode(img_file.read())

print(requests.post('http://dc88a549dfb6.ngrok.io/image', my_string).text)
