import json
import requests

r = requests.get('http://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json')
packages_json = r.json()

#print(packages_json)

packages_str = json.dumps(packages_json, indent=2)
print(packages_str)
