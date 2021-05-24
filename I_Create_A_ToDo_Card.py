# This code sample uses the 'requests' library:
# http://docs.python-requests.org

from config import KEY, TODO, TOKEN
import requests

url = "https://api.trello.com/1/cards"

query = {
   'key': KEY,
   'token': TOKEN,
   'idList': TODO,
   'name': 'GITHUB'
}

response = requests.request(
   "POST",
   url,
   params=query
)

print(response.text)
