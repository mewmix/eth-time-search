from codecs import utf_7_decode
import requests
import time
import json
from datetime import timezone

import datetime




headers = {
    'authority': 'api.thegraph.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'origin': 'https://thegraph.com',
    'referer': 'https://thegraph.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Mobile Safari/537.36',
}

## TAKE USER DATE AND TIME INPUT
print("Enter date and time in the format of YYYY-MM-DD HH:MM:SS")
date = input("Enter date: ")
time = input("Enter time: ")

#convert date and time to epoch time UTC
date_time = datetime.datetime.strptime(date + " " + time, '%Y-%m-%d %H:%M:%S')

utc_time = date_time.replace(tzinfo=timezone.utc)



epoch_time = int(utc_time.timestamp())



converted_time = str(epoch_time)

#use a variable within the json_data to store the data of unix time
json_data = {
    'query': '{\n  blocks(first: 1, orderBy: timestamp, orderDirection: asc, where: {timestamp_gte: "'+converted_time+'"}) {\n    number\n    timestamp\n  }\n}\n',
    'variables': None,
}









response = requests.post('https://api.thegraph.com/subgraphs/name/blocklytics/ethereum-blocks', headers=headers, json=json_data)


loaded = json.loads(response.text)
print(json.dumps(loaded, indent=4))
## get the block from the response
blocknum = loaded["data"]["blocks"][0]["number"]
etherscan = "https://etherscan.io/block/"
url = etherscan+blocknum
print(url)