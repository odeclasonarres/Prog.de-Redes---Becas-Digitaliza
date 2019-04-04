#Crear un script en el que guardéis en una variable un número
num=input("Dime un número  ----->  ")

#Controlar el tamaño del número en 4 rangos
#(menor de 20, entre 20 y 39, entre 40 y 59, mayor de 60)
#En cada uno de los casos imprimir por pantalla el número que se haya introducido.
if(int(num)<20):
    print("Su valor es menor que 20: "+num)
elif((20<=int(num)) and (i0nt(num)<39)):
    print("Su valor está entre 20 y 39: "+num)
elif((40<=int(num)) and (int(num)<59)):
    print("Su valor está entre 40 y 59: "+num)
else:
    print("Su valor es mayor de 60: "+num)
