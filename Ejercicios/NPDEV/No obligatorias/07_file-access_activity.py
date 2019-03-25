# Abra un archivo nuevo y guárdelo como 07_file-access_actvity.py
# Para la función open() use el modo a, que le permitirá agregar un elemento al archivo devices.txt
# Dentro de un bucle while True: loop, mete un input() que solicita al usuario el nuevo dispositivo.
# Establezca el valor de la entrada del usuario en una variable llamada newItem .
# Use una instrucción if que rompa el ciclo si el usuario escribe exit e imprime la declaración "¡Todo listo!" .
# Use el comando file.write( newItem + “\ n”) para agregar el nuevo dispositivo provisto por el usuario.

from os import strerror

newItem=""
try:
    stream = open('devices.txt','at')
    while True:
        newItem = input("Introduce otro dispositivo: ")
        if newItem == "exit":
            break
        else:
            stream.write(newItem+"\n")
    stream.close()
    print("Listo")
except IOError as e:
	print("Ha ocurrido un error: ", strerr(e.errno))
