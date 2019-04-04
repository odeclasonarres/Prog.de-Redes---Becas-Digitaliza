# Crear una lista con nombres de persona e incluir,
#como mínimo, 5 nombres (como mínimo, uno ha de tener la vocal "a")
lista=["Pepe","Juan","Carlos","Jose","Luis", "Ana", "Antonio"]

#Crear una lista llamada "selected"
selected=[]

#Recorrer, mediante un for, la lista de los nombres e imprimir un texto
#con el nombre recorrido en dicha iterración.
#Asimismo, si el nombre de esa iteración contine una "a", añadirlo a la lista llamada "selected"
for nombre in lista:
    for letra in nombre:
        if letra=="a" or letra=="A":
            selected.append(nombre)
            continue 
    print("Toca: "+nombre)

#Finalmente, imprimir por pantalla la lista "selected"
print("Lista seleccionada")
for elem in selected:
    print("Toca: "+elem)
