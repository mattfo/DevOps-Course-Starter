# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests

response = requests.post('https://api.postcodes.io/postcodes', json={'postcodes' : ["NW5 1TL"]})
lat = response.json()['result'][0]['result']['latitude']
lon = response.json()['result'][0]['result']['longitude']
print(f"Got {lon} {lat}")
print(response.text)