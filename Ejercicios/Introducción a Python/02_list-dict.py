#Crear una lista que contenga varios strings.
lista1=["nombre","palabra","rap"]

#Crear una lista que contenga varios integers.
lista2=[1,4,6,9]

#Crear una lista que contenga strings, integers y floats.
lista3=["2",2, 2.3]

#Crear las sentencias necesarias para imprimir, por pantalla, la información de las listas.
print(lista1)
print(lista2)
print(lista3)

#Crear 3 sentencias para asignar, en cada una, el último valor de una lista diferente a una variable
#(es decir, habrá 3 variables, cada una con el último valor de una de las listas).
var1=lista1[len(lista1)-1]
var2=lista2[len(lista2)-1]
var3=lista3[len(lista3)-1]

#Crear una sentencia para imprimir, por pantalla, un texto, y concatenar la información de las variables.
print("La primera variable vale: "+var1+".\nLa segunda: "+str(var2)+".\nLa tercera: "+str(var3)+".")

#Crear un diccionario de vuestras películas/obras favoritas (clave: autor, valor:película)
dicc={'tarantino':'reservoir dogs', 'coppola':'el padrino', 'scorcese':'casino', 'de niro':'historia del bronx'}

#Crear sentencia para imprimir por pantalla todo el diccionario.
print(dicc)

#Crear sentencia para imprimir por pantalla sólo las claves del diccionario
print(dicc.keys())

#Crear sentencia para imprimir por pantalla sólo los valores del diccionario.
print(dicc.values())
