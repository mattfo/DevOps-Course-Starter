# This code sample uses the 'requests' library:
# http://docs.python-requests.org

#from config import BOARDTEXT, KEY, TOKEN
import requests

import os
BOARDTEXT = os.getenv('BOARDTEXT')
KEY = os.getenv('KEY')
TOKEN = os.getenv('TOKEN')

url = "https://api.trello.com/1/boards/?name=" + BOARDTEXT

query = {
   'key': KEY,
   'token': TOKEN,
   'defaultLists': 'false'
}

response = requests.request(
   "POST",
   url,
   params=query
)

print(response.text)