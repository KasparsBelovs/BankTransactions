import json
import requests

#Token should be obtained and changed before start
token = 'ael9WoJLVHo14y9rPhh1'

url = 'https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/?withBalance=false'

payload={}
headers = {
  'Accept': 'application/json',
  'X-Request-ID': 'c745a9cc-0349-44f9-8e4e-5459ef54ff4c',
  'PSU-IP-Address': '127.0.0.1',
  'Authorization': 'Bearer {0}'.format(token)
}

response = requests.request("GET", url, headers=headers, data=payload)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))