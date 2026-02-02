import xml.etree.ElementTree as ET
datasamp='''<?xml version="1.0" encoding="UTF-8"?>
<employee>
<name>prasanth</name>
<mail abc="mail@gb.com"/>
</employee>'''
xmldata=ET.fromstring(datasamp)
print('NAME:',xmldata.find('name').text)
print('COUNTRY:',xmldata.find('mail').get('abc'))


import urllib.request

url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
xml = '''<root>
    <data><count>5</count></data>
    <item><sub><nn><count>10</count></nn></sub></item>
    <count>1</count>
</root>'''
tree = ET.fromstring(xml)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    nums.append(result.text)
print(nums)
print('Count:', len(nums))
#print('Sum:', sum(int(nums)))