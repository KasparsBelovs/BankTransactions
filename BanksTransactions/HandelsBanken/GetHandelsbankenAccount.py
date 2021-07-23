import json
import requests

class GetHandelsbankenAccount:
    def __init__(self, account):
        self.account = account
        self.url = "https://sandbox.handelsbanken.com/openbanking/psd2/v2/accounts/{0}".format(account)
        self.payload={}
        self.headers = {
          'Authorization': 'Bearer MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI1',
          'PSU-IP-Address': '192.102.28.2',
          'TPP-Request-ID': 'c8271b81-4229-5a1f-bf9c-758f11c1f5b1',
          'Accept': 'application/json',
          'TPP-Transaction-ID': '6b24ce42-237f-4303-a917-cf778e5013d6',
          'X-IBM-Client-Id': '62dec6b3-1814-4ca2-864a-c33b91ef6007'
        }

    def run(self):
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload)
        parsed = json.loads(response.text)
        print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))

