import requests
import json
def login_id():
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
    return x['icSessionId']
#<--Hey--> Program starts here <---Hey--->
#For fetching the Mapping task details  - only one
'''Task_Id=input("input your task id:")
# f-prefix enables variable substitution
url = f"https://usw1.dmr-us.informaticacloud.com/saas/api/v2/mttask/{Task_Id}"
headers = {
        "icSessionId": login_id(),
        "Accept": "application/json"
}

response = requests.request("GET", url, headers=headers)
mtt=response.json()
print('sessionname:',mtt['name'])
print('params:',mtt['sessionProperties']["Pushdown Optimization"] )'''
#For multiple sessions
while True:
    Task_Id=input("input your task id:")
    if len(Task_Id) < 1:
        print("invalid task id")
        break
    # f-prefix enables variable substitution
    url = f"https://usw1.dmr-us.informaticacloud.com/saas/api/v2/mttask/{Task_Id}"
    headers = {
        "icSessionId": login_id(),
        "Accept": "application/json"
    }

    response = requests.request("GET", url, headers=headers)
    mtt=response.json()
    print('sessionname:',mtt['name'])
    print('params:',mtt['sessionProperties']["Pushdown Optimization"] )



