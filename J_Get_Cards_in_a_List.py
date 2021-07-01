# This code sample uses the 'requests' library:
# http://docs.python-requests.org

from config import BOARDTEXT, TODO, DOING, KEY, TOKEN
import requests

url = "https://api.trello.com/1/lists/" + DOING + "/cards"

query = {
   'key': KEY,
   'token': TOKEN,
}

response = requests.request(
   "GET",
   url,
   params=query
)

print(" ")
print(response.text)

x=response.json()

#items = {}
items = []

for i in x:
      print(" ")
      print("Item's ID and Name are:")
      print(i['id'])
      print(i['name'])

      #Items = {'id': {i['id']}, 'status': 'Not Started', 'title': {i['name']} }
      #Items[i] = {'id': i['id'], 'status': 'Not Started', 'title': i['name'] }
      #Items[id] = {'status': 'Not Started', 'title': i['name'] }
      items.append({'id': i['id'], 'status': 'Not Started', 'title': i['name'] })
      
      print(items)

print(" ")


#_DEFAULT_ITEMS = [
#    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
#    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
#]


#items = [
#   { 'id: {response.json()['id']}, 'status': 'Not Started', 'title': {response.json()['name']} }
#   { 'id: {response.json()['response'][0]['result']['id']}, 'status': 'Not Started', 'title': {response.json()['result'][0]['result']['name']} }
#]

#print(items.text)