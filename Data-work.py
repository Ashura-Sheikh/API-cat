import json
import requests

# Requests for a different API 
requests = requests.get("http://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json")


# Printing required details
print(requests)
print('Encoding:' , requests.encoding)
print('STATUS_CODE: ', requests.status_code)
print('HEADERS: ', requests.headers)
print('TEXT: ', requests.text)
print('CONTENT: ', requests.content)
print('JSON: ', requests.json)
