'''import socket
import os
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.testingmcafeesites.com', 80))
cmd = 'GET /testcat_bu.html HTTP/1.0\r\nHost: www.testingmcafeesites.com\r\n\r\n'
mysock.send(cmd.encode())
list_new=[]
while True:
    data = mysock.recv(512)
    #data_decode=data.decode()
    if not data:
        break
    list_new.append(data.decode())
full_text = ''.join(list_new)
#print('data is there:',full_text)

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.testingmcafeesites.com/testcat_bu.html')
for line in fhand:
    print(line.decode() , end=" ")'''

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
#Beautiful Soup: turn HTML into a searchable object so you can cleanly grab exactly the data you need.
# 1. Download the page
response = requests.get(url)
html = response.text

# 2. Create a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")  # or "lxml" if installed [web:277][web:289]
print(soup.prettify())
# 3. Extract data (example: all quote texts)
quotes = soup.select("div.quote span.text")  # CSS selector [web:291]
for q in quotes:
    print(q.get_text())




