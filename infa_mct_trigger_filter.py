import requests
import json
from tabulate import tabulate

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

def MCT_ID(sessionid,jobname):
    url = f"https://usw1.dmr-us.informaticacloud.com/saas/api/v2/mttask/name/{jobname}"
    headers = {"Accept": "application/json","icSessionId": sessionid}
    response = requests.request("GET", url, headers=headers)
    mtt = response.json()
    print('using get',mtt.get('updateTime'))
    print('using box',mtt['updateTime'])
    if mtt.get('updateTime1') == '2025-12-24T06:09:12.000Z': #use get() if no failure on key missing
    #if mtt['updateTime'] == '2025-12-24T06:09:12.000Z': # return key failure if key missing
        print('mttask id',mtt['id'])
        return mtt['id']

def MCT_RUN(sessionid,mctid):
    url = "https://usw1.dmr-us.informaticacloud.com/saas/api/v2/job"
    headers = {
        "icSessionId": sessionid,
        "Accept": "application/json"
        }
    jobdetails = {
        "@type": "job",
        "taskId": mctid,
        "taskType": "MTT"
        }

    response = requests.request("POST", url, headers=headers,json=jobdetails)
    mtt=response.json()
    print('Triggered MCT:',mtt['taskName'],"RunID:",mtt['runId'])
    return mtt['taskName'],mtt['runId']

#<--Hey--> Program starts here <---Hey--->
sessionid= login_id()
fetchedjobs=[]
mctlist=['ForAPI_python_4','ForAPI_python_3']
mctlist=['s_api_python','ForAPI_python_4','ForAPI_python_3']
for id in mctlist:
    getmct_id=MCT_ID(sessionid,id)
#details=MCT_RUN(sessionid,getmct_id)
    print('inside main',getmct_id)
    if getmct_id and len(getmct_id) >= 10:
        fetchedjobs.append({'mctid':getmct_id,'name':id})
    else:
        fetchedjobs.append({'mctid':'Filtered','name':id})
print(fetchedjobs)
print(len(fetchedjobs))
print(tabulate(fetchedjobs, headers='keys', tablefmt='fancy_grid'))




