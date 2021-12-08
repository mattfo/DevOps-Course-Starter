# This code sample uses the 'requests' library:
# http://docs.python-requests.org

#from config import BOARD, BOARDTEXT, KEY, TOKEN
import requests

import os
BOARD = os.getenv('BOARD')
BOARDTEXT = os.getenv('BOARDTEXT')
KEY = os.getenv('KEY')
TOKEN = os.getenv('TOKEN')

#url = "https://api.trello.com/1/boards/60a4c4940294522119175ebc"
url = "https://api.trello.com/1/boards/" + BOARD

query = {
   'key': KEY,
   'token': TOKEN,
   #'name': 'Matt ToDo Board'
   'name': BOARDTEXT
}

response = requests.request(
   "PUT",
   url,
   params=query
)

print(response.text)