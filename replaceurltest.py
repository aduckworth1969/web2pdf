import pdfkit
import csv
from bs4 import BeautifulSoup as bs
import lxml
import re

with open('TestLinks.html', 'r') as canvasPage:
    soup = bs(canvasPage, 'lxml')

webURL = []

for a in soup.find_all('a', href=True):
    webURL.append(a['href'])

for a in soup.find_all('iframe', src=True):
    embedURL = 'https:'+a['src']
    webURL.append(embedURL)

r = re.compile('https://docs.google.com/.*')
googleDocs = list(filter(r.match, webURL))

r = re.compile('https://www.youtube.com/.*')
youTube = list(filter(r.match, webURL))

for i in googleDocs:
    webURL.remove(i)

for i in youTube:
    webURL.remove(i)

with open('TestLinks.html', 'r') as testLinks, open('TestLinksReplace.html', 'a') as writeFile:
    testLinksRead = testLinks.read()
    for URL in webURL:
        URLReplace = testLinksRead.replace(URL, URL+'TEST'+'<p cite="'+URL+'">'+URL+'</p>')
        writeFile.write(URLReplace)