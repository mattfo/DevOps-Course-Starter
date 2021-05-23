# This code sample uses the 'requests' library:
# http://docs.python-requests.org

from config import KEY, TOKEN
import requests

url = "https://api.trello.com/1/boards/?name=Matt's Temp Board Again"

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