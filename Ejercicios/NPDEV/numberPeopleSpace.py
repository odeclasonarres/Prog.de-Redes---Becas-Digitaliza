# Crear un archivo llamado: numberPeopleSpace.py
# Crear una app para saber el número de personas que hay en el espacio. Podéis buscar la información en la siguiente URL:
# http://open-notify.org/Open-Notify-API/
# Subir el archivo a vuestro repositorio en GitHub.
import urllib.parse
import requests

url='http://api.open-notify.org/astros.json'
json_data = requests.get(url).json()
number=int(json_data['number'])
print("Hay "+str(number)+" astronautas.")
print("Sus nombres son: ")
#print(json_data['people'])
for i in json_data['people']:
    print("\t"+i['name'])
