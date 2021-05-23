# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests

url = "https://api.trello.com/1/boards/60a4c4940294522119175ebc/cards"

query = {
   'key': '07d1ead8f2f1211b027cf6bb676a9e28',
   'token': 'ac1373f0fbd69245cde4308a736c14a0debbbd130b28d6f39f57959964f78d53'
}

response = requests.request(
   "GET",
   url,
   params=query
)

print(response.text)