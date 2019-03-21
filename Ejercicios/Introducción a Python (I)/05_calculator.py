import sys

def bienvenida(op=1):
    if op==0:
        p="Bienvenido a la".center(100,'.')+'\n'+'CALCULADORA'.center(100,'*')
        print(p)
    else:
        p="GRACIAS, hasta la próxima".center(100,'.')
        print(p)
        sys.exit()

def captura(txt,ty=0):
    if ty==0:
        retorno=float(input(txt))
    else:
        retorno=int(input(txt))
    return retorno

def seguir():
    op="\n¿Qué quieres hacer?"
    op+='\n\t1. Realizar una operación aritmética.'
    op+='\n\t2. Salir del programa.'
    op+='\n\Introduce una CIFRA del 1 al 2 para escoger: '
    try:
        op=captura(op,1)
    except ValueError:
        print("Has introducido un valor(texto o números decimales) erróneo")
        seguir()
    if op==1:
        operar()
    elif op==2:
        bienvenida()
    else:
        print("Has elegido un valor numérico erróneo")
        seguir()

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b
def exponencial(a,b):
    return a**b

def operar():
    resultado=0
    op_aritmetica={1:suma, 2:resta, 3:multiplicacion, 4:division, 5:exponencial}
    ciclos=[True,True]
    op="\n¿Qué operación quieres realizar?"
    op+='\n\t1. Suma'
    op+='\n\t2. Resta'
    op+='\n\t3. Multiplicación'
    op+='\n\t4. División'
    op+='\n\t5. Exponencial'
    op+='\nIntroduce una cifra del 1 al 5 para escoger: '
    try:
        op=captura(op, 1)
    except ValueError:
        print("Has introducido un valor(texto o números decimales) erróneo")
        operar()
    if op>5 or op<1:
        print("Has elegido un valor numérico erróneo")
        operar()
    else:
        for elemento in op_aritmetica:
            if op_aritmetica[elemento]==op:
                print(("Has elegido la "+elemento).center(100))
    print('\n'+'Introduce las dos cifras:')
    n1="\t- La primera:  "
    while ciclos[0]:
        try:
            n1=captura(n1,0)
            ciclos[0]=False
        except ValueError:
            print("Has introducido un valor incorrecto(texto), vuelve a probar: ")
            n1=""
    n2="\t- La segunda:  "
    while ciclos[1]:
        try:
            n2=captura(n2,0)
        except ValueError:
            print("Has introducido un valor incorrecto(texto), vuelve a probar: ")
            n2=""
        if op==4:
            try:
                assert n2
                print("ggc")
                ciclos[1]=False
            except AssertionError:
                print("Has introducido un valor incorrecto, no puedes dividir entre 0, vuelve a probar: ")
                n2=""
        else:
            ciclos[1]=False

    operador=op_aritmetica.get(op)
    resultado="{0:.3f}".format(operador(n1,n2))
    print("El resultado de",str(n1),op,str(n2),"es: ",str(resultado))

bienvenida(0)
while True:
    seguir()
