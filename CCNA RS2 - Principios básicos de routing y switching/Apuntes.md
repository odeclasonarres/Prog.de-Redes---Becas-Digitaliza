# CCNA R&S2 - PRINCIPIOS BÁSICOS DE ROUTING Y SWITCHING

# 2. ROUTING ESTÁTICO

## 1. Implementación de rutas estáticas
### Routing estático
**Alcance de redes remotas**:
  - *Manualmente*: se introducen en la tabla de rutas. Puede configurarlas un administrador de red(teniendo que actualizarlas cada vez que cambia la topología de red)
  - *Dinámicamente*: por medio de un protocolo de routing dinámico.

**Por qué routing estático**
Las rutas estáticas son útiles para redes más pequeñas con solo una ruta hacia una red externa. También proporcionan seguridad en una red más grande para ciertos tipos de tráfico o enlaces a otras redes que necesitan más control. Routing estático y dinámico no son excluyentes.
[IMAGEN 2.1]

**Para qué usarlo**
- Facilita el mantenimiento de la tabla de enrutamiento en redes más pequeñas en las cuales no está previsto que crezcan significativamente.
- Proporciona routing hacia las redes de rutas internas y desde estas. Una red de rutas internas es aquella a la cual se accede a través un de una única ruta y cuyo router tiene solo un vecino.
- Utiliza una única ruta predeterminada para representar una ruta hacia cualquier red que no tenga una coincidencia más específica con otra ruta en la tabla de routing. Las rutas predeterminadas se utilizan para enviar tráfico a cualquier destino que esté más allá del próximo router ascendente.


### Tipos de rutas estáticas
**Aplicaciones de rutas estáticas**
- Conectarse a una red específica.
- Conectar un router de redes internas.
- Reducir el número de rutas anunciadas mediante el resumen de varias redes contiguas como una sola ruta estática
- Crear una ruta de respaldo.

**Ruta estática estándar**
Son útiles para conectarse a una red remota específica
[IMGEN 2.2]

**Ruta estática por defecto**
Una ruta predeterminada es una ruta que coincide con todos los paquetes y es utilizada por el router si un paquete no coincide con ninguna otra ruta más específica en la tabla de routing. Una ruta predeterminada puede ser aprendida de forma dinámica o configurada de manera estática. Una ruta estática predeterminada es simplemente una ruta estática con 0.0.0.0/0 como dirección IPv4 de destino. Al configurar una ruta estática predeterminada, se crea un gateway de último recurso.

Las rutas estáticas predeterminadas se utilizan en los siguientes casos:
- Cuando ninguna otra ruta de la tabla de routing coincide con la dirección IP destino del paquete. En otras palabras, cuando no existe una coincidencia más específica. Se utilizan comúnmente cuando se conecta un router periférico de una compañía a la red ISP.
- Cuando un router tiene otro router único al que está conectado. En esta situación, se conoce al router como router de rutas internas.

**Ruta estática resumida**
Para reducir el número de entradas en la tabla de routing, se pueden resumir varias rutas estáticas en una única ruta estática si se presentan las siguientes condiciones:

Las redes de destino son contiguas y se pueden resumir en una única dirección de red.
Todas las rutas estáticas utilizan la misma interfaz de salida o la dirección IP del siguiente salto.

**Ruta estática flotante**
Son rutas estáticas que se utilizan para proporcionar una ruta de respaldo a una ruta estática o dinámica principal, en el caso de una falla del enlace. Únicamente se utilizan cuando la ruta principal no está disponible.

Se configura con una distancia administrativa(confiabilidad de una ruta) mayor que la ruta principal. Si existen varias rutas, el router elegirá la que tenga una menor distancia administrativa.

## 2. Configuración de rutas estáticas y predeterminadas
### Configuración de rutas estáticas IPv4
**Comando ip route**
[IMG 2.3]

**Opciones de siguiente salto**
El siguiente salto se puede identificar mediante una dirección IP, una interfaz de salida, o ambas. El modo en que se especifica el destino genera uno de los siguientes tres tipos de ruta:
  - Ruta del siguiente salto: solo se especifica la dirección IP del siguiente salto
  - Ruta estática conectada directamente: solo se especifica la interfaz de salida del router
  - Ruta estática especificada completamente: se especifican la dirección IP del siguiente salto y la interfaz de salida

