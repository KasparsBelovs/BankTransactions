import json
import requests

class GetSebBankAccountTransactions:
    def __init__(self, token, account):
       self.token = token
       self.account = account
       self.url = 'https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/{0}/transactions?bookingStatus=booked'.format(account)
       self.payload={}
       self.headers = {
           'Accept': 'application/json',
           'X-Request-ID': '74887845-def4-489e-bf0a-358acc5df2c0',
           'PSU-IP-Address': '127.0.0.1',
           'Authorization': 'Bearer {0}'.format(token)
      }

    def run(self):
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        parsed = json.loads(response.text)
        print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))