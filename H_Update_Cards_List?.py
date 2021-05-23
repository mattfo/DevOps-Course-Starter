# This code sample uses the 'requests' library:
# http://docs.python-requests.org

from config import KEY, TOKEN
import requests
import json

url = "https://api.trello.com/1/cards/07d1ead8f2f1211b027cf6bb676a9e28"

headers = {
   "Accept": "application/json"
}

query = {
   'key': KEY,
   'token': TOKEN,
   'idList': '60a4c4a7405fc93aa8f1a999'
}

response = requests.request(
   "PUT",
   url,
   headers=headers,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))