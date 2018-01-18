#----import local libs
import cb
import apiConnect

#----import downloaded libs
import json
import urllib.request
from IPython.display import HTML


#----Global Variables
CurrencyList= []
totalBalance = 0
balanceList = []

accountsArray = []
accounts = apiConnect.client.get_accounts()
jsonData = accounts.data





#----Print User Details

print("\n \n")
user = apiConnect.client.get_current_user()
user_as_json_string = json.dumps(user)

print("Printing User Details : ")
print("")
print(user_as_json_string)

print("\n \n")







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
        #idArray.append(account.returnId())\
        print(str(account.returnCurrency()) + " " + str(account.returnNativeBalance()[4:]))

        
        balanceList.append(float(account.returnNativeBalance()[4:]))
        CurrencyList.append(account.returnCurrency())
        
        #SUM BALANCES
        currentBalance = float(account.returnNativeBalance()[4:])
        totalBalance = totalBalance + currentBalance
        
        
        
        
        
totalBalance = round(totalBalance, 2) 
        
print("The total balance in GBP is £"+str(totalBalance))
print(CurrencyList)
print(balanceList)





#----CHECKING THRESHOLD and setting email triggers

alerting = "Thresholds/alerting.txt"
#initialize triggers
highTrigger = 0
lowTrigger = 0
highFlag = "no"
lowFlag = "no"
myEmailAddress = ""
emailPassword = ""


linecount = 0

with open(alerting, 'rU') as f:
    for line in f: 
        if linecount == 0:# extract only on first row
            trigValues = line.split(",")
            highTrigger = float(trigValues[0])
            lowTrigger = float(trigValues[1])
        if linecount == 1:# extract only on second row
            mailValues = line.split(",")
            myEmailAddress = str(mailValues[0])
            emailPassword = str(mailValues[1])
        linecount = linecount + 1

print("\n \n")
print("CHECKING THRESHOLDS......")
print(" ")

print("The high threshold you set is : £" + str(highTrigger))
print("The low threshold you set is : £" + str(lowTrigger))


#-----------------ALERTING 
if totalBalance >= highTrigger:
    print("High Balance Triggered")
    highFlag = "yes"   
if totalBalance <= lowTrigger:
    print("Low Balance Triggered")
    lowFlag = "yes"


print(" ")
print("The  Total Balance is " + str(totalBalance))
print("The stored Email Address for Alerting is " + str(myEmailAddress))





#------------------DISPATCH EMAIL IF TRIGGERED

if totalBalance >= highTrigger or totalBalance <= lowTrigger:
    


    # Email Attachment


    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from smtplib import SMTP
    import smtplib
    import sys


    recipients = [myEmailAddress] 
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = "CoinBase Threshold Alert"
    msg['From'] = myEmailAddress
    msg['Reply-to'] = myEmailAddress

    msg.preamble = 'Multipart massage.\n'

    part = MIMEText("Hi, one of the coinbase thresholds you have set has been triggered. Below are the details : \n\n High threshold triggered? " + str(highFlag) + " \n \n Low threshold triggered? " + str(lowFlag) + " \n \n Total Balance Available £" + str(totalBalance) + "\n \n We have attached your Threshold preferences for reference, you can change the at any time in the coinbase installation folder under Thresholds in the alerting.txt file. \n \n This is still a work in progres so not all functionality works just yet")
    msg.attach(part)

    part = MIMEApplication(open("Thresholds/alerting.txt","rb").read())
    part.add_header('Content-Disposition', 'Thresholds/alerting.txt', filename='Thresholds/alerting.txt')
    msg.attach(part)

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(myEmailAddress, emailPassword)

    server.sendmail(msg['From'], emaillist , msg.as_string())



    print("Threshold met, Email sent")
else:
    print("Threshold not met, no Email required")


