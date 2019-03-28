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

#### 1.3.3 Parseando JSON con Python
*Autenticación de una solicitud RESTful*
 - Ninguna: La API es pública y cualquiera puede realizar la solicitud.
 - HTTP básico: Un nombre de usuario y contraseña se pasan al servidor en un string codificado.
 - Token: Con una clave secreta generalmente proporcionada por los desarrolladores de la API.
 - Autorización abierta (OAuth): un estándar abierto para recuperar un token de acceso de un proveedor de identidad. El token se pasa con cada llamada a la API


## 2. PROGRAMANDO APIC-EM
### 2.1. Programabilidad de red
Con los dispositivos de red con los que estamos familiarizados, puede pensar que un enrutador o conmutador es un dispositivo único. Sin embargo, las funciones principales de estos dispositivos se pueden dividir en dos planos:
- **Plano de control**: Toma decisiones de reenvío. El plano de control contiene los mecanismos de reenvío de rutas de Capa 2 y Capa 3. La información enviada al plano de control es procesada por la CPU.
- **Plano de datos**: también llamado plano de reenvío, este plano se usa para reenviar flujos de tráfico. Los enrutadores y conmutadores utilizan la información del plano de control para reenviar el tráfico entrante a través de la interfaz de egreso apropiada.

Al separar el plano de control y el plano de datos, los programadores de red pueden centralizar la información que utilizan los dispositivos para tomar decisiones de reenvío y realizar otras funciones.

En las redes SDN, el plano de control está centralizado en un controlador SDN, una entidad lógica que permite a los administradores de red administrar y dictar cómo debe manejar el plano de datos de enrutadores y conmutadores tráfico de red. SDN utiliza el protocolo OpenFlow para comunicarse entre el controlador y los dispositivos de red.

[IMAGEN]
