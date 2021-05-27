# This code sample uses the 'requests' library:
# http://docs.python-requests.org

from config import BOARDTEXT, KEY, TOKEN, TODO
import requests

url = "https://api.trello.com/1/lists/" + TODO + "/cards"

query = {
   'key': KEY,
   'token': TOKEN,
}

response = requests.request(
   "GET",
   url,
   params=query
)

print(response.text)