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
    #print(mtt)
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
mctlist=['s_api_python','ForAPI_python_4','ForAPI_python_3']
final_dictionary=[]
final_tuple=[]
for m in mctlist:
    getmct_id=MCT_ID(sessionid,m)
# if want to load as dictionary
    taskname,runid=MCT_RUN(sessionid,getmct_id)
    final_dictionary.append({'MCTNAME':taskname,'runid':runid})

print(tabulate(final_dictionary, headers='keys', tablefmt='fancy_grid'))
#if load as normal tuple
    #details = MCT_RUN(sessionid, getmct_id)
    #final_tuple.append(details)
#print(tabulate(final_tuple, headers=['Name', 'runid'], tablefmt='fancy_grid'))

import csv
with open("infa_mct_trigger_table.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['MCTNAME', 'runid'])
    writer.writeheader()
    writer.writerows(final_dictionary)




