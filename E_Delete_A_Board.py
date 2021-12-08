# This code sample uses the 'requests' library:
# http://docs.python-requests.org

#from config import BOARD, KEY, TOKEN
import requests

import os
BOARD = os.getenv('BOARD')
KEY = os.getenv('KEY')
TOKEN = os.getenv('TOKEN')

url = "https://api.trello.com/1/boards/" + BOARD

query = {
   'key': KEY,
   'token': TOKEN
}

response = requests.request(
   "DELETE",
   url,
   params=query
)

print(response.text)