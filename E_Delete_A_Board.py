# This code sample uses the 'requests' library:
# http://docs.python-requests.org

from config import BOARD, KEY, TOKEN
import requests

url = "https://api.trello.com/1/boards/60aae0b71446fd45ec2a19b2"

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