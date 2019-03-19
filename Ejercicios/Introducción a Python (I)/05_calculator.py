import sys

def bienvenida(op=1):
    if op==0:
        p="Bienvenido a la".center(100,'.')+'\n'+'CALCULADORA'.center(100,'*')
        print(p)
    else:
        p="GRACIAS, hasta la próxima".center(100,'.')
        print(p)
        sys.exit()
#def seguir():
#    op="¿Qué quieres hacer?"
#    op+='\n\t1. Suma'
#    op+='\n\t2. Resta'
#    op+='\n\tIntroduce una cifra del 1 al 5 para escoger'
#    op+='\n\t\t\t'
#    op=int(input(op))
#    if op==1:
#        operar(datos())
#    else:
#        bienvenida()
def datos():
    p='\n'+'\n'+'Introduce las dos cifras'
    print(p)
    #Crear las sentencias necesarias para recoger dos números a través del terminal
    n1=float(input("\tLa primera:  "))
    n2=float(input("\tLa segunda:  "))
    op="¿Qué operación quieres realizar?"
    op+='\n\t1. Suma'
    op+='\n\t2. Resta'
    op+='\n\t3. Multiplicación'
    op+='\n\t4. División'
    op+='\n\t5. Exponencial'
    op+='\n\tIntroduce una cifra del 1 al 5 para escoger'
    op+='\n\t\t\t'
    op=int(input(op))
    dic={'op':op,'1':n1,'2':n2}
    return dic

def operar(dic):
    resultado=0
    #if dic.=="+":
    #    resultado=n1+n2
    #elif func=="*":
    #    resultado=n1*n2
    #elif func=="/":
    #    resultado=n1/n2
    #else:
    #    resultado=n1**n2
    #print("El resultado de "+(n1)+func+str(n2)+" es:
    return resultado

bienvenida(0)
datos()
#print(operar(datos())


#Integrar funcionalidades de suma, multiplicación, división, y exponencial
#func=input("Elige la operación: + * / ^ ")
#resultado=0
#Permitir escoger el modo de operación de forma manual
#(el usuario ha de introducir un número para que sepa qué operación realizar)


#Permitir escoger el modo de operación de forma manual
#Realizar las operaciones e imprimir el valor por pantalla.
#print("El resultado de "+str(n1)+func+str(n2)+" es: "+str(resultado))

# Integrar funcionalidades de suma, resta, multiplicación, división, y exponencial
# Implementar funciones, diccionarios, y excepciones
#(el usuario ha de introducir un número para que sepa qué operación realizar)""
