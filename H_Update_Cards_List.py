# This code sample uses the 'requests' library:
# http://docs.python-requests.org

from config import DOING, DONE, KEY, PYTHONWORK, TODO, TOKEN
import requests
import json

#url = "https://api.trello.com/1/cards/07d1ead8f2f1211b027cf6bb676a9e28"
url = "https://api.trello.com/1/cards/" + PYTHONWORK 

headers = {
   "Accept": "application/json"
}

query = {
   'key': KEY,
   'token': TOKEN,
   'idList': DONE
}

response = requests.request(
   "PUT",
   url,
   headers=headers,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))