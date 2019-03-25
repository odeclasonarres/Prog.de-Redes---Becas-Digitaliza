# PROGRAMACIÓN DE REDES

## 1.

#### 1.2.1.
Orden de evaluación de operaciones aritméticas: PEMDAS.
  - Parentheses
  - Exponents
  - Multiplication and Division
  - Addition and Subtraction


#### 1.2.6.
~~~
open(name, [mode])
  mode:
    -r: read, modo por defecto.
    -w: write.
    -a: append.
~~~

Borrar las líneas en blanco al final de cada lectura de archivo:
`strip()`

~~~
devices = []
 file = open ("devices.txt", "r")
para el elemento en el archivo:
   item = item.strip ()
   devices.append (item)
 file.close ()
print (devices)
~~~

#### 1.3.1: Interfaz de programación de aplicaciones (API)
Una API define cómo un programador puede escribir software que se comunique con una aplicación existente o incluso crear aplicaciones completamente nuevas. El creador de la API especifica cómo y bajo qué circunstancias los programadores pueden acceder a la interfaz.


*Interfaz de servicios web usando HTTP*
Los navegadores web usan HTTP para solicitar (GET) una página web, y los servidores devuelven un documento HTML.
[IMAGEN]

*RESTful API usando HTTP*
Las REST API de transferencia de estado de representación (REST) ​​utilizan HTTP para interactuar con los servicios REST, el servidor responderá con datos JSON.
[IMAGEN]

 - *Solicitudes REST*:
[IMAGEN]
  - Servidor API : la URL del servidor que responde a las solicitudes REST
  - Recursos : especifica la API que se solicita
  - Formato : Generalmente JSON o XML
Parámetros : Especifica qué datos se solicitan.

1.3.2.1: JSON
JSON es un formato para almacenar e intercambiar texto entre un servidor y una aplicación cliente. Es fácil de leer y escribir. JSON es un formato muy popular que los servicios web y las API utilizan para proporcionar datos públicos porque es fácil de analizar y se puede usar con la mayoría de los lenguajes de programación modernos, incluido Python.

1.3.2.2: XML
XML amplía la funcionalidad de HTML al permitir a los programadores web construir etiquetas personalizadas. M´as dificil de leer que JSON.