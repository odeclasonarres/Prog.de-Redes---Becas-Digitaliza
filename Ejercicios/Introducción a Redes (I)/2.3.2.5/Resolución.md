# Packet Tracer: Implementación de conectividad básica

### Parte 1: Realizar una configuración básica en S1 y S2
#### Paso 1:   Configurar un nombre de host en el S1.
~~~
enable
configure terminal
hostname S1
exit
~~~

#### Paso 2:   Configure las contraseñas de consola y del modo EXEC privilegiado.
~~~
configure terminal
line console 0
password cisco
login
exit

enable
configure terminal
enable password clases
exit
~~~
#### Paso 3:   Verificar la configuración de contraseñas para el S1.
**¿Cómo puede verificar que ambas contraseñas se hayan configurado correctamente?** Comprobando el archivo de startup-config mediante `show running-config`

#### Paso 4: Configure un aviso de MOTD.
~~~
config t
banner motd "Acceso autorizado únicamente. Los infractores se procesarán en la medida en que lo permita la ley."
~~~

#### Paso 5: Guardar el archivo de configuración en la NVRAM.
**¿Qué comando emite para realizar este paso?** `copy running-config startup-config`

#### Paso 6: Repita los pasos 1 a 5 en S2.
~~~
enable
configure terminal
hostname S2
exit

configure terminal
line console 0
password cisco
login
exit

enable
configure terminal
enable password clase
exit

config t
banner motd "Acceso autorizado únicamente. Los infractores se procesarán en la medida en que lo permita la ley."
exit

copy running-config startup-config
~~~
### Parte 2: Configurar las PC
#### Paso 1: Configurar ambas PC con direcciones IP.
~~~

~~~
a.    Haga clic en PC1 y luego en la ficha Escritorio.

b.   Haga clic en Configuración de IP. En la tabla de direccionamiento anterior, puede ver que la dirección IP para la PC1 es 192.168.1.1 y la máscara de subred es 255.255.255.0. Introduzca esta información para la PC1 en la ventana Configuración de IP.

c.    Repita los pasos 1a y 1b para la PC2.

#### Paso 2: Probar la conectividad a los switches.
~~~
ping 192.168.1.253
~~~
**¿Tuvo éxito? Explique.** No, 4 paquetes enviados y 4 perdidos. Los switches aún no tienen IP.

### Parte 3: Configurar la interfaz de administración de switches
#### Paso 1. Configurar S1 con una dirección IP.
**¿Por qué lo configuraríamos con una dirección IP?** Para poder acceder remotamente.
~~~
enable
configure terminal
interface vlan 1
ip address 192.168.1.253 255.255.255.0
no shutdown
exit
~~~
**¿Por qué debe introducir el comando no shutdown?** Para tener habilitada la interfaz virtual.

#### Paso 2. Configurar S2 con una dirección IP.
~~~
enable
configure terminal
interface vlan 1
ip address 192.168.1.254 255.255.255.0
no shutdown
exit
~~~

#### Paso 3: Verifique la configuración de direcciones IP en el S1 y el S2.
~~~
show ip interface brief
~~~

#### Paso 4: Guarde la configuración para el S1 y el S2 en la NVRAM.
**¿Qué comando se utiliza para guardar en la NVRAM el archivo de configuración que se encuentra en la RAM?** `copy run start`

#### Paso 5: Verificar la conectividad de red.
Puede verificarse la conectividad de la red mediante el comando ping. Es muy importante que haya conectividad en toda la red. Se deben tomar medidas correctivas si se produce una falla. Desde la PC1 y la PC2, haga ping al S1 y S2.
~~~
ping 192.168.1.2
ping 192.168.1.253
ping 192.168.1.254
~~~
