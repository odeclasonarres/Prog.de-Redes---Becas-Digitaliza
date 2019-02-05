#Crear las sentencias necesarias para recoger dos números a través del terminal
n1=int(input("Dime el primer número: "))
n2=int(input("Dime el segundo número: "))
#Integrar funcionalidades de suma, multiplicación, división, y exponencial
func=input("Elige la operación: + * / ^ ")
resultado=0
#Permitir escoger el modo de operación de forma manual
#(el usuario ha de introducir un número para que sepa qué operación realizar)
if func=="+":
    resultado=n1+n2
elif func=="*":
    resultado=n1*n2
elif func=="/":
    resultado=n1/n2
else:
    resultado=n1**n2

#Realizar las operaciones e imprimir el valor por pantalla.
print("El resultado de "+str(n1)+func+str(n2)+" es: "+str(resultado))
