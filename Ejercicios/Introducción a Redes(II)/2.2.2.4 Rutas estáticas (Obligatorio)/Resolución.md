# Packet Tracer: configuración de rutas estáticas y predeterminadas IPv4

## Parte 1: examinar la red y evaluar la necesidad de routing estático
**Observe el diagrama de la topología. ¿Cuántas redes hay en total?** 5
**¿Cuántas redes están conectadas directamente al R1, al R2 y al R3?** A R1 y R3 dos redes. A R2 3 redes.
**¿Cuántas rutas estáticas requiere cada router para llegar a las redes que no están conectadas directamente?** R1 y R3 necesitan 3 redes. R2 necesita 2.
**Pruebe la conectividad a las LAN del R2 y el R3 haciendo ping de la PC1 a la PC2 y la PC3.¿Por qué no logró hacerlo?**
~~~
ping 172.31.0.254
ping 172.31.1.190
~~~
Porque no hay rutas estáticas definidas desde R1.

## Parte 2: configurar rutas estáticas y predeterminadas
#### Paso 1: configurar rutas estáticas recursivas en el R1.
**¿Qué es una ruta estática recursiva?** Una ruta que depende del router del siguente salto para que lleguen los paquetes al destino.
**¿Por qué una ruta estática recursiva requiere dos búsquedas en la tabla de routing?** Primero busca la ruta para llegar en la red de destino y luego la interfaz al router de siguiente salto.
**Configure una ruta estática recursiva a cada red que no esté conectada directamente al R1, incluidos los enlaces WAN entre el R2 y el R3.**
~~~
En R1:
enable
configure terminal
ip route 172.31.0.0 255.255.255.0 172.31.1.193
ip route 172.31.1.196 255.255.255.252 172.31.1.193
ip route 172.31.1.128 255.255.255.192 172.31.1.193
~~~
**Pruebe la conectividad a la LAN del R2 y haga ping a las direcciones IP de la PC2 y la PC3.**
~~~
ping 172.31.0.254
ping 172.31.1.190
~~~


#### Paso 2: ¿por qué no logró hacerlo? configurar rutas estáticas conectadas directamente en el R2.
~~~
En R2:
enable
configure terminal
ip route 172.31.1.0 255.255.255.128 172.31.1.1
ip route 172.31.1.128 255.255.255.192 172.31.1.129
~~~
**¿En qué se diferencia una ruta estática conectada directamente de una ruta estática recursiva? Configure una ruta estática conectada directamente del R2 a cada red que no esté conectada directamente.**
~~~

~~~
**¿Con qué comando se muestran solo las redes conectadas directamente?** ` `
**¿Con qué comando se muestran solo las rutas estáticas que se indican en la tabla de routing?** ` `
**Al ver la tabla de routing completa, ¿cómo se puede distinguir entre una ruta estática conectada directamente y una red conectada directamente?**

#### Paso 3: configurar una ruta predeterminada en el R3.
**¿En qué se diferencia una ruta predeterminada de una ruta estática común? Configure una ruta predeterminada en el R3 de modo que se pueda llegar a cada red que no esté conectada directamente.**
~~~
ip route 0.0.0.0 0.0.0.0 172.31.1.196
~~~
**¿Cómo se muestra una ruta estática en la tabla de routing?** ` `

#### Paso 4: registrar los comandos para las rutas completamente especificadas.
~~~

~~~
**Explique qué es una ruta completamente especificada. ¿Qué comando proporciona una ruta estática completamente especificada del R3 a la LAN del R2?**............... ` `
**Escriba una ruta completamente especificada del R3 a la red entre el R2 y el R1. No configure la ruta, solo calcúlela.** ` `
**Escriba una ruta estática completamente especificada del R3 a la LAN del R1. No configure la ruta, solo calcúlela.** ` `

#### Paso 5: verificar la configuración de la ruta estática.
**Utilice los comandos show correspondientes para verificar que la configuración sea la correcta.**
~~~

~~~
**¿Qué comandos show puede utilizar para verificar que las rutas estáticas están configuradas correctamente?** ` ` ó ` `

## Parte 3: verificar la conectividad
~~~

~~~
ping 172.31.0.254 255.255.255.0
ping 172.31.1.190 255.255.255.192
