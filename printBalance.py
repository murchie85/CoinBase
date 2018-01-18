#----import local libs
import cb
import apiConnect

#----import downloaded libs
import json
import urllib.request
from IPython.display import HTML




accountsArray = []
accounts = apiConnect.client.get_accounts()
jsonData = accounts.data
if "error" not in jsonData: 
    for item in jsonData:   # iterate thru JSON object

        balance = str(item.get("balance"))
        created_at = str(item.get("created_at"))
        currency = str(item.get("currency"))
        cid = str(item.get("id"))
        name =  str(item.get("name"))
        primary =  str(item.get("primary"))
        native_balance =  str(item.get("native_balance"))
        resource =  str(item.get("resource"))
        resource_path =  str(item.get("resource_path"))
        ctype =  str(item.get("type"))
        updated_at =  str(item.get("updated_at"))

        #tmpCoin = coinbase.coinBase(blah)   if we are importing from a coinbase lib
        tmpObjectBucket = cb.cB(balance, created_at,currency, cid, name,primary, native_balance ,resource,resource_path,ctype,updated_at)    # THIS IS CREATION OF OBJECT, CONSTRUCTING (POPULATION)

        accountsArray.append(tmpObjectBucket)
else:
    print("API Returned Error!!")
print("coinBase Objects Filled! Iterate and Print")

selectedCurrency = ["BTC", "GBP", "EUR", "LTC", "ETH", "BCH"]


for account in accountsArray:
    if account.Currency in selectedCurrency: # everytime its in this list we use coin.sth
        print(account.printGBPBalance())
