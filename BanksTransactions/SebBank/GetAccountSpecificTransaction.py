import json
import requests

#Token should be obtained and changed before start
token = 'ael9WoJLVHo14y9rPhh1'
#Account can be different account_id from SebBank api
account = '5a59028c-e757-4f22-b88c-3ba90573383c'
#Transaction can be different transaction_id from SebBank api
transaction = '6f24de7e-9f81-4f09-999a-b33bead16e8d'

url = 'https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/{0}/transactions/{1}'.format(account, transaction)

payload={}
headers = {
  'Accept': 'application/json',
  'X-Request-ID': '291f8d0d-3f57-4767-8b20-f2a098bea49c',
  'Authorization': 'Bearer {0}'.format(token),
}

response = requests.request("GET", url, headers=headers, data=payload)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))