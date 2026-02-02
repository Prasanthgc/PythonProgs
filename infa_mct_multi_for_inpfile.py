import requests
import json
import os
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
    print("sessionId:", x['icSessionId'])
    return x['icSessionId']
#<--Hey--> Program starts here <---Hey--->

#010FJ10Z000000002WFH & 0CUMfP4ekeOcyd7BnzCWYb
filename=input("please input the filename:")
#/Users/pcinthamani/Desktop/Partner Team Management/Python_learning/Works/MCTList.txt
if not os.path.exists(filename):
    exit()
if len(filename) < 1:
    print("invalid filename")
    exit()
print("completed block & going to FOR")
sessionid=login_id()
print("calling single icsession id:", sessionid)

readfile=open(filename,"r")
for i in readfile:
    # f-prefix enables variable substitution
    print('what i value:',i)
    idstrip=i.strip()
    url = f"https://usw1.dmr-us.informaticacloud.com/saas/api/v2/mttask/{idstrip}"
    headers = {
        "icSessionId": sessionid,
        "Accept": "application/json"
    }

    response = requests.request("GET", url, headers=headers)
    mtt=response.json()
    print('sessionname:',mtt['name'],'params:',mtt['sessionProperties']["Pushdown Optimization"] )




