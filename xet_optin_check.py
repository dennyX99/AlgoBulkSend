from dextoolsmain_data import data
import requests

for i in range(0,len(data)):
    dat = {}
    accountAddress = data[i]["address"]
    assetid = 283820866
    url = "https://mainnet-algorand.api.purestake.io/ps2/v2"
    api_key = "VzZDSA0GmX3p9YpIbryAe8Wtif6VWNUp4CQaV6NG"
    route = "/accounts/"+accountAddress
    res = requests.request("GET", url+route, headers={'x-api-key':api_key}, data={}).json()
    dat["assets"] = res["assets"]
    index = -1
    for i in range(0,len(dat["assets"])):
        if assetid == dat["assets"][i]["asset-id"]:
            index = i
    if index == -1:
        print("Account not optedin into XET:- " + accountAddress)
        

