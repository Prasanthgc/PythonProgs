import json
c=[]
data= '''
[{
  "name": "Prasanth",
  "country": { "local": "INDIA",
               "Foreign":"Netherlands"
               }},
               { "name": "drn",
  "country": { "local": "cc",
               "Foreign":"e"
               }
}]
'''
loaded=json.loads(data)
for item in loaded:
    c.append(item['name'])
    print('name:',item['name'])
    print('country:',item['country'] ['local'])
print(c)