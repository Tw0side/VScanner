import requests
import socket
from urllib.parse import urlparse
import json

print("Enter url :")
link=input();
api=input("Enter your api key: ")
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