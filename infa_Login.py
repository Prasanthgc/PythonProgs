import requests
import json

url="https://dmr-us.informaticacloud.com/ma/api/v2/user/login"
#content in RAW section of postman use below as dictionary
payload= {
"@type": "login",
"username": "pcinthamani_preview",
"password": "Komali@1234"
}
#Headers section - you can add as below like a dictionary
headers = {"Content-Type": "application/json", "Accept": "application/json"}
session = requests.Session() #to keep session alive so no need to call API put many times
response = session.request("POST", url, headers=headers, json=payload)
x=response.json() #converting response to json internally its json.loads() to dict/list/tuple
print(x)
print("sessionId:", x['icSessionId'])
print("sessionId:", x.get('icSessionId'))



