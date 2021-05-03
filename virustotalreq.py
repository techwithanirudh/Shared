from urllib.parse import quote_plus

url = quote_plus('https://stackoverflow.com/')
url = url.replace('%2F', '%252F')

if url[5] != 's':
    url = url.replace('http%3A', 'http%253A')
else:
    url = url.replace('https%3A', 'https%253A')

url = 'https://www.virustotal.com/gui/search/' + url

print(url)
