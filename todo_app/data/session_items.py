# This code sample uses the 'requests' library:
# http://docs.python-requests.org
# 
# 
# from flask import session
#from .env import KEY, TOKEN, TODO, DOING, DONE

#from config import KEY, TOKEN, TODO, DOING, DONE
import requests

import os
KEY = os.getenv('KEY')
TOKEN = os.getenv('TOKEN')
TODO = os.getenv('TODO')
DOING = os.getenv('DOING')
DONE = os.getenv('DONE')

class ViewModel:
    def __init__(self, items):
        self._items = items
    
    @property
    def items(self):
        return self._items

def get_items(idList):
    """
    Fetches all cards for the particular list id argument.
    """

    url = "https://api.trello.com/1/lists/" + idList + "/cards"

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

    #empty list:
    items = []
    array_count = 0

    for i in x:
        #print(i['id'])
        #print(i['name'])

        array_count + 1
        items.append({'id': i['id'], 'status': 'Not Started', 'title': i['name'] })

    return items

def get_item(id):
    """
    Fetches the saved item with the specified ID.

    Args:
        id: The ID of the item.

    Returns:
        item: The saved item, or None if no items match the specified ID.
    """
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(name):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """

    url = "https://api.trello.com/1/cards"

    query = {
    'key': KEY,
    'token': TOKEN,
    'idList': TODO,
    'name': name
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )

    print(response.text)

def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item


def complete_item(id):
#    item = get_item(id)
#
#    if item != None:
#        item['status'] = 'Completed'
#        save_item(item)
#
#    return item

    url = "https://api.trello.com/1/cards/" + id 

    headers = {
    "Accept": "application/json"
    }

    query = {
    'key': KEY,
    'token': TOKEN,
    'idList': DONE
    }

    response = requests.request(
    "PUT",
    url,
    headers=headers,
    params=query
    )

    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


