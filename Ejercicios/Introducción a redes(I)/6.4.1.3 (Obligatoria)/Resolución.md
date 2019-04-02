# Packet Tracer: Configuración inicial del router

## Parte 1: Verificar la configuración predeterminada del router
#### Paso 1: Establecer una conexión de consola con el R1
#### Paso 2: Ingresar al modo con privilegios y examinar la configuración actual.
~~~
enable
show running-config
show startup-config
~~~
##### c)
**¿Cuál es el nombre de host del router?** Router
**¿Cuántas interfaces Fast Ethernet tiene el router?** 4
**¿Cuántas interfaces Gigabit Ethernet tiene el router?** 2
**¿Cuántas interfaces seriales tiene el router?** 2
**¿Cuál es el rango de valores que se muestra para las líneas vty?** 0-4

##### d)
**¿Por qué el router responde con el mensaje startup-config is not present?** El archivo de configuración solo está en la RAM aún.

## Parte 2: Configurar y verificar la configuración inicial del router
#### Paso 1: Configurar los parámetros iniciales del R1.
~~~
configure terminal
hostname R1

exit
configure terminal
line console 0
password letmein
login
exit
exit

enable
configure terminal
enable password cisco
exit


config t
enable secret itsasecret
exit

config t
service password-encryption
exit

config t
banner motd "Unauthorized access is strictly prohibited (El acceso no autorizado queda terminantemente prohibido)"
~~~

#### Paso 2: Verificar los parámetros iniciales del R1.
**Para verificar los parámetros iniciales, observe la configuración de R1. ¿Qué comando utiliza?** `show running-config`

**¿Por qué todos los routers deben tener un mensaje del día (MOTD)?** Para informar que solo el personal autorizado debe intentar obtener acceso al dispositivo, y que en caso de hacerlo sin estar autorizado puede suponer una infracción legal. O para enviar mensajes al personal autorizado.

**Si no se le pide una contraseña, ¿qué comando de la línea de consola se olvidó de configurar?** `login` despues de `password letmein`

**¿Por qué la contraseña de enable secret permitiría el acceso al modo EXEC privilegiado y la contraseña de enable dejaría de ser válida?** La contraseña de `enable secret` sobreescribe a la de `enabled`

**Si configura más contraseñas en el router, ¿se muestran como texto no cifrado o en forma cifrada en el archivo de configuración? Explique.** Se mostrarán como texto cifrado, ya que `service password-encryption` encripta las contraseñas que están en el archivo de configuración, sean presentes o futuras.

## Parte 3: Guardar el archivo de configuración en ejecución
#### Paso 1: Guardar el archivo de configuración en la NVRAM.
~~~
copy running-config startup-config
~~~

**¿Qué comando introdujo para guardar la configuración en la NVRAM?** `copy running-config startup-config`
**¿Cuál es la versión más corta e inequívoca de este comando?** `copy r s`
**¿Qué comando muestra el contenido de la NVRAM?** `show start`

#### Paso 2: Puntos extra opcional: guarde el archivo de configuración de inicio en la memoria flash.
~~~
show flash
~~~
**¿Cuántos archivos hay almacenados actualmente en la memoria flash?** 3
**¿Cuál de estos archivos cree que es la imagen de IOS?** El 3: `c1900-universalk9-mz.SPA.151-4.M4.bin`
**¿Por qué cree que este archivo es la imagen de IOS?** Porque es un `.bin`

~~~
copy startup-config flash
show flash
~~~
