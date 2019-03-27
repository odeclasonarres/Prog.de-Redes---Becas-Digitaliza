import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Granada"
dest = "Madrid"
key = "H77pgsAHyOnis3NuUqQrt4Ord44bXW6G"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)
