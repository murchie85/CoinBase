# CoinBase Reporting & Alerting Tool  


## Overview  

![coinbaseimage](https://www.coinbase.com/assets/press/coinbase-logos/coinbase-a673b0735e63d6ea6513e464a83c41165fca9b99b2216b5de70e5187356dd47d.png)

HI! This code which you can clone or download to your local machine so far can do a few things:  
1. Email Alert service for when your portfolio hits a certain high/low which you can configure.  
2. Print your CoinBase Balances to console.  
3. Print all your CoinBase Account Information to console.  

Not all possible methods added due to CoinBase's ongoing work - as of 01/16 most of their functionality contains bugs - however client.getAccounts works and is used here. 

## Steps for running printBalance only.

1. Copy API keys from Coinbase into keys/keys.txt.  
2. Remove brackets <>
3. Now you can run printAll.py or printBalance.py (command = python3 printAll.py

Requirements

1. pip3 install coinbase



Only tested for Python3. 

This code is for my own public use but feel free to make use of it if you can.




# SET UP ALERTING INSTRUCTIONS 

## Steps for setting up your own alerting, you need to have completed the first steps to make this work

Just enter the high and low value by over writing X and Y in alerting.txt respectively you wish to be alerted on such as:

60,40,hightrigger,lowtrigger 

To be alerted if your balance hits 60 or drops below 40. No punctuation or special characters to be used. 
## Important: please don’t remove commas, and keep the formatting. 

# ENTER YOUR EMAIL DETAILS  

On the second line jus fill in your email details such as   
email123@gmail.com,mypassword  

## Important: please don’t remove commas, and keep the formatting. 

### To better utilise this tool, you can run alerting.py on a schedule using crontab or windows scheduler