**Configuración de una ruta estática de siguiente salto**
En una ruta estática de siguiente salto, solo se especifica la dirección IP del siguiente salto. La interfaz de salida se deriva del próximo salto.

Antes de que un router reenvíe un paquete, el proceso de la tabla de routing debe determinar qué interfaz de salida utilizará para reenviar el paquete. A esto se lo conoce como resolución de rutas.

Una ruta estática recursiva es válida (es decir, es candidata para agregarse a la tabla de routing) solo cuando el siguiente salto especificado resuelve a una interfaz de salida válida, ya sea de forma directa o indirecta. Si la interfaz de salida está “down” (inactiva) o “administratively down” (administrativamente inactiva), la ruta estática no se instalará en la tabla de routing.

**Configuración de una ruta estática conectada directamente**
Al configurar una ruta estática, otra opción es utilizar la interfaz de salida para especificar la dirección del siguiente salto.

La configuración de una ruta estática conectada directamente con una interfaz de salida permite que la tabla de routing resuelva esta interfaz en una única búsqueda, no en dos. Aunque la entrada de la tabla de routing indica “conectado directamente”, la distancia administrativa de la ruta estática sigue siendo 1. Solo una interfaz conectada directamente puede tener una distancia administrativa de 0.

**Configuración de una ruta estática completamente especificada**
Una ruta estática completamente especificada tiene determinadas tanto la interfaz de salida como la dirección IP del siguiente salto. Este es otro tipo de ruta estática que se utiliza en versiones más antiguas de IOS, antes de CEF. Esta forma de ruta estática se utiliza cuando la interfaz de salida es una interfaz de acceso múltiple y se debe identificar explícitamente el siguiente salto. El siguiente salto debe estar conectado directamente a la interfaz de salida especificada.

**Verificación de una ruta estática**:Comandos útiles para verificar rutas estáticas:
- show ip route
- show ip route static
- show ip route Red


### Configuración de rutas predeterminadas IPv4



### Configuración de rutas estáticas IPv6

### Configuración de rutas predeterminadas IPv4

### Configuración de rutas estáticas flotantes

### Configurar rutas de host estáticas

## 3. Resolución de problemas de rutas estáticas y predeterminadas
### Procesamiento de paquetes con rutas estáticas

### Resolución de problemas de configuración de rutas estáticas y predeterminadas IPv4

## 4. Conclusiones  




# 3. ROUTING DINÁMICO

# 5. CONFIGURACIÓN DEL SWITCH
Los switches se usan para conectar varios dispositivos en la misma red. Se pueden configurar manualmente para satisfacer mejor las necesidades de la red.

Los switches se deben configurar para que sean resistentes a los ataques de todo tipo y, al mismo tiempo, protejan los datos de los usuarios y permitan que haya conexiones de alta velocidad. La seguridad de puertos es una de las características de seguridad que proporcionan los switches administrados por Cisco.

En este capítulo, se analizan algunas de las opciones de configuración básica de switch que se requieren para mantener un entorno LAN conmutado seguro y disponible.

## 1. Configuración básica del switch
### Configuración de los parámetros iniciales de un switch
**Secuencia de arranque**:
1. Programa de autodiagnóstico al encender (POST) almacenado en ROM, verifica el subsistema de la CPU. Este comprueba la CPU, la memoria DRAM y la parte del dispositivo flash que integra el sistema de archivos flash.

2. Carga el software del cargador de arranque.

  1. Inicialización de la CPU de bajo nivel(registros de dirección de memoria física, cantidad y velocidad)

  2. Sistema de archivos flash en la placa del sistema.

  3. Carga imagen de IOS en la memoria y delega el control del switch a IOS.
3. IOS inicia las interfaces mediante los comandos que se encuentran en el archivo de configuración de arranque.


### Configuración de puertos de un switch

## 2. Seguridad del switch
### Acceso remoto seguro

### Seguridad de puertos del switch

## 3. Conclusión


# 6. VLAN
