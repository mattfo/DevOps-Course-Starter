# This code sample uses the 'requests' library:
# http://docs.python-requests.org

#from config import KEY, TOKEN, BOARD
import requests

import os
KEY = os.getenv('KEY')
TOKEN = os.getenv('TOKEN')
BOARD = os.getenv('BOARD')


url = "https://api.trello.com/1/boards/" + BOARD + "/cards"

query = {
   'key': KEY,
   'token': TOKEN
}

response = requests.request(
   "GET",
   url,
   params=query
)

print(response.text)





# New

items = response.json()['result'][0]['result']['id']

#print(response.text)
