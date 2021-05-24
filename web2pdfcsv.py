import pdfkit
import csv
import re

with open('web.csv') as canvasPage:
    

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

titleNumber = 0

for i in webURL:
    titleNumber+=1
    pdfkit.from_url(i, 'title'+str(titleNumber)+'.pdf')