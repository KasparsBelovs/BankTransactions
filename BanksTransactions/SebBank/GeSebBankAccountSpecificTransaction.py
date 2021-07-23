import json
import requests

class GeSebBankAccountSpecificTransaction:
    def __init__(self, token, account, transaction):
      self.token = token
      self.account = account
      self.tranaction = transaction
      self.url = 'https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/{0}/transactions/{1}'.format(account, transaction)
      self.payload={}
      self.headers = {
         'Accept': 'application/json',
         'X-Request-ID': '291f8d0d-3f57-4767-8b20-f2a098bea49c',
         'Authorization': 'Bearer {0}'.format(self.token),
      }

    def run(self):
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        parsed = json.loads(response.text)
        print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))