#Crear un script que pregunte por el nombre, el apellido, el teléfono, la ciudad, y la edad.
#Cada valor ha de ser guardado en una variable diferente.
nombre=input("¿Cuál es tu nombre? --> ")
apellidos=input("¿Tus apellidos? --> ")
tlf=input("Cuál es tu número de teléfono --> ")
ciudad=input("¿Dónde vives? --> ")
edad=input("¿Cuál es tu edad? --> ")

#Imprimir, por pantalla, toda la infomarción coleccionada en una frase que combine la información
#con coherencia (una oración que no sólo sean los datos recogidos).
print("Te llamas "+nombre+" "+apellidos+", tienes "+edad+" años, tu número de teléfono es "+tlf+" y vives en "+ciudad+".")
