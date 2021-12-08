# This code sample uses the 'requests' library:
# http://docs.python-requests.org

#from config import KEY, TOKEN
import requests

import os
KEY = os.getenv('KEY')
TOKEN = os.getenv('TOKEN')

url = "https://api.trello.com/1/members/me/boards?fields=name,url"

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