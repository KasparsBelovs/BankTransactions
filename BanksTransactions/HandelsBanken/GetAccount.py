import json
import requests

account = 'ae57e780-6cf3-11e9-9c41-e957ce7d7d69'
url = "https://sandbox.handelsbanken.com/openbanking/psd2/v2/accounts/{0}".format(account)

payload={}
headers = {
  'Authorization': 'Bearer MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI1',
  'PSU-IP-Address': '192.102.28.2',
  'TPP-Request-ID': 'c8271b81-4229-5a1f-bf9c-758f11c1f5b1',
  'Accept': 'application/json',
  'TPP-Transaction-ID': '6b24ce42-237f-4303-a917-cf778e5013d6',
  'X-IBM-Client-Id': '62dec6b3-1814-4ca2-864a-c33b91ef6007'
}

response = requests.request("GET", url, headers=headers, data=payload)
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=3, separators=(',', ':'), sort_keys=True))

