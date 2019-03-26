# Crear una aplicación para acceder a la API de las horas de salida y puesta del sol de la siguiente URL:
# https://api.sunrise-sunset.org/json?lat=48.8584&lng=2.2945
# En el ejemplo, se calcula para París, Francia.

# Crear un archivo llamado: sunsetSunrise.py
# Mostrar las horas para una latitud y longitud concretas (que no sea la del ejemplo; por ejemplo, donde vivís).
# Incluir un print con texto (lo que queráis), con los valores de latitud y longitud, y con las horas obtenidas.
# Subir el archivo a vuestro repositorio en GitHub.

import urllib.parse
import requests

coordenadas=[str(37.1881),str(-3.6066)]
url='https://api.sunrise-sunset.org/json?lat='+coordenadas[0]+'&lng='+coordenadas[1]
json_data = requests.get(url).json()
ciudad='Granada'
salida=json_data['results']['sunrise']
puesta=json_data['results']['sunset']
print("Mi ciudad es: "+ciudad+". Sus coordenadas son: \n\t-Latitud: "+coordenadas[0]+"\n\t-Longitud: "+coordenadas[1]+"\nLa hora de salida del sol: "+salida+"\nLa hora de puesta del sol: "+puesta)
