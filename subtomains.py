# Subdomains https://gist.github.com/tvldz/5856195
# Code: https://www.youtube.com/watch?v=gbhQrz3Przo

import requests
import os

os.chdir(os.path.dirname(__file__))

domain = 'amazon.com'
file = open('subdomains.txt', 'r')
content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
    url = f'https://{subdomain}.{domain}'
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print('Discovered Subdomain: ', url)