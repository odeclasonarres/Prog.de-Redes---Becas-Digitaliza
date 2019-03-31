# CCNA Routing&Switching 1

## 0. Introducción al curso
El objetivo de este curso es presentar los conceptos y tecnologías básicos de redes.
- Comparación de la comunicación humana con la de red y observará las semejanzas entre ambas.
- Introducción a los dos modelos principales para planificar e implementar redes: OSI y TCP/IP.
- Obtendrá cierto entendimiento del enfoque de capas de las redes.
- Diversos dispositivos de red y esquemas de asignación de dirección de red.
- Tipos de medios utilizados para transportar datos a través de la red.


[Cisco Aspire](https://www.netacad.com/group/offerings/cisco-aspire)

## 1. Exploración de la red
#### 1.Conectados globalmente
###### Provisión de recursos en una red
  - Redes de muchos tamaños.
  - Clientes y servidores.
  - Redes entre pares

#### 2.LAN, WAN e Internet
###### Componentes de la red
La infraestructura de red tiene tres tipos de componentes:
  - Dispositivos
    - Terminales
    - Dispositivos intermedios(conectan los terminales individuales a la red y pueden conectar varias redes individuales)
  - Medios
    - Cable eléctrico
    - Fibra óptica
    - Inalámbrico
  - Servicios

**Representaciones de red - Diagramas de topología:** proporcionan un mapa visual que muestra cómo está conectada la red.
  - Diagramas de topología física: identifican la ubicación física de los dispositivos intermediarios y la instalación de los cables.
  - Diagramas de topología lógica: identifican dispositivos, puertos y el esquema de direccionamiento.

###### LAN y WAN
**Tipos de redes:**
 - LAN: infraestructuras de red que abarcan un área geográfica pequeña.
  - Su administración de las LAN está a cargo de una única organización o persona. Las políticas de seguridad y control de acceso están implementadas en el nivel de red.
  - Proporcionan un ancho de banda de alta velocidad.
 - WAN: infraestructuras de red que abarcan un área geográfica extensa.
  - Interconectan LAN.
  - La administración está a cargo de proveedores de servicios.
  - Proporcionan enlaces de velocidad más lenta entre redes LAN.
 - MAN: A nivel metropolitano.
 - WLAN: LAN Inalámbrica
 - SAN: son infraestructuras de red diseñadas para admitir servidores de archivos y proporcionar almacenamiento, recuperación y replicación de datos.


###### Internet
Internet es una red global de redes interconectadas (internetworks o internet para abreviar). Garantizar una comunicación efectiva en esta infraestructura heterogénea requiere la aplicación de estándares y tecnologías uniformes, y comúnmente reconocidas.

 - **Intranet**: Conexión privada
 - **Extranet**: Acceso seguro para entes externos que requieren información privada.

**Tecnologías de acceso**
- A nivel doméstico/oficina pequeña:
    - Cable: Internet se transmite a través del mismo cable que transporta televisión por cable. Proporciona una conexión siempre activa con ancho de banda elevado.
    - DSL: se transmite por línea de teléfono proporciona una conexión siempre activa y con ancho de banda elevado. (ADSL, asimétrico: la velocidad de descarga es mayor).
    - Red móvil: se logra mediante una red de telefonía móvil. Rendimiento limitado por las capacidades del teléfono y la antena a la que se conecte.
    - Satelital: Conexión por satélite
    - Telefonía por conexión conmutada: funciona con cualquier línea telefónica y un módem. El ancho de banda es bajo.
- Conexiones empresariales:
    - Líneas arrendadas dedicadas: líneas reservadas dentro de la red del proveedor de servicios que conectan puntos separados geográficamente.
    - WAN Ethernet: este tipo de redes amplían la tecnología de acceso LAN a una WAN..
    - DSL:(SDSL, simétrico: mismas velocidades de subida y descarga).
    - Satelital.

#### 3.La red como plataforma
###### Redes convergentes
 Las redes convergentes pueden transmitir datos de diferente tipo entre muchos tipos diferentes de dispositivos en la misma infraestructura usando el mismo conjunto de reglas, acuerdos y estándares de implementación.

###### Red confiable
Características básicas que las arquitecturas necesitan para cumplir con las expectativas:
 - Tolerancia a fallos: limita el impacto de los fallos para que la cantidad de dispositivos afectados sea la menor posible y que permita una recuperación rápida. Conexiones redundantes:
    - Conmutación por paquetes: divide el tráfico en paquetes que se enrutan a través de una red compartida. Cada paquete tiene la información de dirección necesaria del origen y el destino para que los routers los conmuten según la condición de la red en ese momento, pudiendo tomar distintas rutas para llegar al destino.
 - Escalabilidad: La red se expande para admitir nuevos usuarios y aplicaciones sin afectar el rendimiento.
 - Calidad de servicio (QoS): mecanismo principal para administrar la congestión.
 - Seguridad:
  - Seguridad de la infraestructura de red
  - Seguridad de la información: proteger la información que contienen los paquetes que se transmiten por la red y la información almacenada los dispositivos conectados a la red. Tres requisitos:
    - Confidencialidad: solamente los destinatarios autorizados acceden.
    - Integridad: la información no se altera en la transmisión.
    - Disponibilidad

#### 4. El cambiante entorno de la redes
###### Tendencias de redes
 - BYOD(Bring Your Own Device): significa que se puede usar cualquier dispositivo, de cualquier persona, en cualquier lugar.
 - Colaboración en línea:
 - Videollamadas
 - Computación en la nube:

###### Tecnologías de red para el hogar
 - Hogar inteligente
 - Redes por línea eléctrica
 - Red inalámbrica:
  - WISP
  - Banda ancha Inalámbrica

###### Seguridad de la red
La seguridad es una parte integral de las redes; debe tener en cuenta el entorno, las herramientas y los requisitos. Debe poder proteger los datos y, al mismo tiempo, mantener la calidad de servicio que se espera de la red. Incluye protocolos, tecnologías, dispositivos, herramientas y técnicas para proteger los datos y mitigar amenazas.
 - Amenazas de seguridad:
  - Externas
    - Virus, gusanos y caballos de Troya
    - Spyware y adware
    - Ataques de hora cero
    - Ataques de hackers
    - Ataques por denegación de servicio
    - Interceptación y robo de datos
  - Internas

**Soluciones de seguridad**:
la seguridad debe implementarse en varias capas, y debe utilizarse más de una solución de seguridad
 - Antivirus y antispyware
 - Filtrado de firewall
 - Sistemas de firewall dedicados
 - Listas de control de acceso (ACL)
 - Sistemas de prevención de intrusión (IPS)
 - Redes privadas virtuales (VPN)

###### Arquitectura de red
La arquitectura de red se refiere a los dispositivos, las conexiones y los productos que se integran para admitir las tecnologías y aplicaciones necesarias.









## 2. Configuración de un sistema operativo de red
El Sistema operativo Internetwork (IOS) de Cisco es un término genérico para la colección de sistemas operativos de red que se utilizan en los dispositivos de red Cisco. Cisco IOS se utiliza en la mayoría de los dispositivos Cisco, independientemente del tamaño o el tipo de dispositivo. Este curso se centrará principalmente en Cisco IOS, versión 15.x.

### 1.Entrenamiento intensivo para IOS
La parte del SO que interactúa directamente con el hardware de la computadora se conoce como el Núcleo. La parte que interactúa con las aplicaciones y el usuario se conoce como Shell. El usuario puede interactuar con el shell mediante la interfaz de línea de comandos (CLI) o la interfaz gráfica del usuario (GUI). Se suele acceder a los dispositivos de red mediante una CLI.

**Métodos de acceso**:
 - Consola
 - SSH
 - Telnet

**Modos del comando primario**: Como característica de seguridad, hay 2 modos de acceso de administración:
 - Modo de ejecución de usuario: Permite solo una cantidad limitada de comandos de monitoreo básicos, pero no permite la ejecución de ningún comando que podría cambiar la configuración del dispositivo. La petición de entrada en la terminal termina con el símbolo  `>`.
 - Modo de ejecución privilegiado: Permite acceso a todos los comandos y funciones. La petición de entrada que termina con el símbolo `#`.

 Para pasar del modo usuario al modo con privilegios `enable`. A la inversa `disable`.

 Para configurar el dispositivo, el usuario debe ingresar al modo de configuración global: `configure terminal`, para salir `exit`. En el modo de configuración global, el usuario puede ingresar a diferentes modos de subconfiguración. Cada uno de estos modos permite la configuración de una parte o función específica del dispositivo. Los dos tipos de modos de subconfiguración incluyen lo siguiente:
- Modo de configuración de línea: se utiliza para configurar la consola, SSH, Telnet o el acceso auxiliar. `line console 0`
- Modo de configuración de interfaz: se utiliza para configurar un puerto de switch o una interfaz de red de router. `interface`

**Estructura básica de comandos de IOS**
La sintaxis general es: comando seguido de palabras clave y argumentos.
- Palabra clave: un parámetro específico que se define en el sistema operativo.
- Argumento:valor definido por el usuario.

*Funciones de ayuda*:
- Ayuda contextual: `?` y te lista posibles comandos en ese contexto, o a medias de un comando y lo completa, al final y muestra argumentos y palabras clave.
- Verificación de la sintaxis del comando

### 2. Configuración básica de dispositivos
**Nombres de host**
Al configurar un dispositivo de red, uno de los primeros pasos es la configuración de un nombre único. Si el nombre del dispositivo no se configura explícitamente, Cisco IOS utiliza un nombre de dispositivo predeterminado de fábrica. Reglas de nombres:
- Tienen que comenzar con una letra
- Sin espacios
- Solo letras(mayúsculas o minúsculas), dígitos y guiones(finalizando con letra o dígito)
- Menos de 64 caracteres.

~~~
#Fijar el nombre
configure terminal
hostname nombre-Elegido

#Eliminar el nombre
no hostname
~~~

**Protección del acceso de los dispositivos**
Todos los dispositivos de red deben tener acceso limitado

[IMAGEN]
- *Configuración de contraseñas*:
  - Modo privilegiado: `enable secret contraseñaElegida`
  - Modo usuario
  - Vty: Las líneas de terminal virtual (VTY) habilitan el acceso remoto al dispositivo.

~~~
#usuario
configure terminal
line console 0
password contraseñaElegida
login

#Vty
line vty 0 15
password contraseñaElegida
login
~~~

- *Cifrado de las contraseñas*: Los archivos startup-config y running-config muestran la mayoría de las contraseñas en texto no cifrado.
  - `service password-encryption`:aplica un cifrado débil a todas las contraseñas no cifradas del archivo de configuración.
  - `show running-config`: verificar que se han encriptado.

- *Mensajes de aviso*: Comando de configuración global `banner motd # mensaje del día #`.


**Guardar configuración**
- *Guardar el archivo de configuración en ejecución*: Existen dos archivos de sistema que almacenan la configuración de dispositivos.
  - *startup-config*: almacenado en la NVRAM, contiene todos los comandos que utilizará el dispositivo durante el inicio o reinicio. La memoria NVRAM no pierde su contenido cuando el dispositivo se desconecta. `show startup-config`
  - *running-config*: almacenado en la RAM, refleja la configuración actual. La modificación de una configuración en ejecución afecta al funcionamiento de inmediato. Pierde todo el contenido cuando el dispositivo se apaga o se reinicia. `show running-config `
  - `copy running-config startup-config`

### 3. Esquemas de direcciones
**Puertos y direcciones**
  - *Direcciones IP*:
  - *Interfaces y puertos*:

**Configurar direccionamiento IP**
  - *Configuración manual*: Para que un terminal se comunique a través de la red, se debe configurar con una dirección IPv4 y una máscara de subred únicas. La información de dirección IP se puede introducir en los terminales en forma manual o automáticamente mediante el Protocolo de configuración dinámica de host (DHCP).
  - *Configuración automática*: En una red, DHCP permite la configuración automática de direcciones IPv4 para cada terminal con DHCP habilitado.
  - *Configuración de la interfaz virtual de switch*: Para acceder al switch de manera remota, se deben configurar una dirección IP y una máscara de subred en la SVI. Para configurar una SVI en un switch, utilice el comando de configuración global `interface vlan 1`. Después asigna una dirección IPv4: `ip-address subnet-mask` para la configuración de interfaz. Finalmente, habilite la interfaz virtual con `no shutdown`.

**Verificación de la conectividad**
Del mismo modo que se usan comandos y utilidades como ipconfig para verificar la configuración de red de un host de PC, se deben utilizar los comandos para verificar los ajustes de interfaces y dirección de los dispositivos intermediarios, como switches y routers.
`show ip interface brief`


### 4. Conclusiones
**Capítulo 2: Configuración de un sistema operativo de red**
Cisco IOS es un término que abarca diferentes sistemas operativos que se ejecutan en diversos dispositivos de redes. El técnico puede introducir comandos para configurar o programar el dispositivo a fin de que lleve a cabo diversas funciones de redes. Los routers y switches Cisco IOS realizan funciones de las cuales dependen los profesionales de red para hacer que sus redes funcionen de la forma esperada.

Se accede a los servicios que proporciona Cisco IOS mediante una interfaz de línea de comandos (CLI), a la que se accede a través del puerto de consola, el puerto auxiliar o mediante Telnet o SSH. Una vez que se conectan a la CLI, los técnicos de red pueden realizar cambios de configuración en los dispositivos Cisco IOS. Cisco IOS está diseñado como sistema operativo modal, esto significa que los técnicos de red deben navegar a través de diversos modos jerárquicos del IOS. Cada modo admite distintos comandos del IOS.

Los routers y switches Cisco IOS admiten sistemas operativos modales y estructuras de comandos similares, así como muchos de los mismos comandos. Además, los pasos de configuración inicial durante su implementación en una red son idénticos para ambos dispositivos.

En este capítulo, se presentó Cisco IOS. Se explicaron los diversos modos de Cisco IOS en detalle y se analizó la estructura básica de comandos que se utiliza para configurarlo. También se exploró la configuración inicial de los dispositivos de switch Cisco IOS, que incluye la configuración de un nombre, la limitación del acceso a la configuración de dispositivos, la configuración de mensajes de aviso y el guardado de la configuración.

En el capítulo siguiente, se analiza cómo se desplazan los paquetes a través de la infraestructura de red y se presentan las reglas de comunicación de paquetes.





## Capítulo 3: Protocolos y comunicaciones de red
### 1. Reglas de la comunicación
**Reglas**
  - *Aspectos básicos de la comunicación*: Reglas-->Protocolos; específicos de cada tipo de comunicación. Elementos de la comunicación:
    - Emisor
    - Receptor
    - Mensaje
  - *Requisitos de los protocolos informáticos comunes*:
    - *Codificación de los mensajes*: Proceso mediante el cual la información se convierte en otra forma aceptable para la transmisión. La decodificación revierte este proceso para interpretar la idea.
    - *Formato y encapsulamiento de los mensajes*:  Los formatos de los mensajes dependen del tipo de mensaje y el canal que se utilice para entregar el mensaje. El proceso que consiste en colocar un formato de mensaje (mensaje encapsulado) dentro de otro formato de mensaje (trama) se denomina encapsulamiento.
    - *Tamaño del mensajes*: Las reglas que controlan el tamaño de las partes,que se comunican a través de la red, son muy estrictas. Las tramas que son demasiado largas o demasiado cortas no se entregan, lo que requiere que el host de origen divida un mensaje largo en fragmentos individuales que cumplan los requisitos y que contendrán una parte del mensaje original y su propia información de direccionamiento.
    - *Sincronización del mensaje*:
      - Método de acceso: El método de acceso determina en qué momento alguien puede enviar un mensaje.
      - Control de flujo: Cantidad y velocidad de información que se puede enviar.
      - Tiempo de espera para la respuesta: Cuánto tiempo esperar y qué hacer si se agota el tiempo de espera.
    - *Opciones de entrega del mensaje*: Método de difusión(unidifusión, multififusión y transmisión) y acuse de recibo.

### 2. Protocolos y estándares de red
**Protocolos**
Grupo de protocolos interrelacionados--->suite de protocolos; se muestran en capas, el nivel superior depende de la funcionalidad definida por los niveles inferiores.    

*Protocolos de red*: definen un formato y un conjunto de reglas comunes para intercambiar mensajes entre dispositivos.

*Interacción de protocolos*
  - HTTP: define el contenido y el formato de las solicitudes y respuestas intercambiadas entre el cliente y el servidor.
   - TCP: divide los mensajes HTTP en “segmentos” y es responsable de controlar tamaño e intervalos a los que se intercambian mensajes entre servidor y cliente.
   - IP: tomar los segmentos formateados del TCP, los encapsula en paquetes, asigna direcciones y selecciona la mejor ruta al host de destino.
   - Ethernet: dos funciones principales: la comunicación a través de un enlace de datos y la transmisión física de datos en los medios de red. Los protocolos de acceso a la red son responsables de tomar los paquetes de IP y los formatean para transmitirlos por los medios.

*Suites de protocolos y estándares del sector*
  - *TCP/IP*. os protocolos TCP/IP son específicos de las capas Aplicación, Transporte e Internet.
[IMAGEN]

*Organizaciones de estandarización*
  - Estándares abiertos: Las organizaciones de estandarización son importantes para mantener una Internet abierta con especificaciones y protocolos de libre acceso que pueda implementar cualquier proveedor.
  -

**Modelos de referencia**
[IMAGEN]
- *Modelo de referencia OSI*: este tipo de modelo es coherente con todos los tipos de servicios y protocolos de red al describir qué es lo que se debe hacer en una capa determinada, pero sin regir la forma en que se debe lograr. El modelo OSI proporciona una amplia lista de funciones y servicios que se pueden presentar en cada capa. También describe la interacción de cada capa con las capas directamente por encima y por debajo de él.
  1. *Física*: Describe los medios físicos, funcionales y de procedimiento para mantener la conexión física,
  2. *Enlace de datos*: Describe los métodos para el intercambio de tramas entre dispositivos.
  3. *Red*: Servicios para intercambiar datos individuales entre dispositivos identificados.
  4. *Transporte*: Servicios para segmentar, transferir y reensamblar los datos para conexiones individuales.
  5. *Sesión*: Organiza el diálogo y administra el intercambio de datos.
  6. *Presentación*: Proporciona una representación común de datos transferidos
  7. *Aplicación*: Comunicaciones proceso a proceso

- *Modelo de protocolo TCP/IP*: este tipo de modelo coincide con precisión con la estructura de una suite de protocolos determinada. El modelo TCP/IP es un protocolo modelo porque describe las funciones que ocurren en cada capa de protocolos dentro de una suite de TCP/IP. TCP/IP también es un ejemplo de un modelo de referencia. Define cuatro categorías de funciones que deben ocurrir para que las comunicaciones se lleven a cabo correctamente.
  - *Aplicación*: Representa datos para el usuario más el control de cdificación y de diálogo.
  - *Transporte*: Admite la comunicaciónentre dispositivos
  - *Internet*: Determina el mejor camino a través de una red
  - *Acceso a la red*: Controla los dispositivos del hardware y los medios que forman parte de la red.
  
