# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests

url = "https://api.trello.com/1/boards/?name=Matt's Temp Board Again"

query = {
   'key': '07d1ead8f2f1211b027cf6bb676a9e28',
   'token': 'ac1373f0fbd69245cde4308a736c14a0debbbd130b28d6f39f57959964f78d53',
   'defaultLists': 'false'
}

response = requests.request(
   "POST",
   url,
   params=query
)

print(response.text)