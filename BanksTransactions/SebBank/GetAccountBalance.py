import json
import requests

#Token should be obtained and changed before start
token = 'ael9WoJLVHo14y9rPhh1'
#Account can be different account_id from SebBank api
account = '5a59028c-e757-4f22-b88c-3ba90573383c'

url = 'https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/{0}/balances'.format(account)

payload={}
headers = {
  'Accept': 'application/json',
  'X-Request-ID': '91fc5dfd-6254-4c68-9ce5-66e861a82884',
  'PSU-IP-Address': '127.0.0.1',
  'Authorization': 'Bearer {0}'.format(token)
}

response = requests.request("GET", url, headers=headers, data=payload)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))