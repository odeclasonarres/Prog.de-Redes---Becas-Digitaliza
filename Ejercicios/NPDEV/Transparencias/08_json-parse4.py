import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "H77pgsAHyOnis3NuUqQrt4Ord44bXW6G"
while True:
    orig = input("Introduce la localidad de origen: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Introduce la localidad de destino: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = Encontrada ruta exitosa.\n")
