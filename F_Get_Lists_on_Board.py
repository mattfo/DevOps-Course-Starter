# This code sample uses the 'requests' library:
# http://docs.python-requests.org

from config import BOARD, KEY, TOKEN
import requests

url = "https://api.trello.com/1/boards/" + BOARD + "/lists"

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