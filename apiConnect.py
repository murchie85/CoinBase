import os
from coinbase.wallet.client import Client


"""
API Key + Secret
If you're writing code for your own Coinbase account, enable an API key.

Next, create a Client object for interacting with the API:

API Key: B843sfzmpqWIov45

API Secret: S4dvIqFPHV1m2N2ttCSW7u84BUDa3sbV

"""
directory = "keys/keys.txt"
#initialize keys
api_key = ""
api_secret = ""

with open(directory, 'rU') as f:
    for line in f: # Iterate through rows
        keys = line.split(",")
        api_key = keys[0]
        api_secret = keys[1]


# Define global client
global client
client = Client(api_key, api_secret)