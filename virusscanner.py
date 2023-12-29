import requests
import socket
from urllib.parse import urlparse
import json

def getapikey():
	url = "http://127.0.0.1:5000/random_api"
	response = requests.get(url)
	apikey = json.loads(response.text)
	apikey = apikey[0][0]
	return apikey

print("Enter url :")
link=input();
api=getapikey()
domain=urlparse(link).netloc
ip=socket.gethostbyname(domain)

url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip

headers = {
'x-apikey':api,
"accept": "application/json"
}

response = requests.get(url, headers=headers)

with open('response.txt','w')as file:
	file.write(response.text)

print("Response saved")