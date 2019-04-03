# Packet Tracer: Configuración de redes VLAN

## Parte 1: Verificar la configuración de VLAN predeterminada
#### Paso 1: Mostrar las VLAN actuales
~~~
show vlan brief
~~~

#### Paso 2: Verificar la conectividad entre dos computadoras en la misma red
~~~
En PC1:
ping 172.17.10.24


En PC2:
ping 172.17.20.25

En PC3:
ping 172.17.30.26
~~~
**¿Qué beneficios proporciona configurar las VLAN a la configuración actual?** Preveni que haya mucho tráfico de broadcast.

## Parte 2: Configurar las VLAN
#### Paso 1: Crear y nombrar las VLAN en el S1
~~~
En S1
enable
config t
vlan 20
name Students
vlan 10
name Faculty/Staff
vlan 30
name Guest(Default)
vlan 99
name Management&Native
vlan 150
name VOICE
exit
~~~

#### Paso 2: Verificar la configuración de la VLAN
**¿Con qué comando se muestran solamente el nombre y el estado de la VLAN y los puertos asociados en un
switch?** `show vlan brief`

#### Paso 3: Crear las VLAN en el S2 y el S3
~~~
En S2:
enable
config t
vlan 20
name Students
vlan 10
name Faculty/Staff
vlan 30
name Guest(Default)
vlan 99
name Management&Native
vlan 150
name VOICE
exit

En S3:
enable
config t
vlan 20
name Students
vlan 10
name Faculty/Staff
vlan 30
name Guest(Default)
vlan 99
name Management&Native
vlan 150
name VOICE
exit
~~~

#### Paso 4: Verificar la configuración de la VLAN
~~~
En S2:
enable
show vlan brief

En S3:
enable
show vlan brief
~~~

## Parte 3: Asignar las VLAN a los puertos
#### Paso 1: Asignar las VLAN a los puertos activos en el S2
~~~
En S2:
enable
config t
interface fa0/11
switchport mode access
switchport access vlan 10

interface fa0/18
switchport mode access
switchport access vlan 20

interface fa0/6
switchport mode access
switchport access vlan 30
~~~

#### Paso 2: Asignar VLAN a los puertos activos en S3
~~~
En S3:
enable
config t
interface fa0/11
switchport mode access
switchport access vlan 10

interface fa0/18
switchport mode access
switchport access vlan 20

interface fa0/6
switchport mode access
switchport access vlan 30
~~~

#### Paso 3: Asignar la red VLAN de voz a FastEthernet 0/11 en el S3
~~~
interface fa0/11
mls qos trust cos
switchport voice vlan 150
~~~

#### Paso 4: Verificar la pérdida de conectividad
**Intente hacer ping entre PC1 y PC4. Si bien los puertos de acceso están asignados a las VLAN adecuadas,
¿los pings se realizaron correctamente? ¿Por qué?**
**¿Qué podría hacerse para resolver este problema?**
