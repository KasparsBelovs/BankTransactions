import json
import requests

class GetSebBankAccountBalance:
    def __init__(self, token, account):
        self.token = token
        self.account = account
        self.url = 'https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/{0}/balances'.format(account)
        self.payload={}
        self.headers = {
          'Accept': 'application/json',
          'X-Request-ID': '91fc5dfd-6254-4c68-9ce5-66e861a82884',
          'PSU-IP-Address': '127.0.0.1',
          'Authorization': 'Bearer {0}'.format(token)
        }

    def run(self):
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        parsed = json.loads(response.text)
        print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))