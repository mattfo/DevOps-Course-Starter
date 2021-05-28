# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests

r = requests.get('https://api.covid19india.org/data.json')

x=r.json()['statewise']


#print(" ")
#print(r.text)

print(" ")

for i in x:
  print(i['statecode'])
