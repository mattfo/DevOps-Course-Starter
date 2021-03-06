# This code sample uses the 'requests' library:
# http://docs.python-requests.org

from config import KEY, TOKEN
import requests

url = "https://api.trello.com/1/members/me/boards"

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