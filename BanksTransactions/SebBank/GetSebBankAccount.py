import json
import requests

class GetSebBankAccount:
    def __init__(self, token, account):
        self.token = token
        self.account = account
        self.url = 'https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/{0}?withBalance=false'.format(account)
        self.payload={}
        self.headers = {
          'Accept': 'application/json',
          'X-Request-ID': 'c0e133c3-403f-40fc-aa8f-83021e8f190b',
          'PSU-IP-Address': '127.0.0.1',
          'Authorization': 'Bearer {0}'.format(token)
        }

    def run(self):
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        parsed = json.loads(response.text)
        print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))
