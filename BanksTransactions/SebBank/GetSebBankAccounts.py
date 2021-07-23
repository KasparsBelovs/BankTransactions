import json
import requests

class GetSebBankAccounts:
    def __init__(self, token):
        self.token = token
        self.url = 'https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/?withBalance=false'
        self.payload={}
        self.headers = {
          'Accept': 'application/json',
          'X-Request-ID': 'c745a9cc-0349-44f9-8e4e-5459ef54ff4c',
          'PSU-IP-Address': '127.0.0.1',
          'Authorization': 'Bearer {0}'.format(token)
        }

    def run(self):
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        parsed = json.loads(response.text)
        print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))