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
##### 2.1.1 Conceptos
Con los dispositivos de red con los que estamos familiarizados, puede pensar que un enrutador o conmutador es un dispositivo único. Sin embargo, las funciones principales de estos dispositivos se pueden dividir en dos planos:
- **Plano de control**: Toma decisiones de reenvío. El plano de control contiene los mecanismos de reenvío de rutas de Capa 2 y Capa 3. La información enviada al plano de control es procesada por la CPU.
- **Plano de datos**: también llamado plano de reenvío, este plano se usa para reenviar flujos de tráfico. Los enrutadores y conmutadores utilizan la información del plano de control para reenviar el tráfico entrante a través de la interfaz de egreso apropiada.

Al separar el plano de control y el plano de datos, los programadores de red pueden centralizar la información que utilizan los dispositivos para tomar decisiones de reenvío y realizar otras funciones.

En las redes SDN, el plano de control está centralizado en un controlador SDN, una entidad lógica que permite a los administradores de red administrar y dictar cómo debe manejar el plano de datos de enrutadores y conmutadores tráfico de red. SDN utiliza el protocolo OpenFlow para comunicarse entre el controlador y los dispositivos de red.

[IMAGEN]

Un enfoque SDN diferente está representado por los controladores Cisco APIC o APIC-EM SDN. Estos controladores crean una abstracción desde el tejido de la red física en la parte inferior hasta las aplicaciones en la parte superior.

En este caso, el plano de control no necesita ser desacoplado del plano de datos. El plano de control aún reside en todos los dispositivos, lo que proporciona inteligencia distribuida local donde se necesita. Este enfoque elimina la posibilidad de que el controlador se convierta en el cuello de botella de la red. Los dispositivos de red existentes, como los enrutadores y los conmutadores, se siguen utilizando para crear redes distribuidas escalables y de alto rendimiento.

En el pasado, el personal de la red ha tenido que pasar mucho tiempo en la infraestructura al final del diagrama (los conmutadores y los enrutadores) conectándolos entre sí para construir una arquitectura de red. Donde la gente realmente necesita gastar su tiempo, en lo que prospera el negocio digital, es esta capa de aplicación en la parte superior del diagrama.

El controlador SDN en este caso es muy importante, porque concilia las dos necesidades de la organización. Presenta la capa de aplicación con abstracciones de la red que se encuentra debajo. Debido a esto, las aplicaciones pueden consumir muy fácilmente servicios de red. Esto es crítico porque la empresa digital está completamente orientada a la aplicación. Estas aplicaciones de software controlan la orquestación, la automatización, la colaboración, la política y la seguridad para que el personal de la red pueda trabajar con la representación abstracta y fácil de usar del tejido de la red.

La apertura del entorno de software a desarrolladores externos fomenta la innovación y el crecimiento. DevNet es un recurso primordial para facilitar las relaciones entre Cisco y los desarrolladores. Aquí está la necesidad de que los desarrolladores de aplicaciones de red que interactúen con el controlador SDN, a través de las API REST, puedan satisfacer las necesidades empresariales en la operación de la infraestructura física.
[IMAGEN]

[IMAGEN]
Como se muestra en la figura, el controlador Cisco APIC-EM SDN se comunica con la topología física mediante protocolos API estándar de Southbound como SNMP, SSH y Telnet en lugar de un protocolo como OpenFlow. Esto hace que una abstracción fácil de usar del tejido de red esté disponible para las aplicaciones que utilizan una interfaz de API REST estándar.

Estas aplicaciones pueden ejecutarse desde grandes herramientas de orquestación "todo en uno" hasta scripts simples que usan una sola llamada de API para responder una pregunta como, "¿Cuántas computadoras están conectadas a nuestra red?" Imagine responder esa pregunta con un nivel de conocimiento CCENT de su computadora por SSHing a cada enrutador y conmutador e ingresando comandos en la CLI como "show ip route", "show ip arp", y "show mac address-table". Entonces imagine que trata de darle sentido a toda la salida para crear Una respuesta significativa a la pregunta simple.

Ahora analizamos más de cerca cómo podemos responder preguntas sobre una red mediante el uso de las API APIC-EM.

#### 2.1.2 APIC-EM
APIC-EM es un controlador SDN que tiene las siguientes características:
- Controlador SDN de red empresarial
- Puede ser un dispositivo de software virtual o un dispositivo físico
- Crea una red inteligente, abierta y programable con API abiertas
- Puede transformar las políticas de intención empresarial en una configuración de red dinámica.
- Proporciona un punto único para la automatización y el control de toda la red.

[Access the APIC-EM sandbox environments hosted](https://DevNetSBX-NetAcad-APICEM-3.cisco.com)
