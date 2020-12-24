import requests
from bs4 import BeautifulSoup

def _get_soup_object(url, parser="html.parser"):
    return BeautifulSoup(requests.get(url).text, parser)

data = _get_soup_object("https://www.synonym.com/")
section = data.find('div', {'class': 'root'})
spans = section.findAll('a')
spans = str(spans[0])
spans = spans[28:]
print(spans.split('href')[0].replace('\"', ''))
