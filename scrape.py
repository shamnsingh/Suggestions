import json
import requests
import sys

# Pass in an artists name for query.
artist = str(sys.argv[1])

# Obtain data in json format.
url = 'http://ws.spotify.com/search/1/artist.json?q='
response = requests.get(url + artist)
data = json.loads(response.text)

for i in range(0,5):
	print(data['artists'][i]['name'])