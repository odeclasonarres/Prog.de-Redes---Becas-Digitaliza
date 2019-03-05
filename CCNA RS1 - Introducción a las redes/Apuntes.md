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
