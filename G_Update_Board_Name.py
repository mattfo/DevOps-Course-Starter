# This code sample uses the 'requests' library:
# http://docs.python-requests.org

from config import BOARD, BOARDTEXT, KEY, TOKEN
import requests

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