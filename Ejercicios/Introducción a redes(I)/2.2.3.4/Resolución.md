## Packet Tracer: Configuración de los parámetros iniciales del switch
### Parte 1:
#### Paso 1: Ingrese al modo EXEC privilegiado.
~~~
enable
~~~
#### Paso 2: Examine la configuración actual del switch.
~~~
show running-config
~~~

**1. ¿Cuántas interfaces FastEthernet tiene el switch?** Tiene 24

**2. ¿Cuántas interfaces Gigabit Ethernet tiene el switch?** Tiene 2

**3. ¿Cuál es el rango de valores que se muestra para las líneas vty?** De 0 a 4 y de 5 a 15

**4. ¿Qué comando muestra el contenido actual de la memoria de acceso aleatorio no volátil (NVRAM)?** `show startup-config`

**5.  ¿Por qué el switch responde con startup-config is not present?** El archivo de configuración solo está en la RAM de momento.

### Parte 2: Establecer una configuración básica del switch
#### Paso 1:  Asigne un nombre al switch.
~~~
configure terminal
hostname S1
exit
~~~

#### Paso 2: Proporcionar un acceso seguro a la línea de consola.
~~~
configure terminal
line console 0
password letmein
login
exit
exit
~~~
**¿Por qué se requiere el comando login?** Para establecer que el acceso por consola tenga que ser validado mediante la contraseña que hemos introducido justo antes.

#### Paso 3: Verifique que el acceso a la consola sea seguro.
~~~
exit
## (Introducir contraseña, letmein)
~~~

#### Paso 4: Proporcionar un acceso seguro al modo privilegiado.
~~~
enable
configure terminal
enable password c1$c0
exit
~~~

#### Paso 5: Verificar que el acceso al modo privilegiado sea seguro.
~~~
exit
## (Introducir contraseña, letmein)
enable
## (Introducir contraseña, c1$c0)
show running-config
~~~

#### Paso 6: Configure una contraseña encriptada para proporcionar un acceso seguro al modo privilegiado.
~~~
config t
enable secret itsasecret
exit
~~~

#### Paso 7: Verifique si la contraseña de enable secret se agregó al archivo de configuración.
~~~
show run
~~~

**¿Qué se muestra como contraseña de enable secret?** $1$mERr$9GE1HCCTqsIl0lu/cbmD1

**¿Por qué la contraseña de enable secret se ve diferente de lo que se configuró?** Porque ha sido encriptada mediante un hash md5.

#### Paso 8: Encriptar las contraseñas de consola y de enable.
~~~
config t
service password-encryption
exit
~~~

**Si configura más contraseñas en el switch, ¿se mostrarán como texto no cifrado o en forma cifrada en el archivo de configuración? Explique.** Se mostrarán como texto cifrado, ya que `service password-encryption` encripta las contraseñas que están en el archivo de configuración, sean presentes o futuras.

### Parte 3: Configurar un aviso de MOTD
#### Paso 1: Configure un aviso de mensaje del día (MOTD).
~~~
config t
banner motd "This is a secure system. Authorized Access Only! (Este es un sistema de seguridad. Acceso autorizado únicamente)"
~~~

**1. ¿Cuándo se muestra este aviso?**
Antes de intentar iniciar sesión para entrar en el modo usuario.

**2. ¿Por qué todos los switches deben tener un aviso de MOTD?** Para informar que solo el personal autorizado debe intentar obtener acceso al dispositivo, y que en caso de hacerlo sin estar autorizado puede suponer una infracción legal. O para enviar mensajes al personal autorizado.

### Parte 4: Guardar los archivos de configuración en la NVRAM
#### Paso 1: Verifique que la configuración sea precisa mediante el comando show run.
~~~
show run
~~~

#### Paso 2: Guardar el archivo de configuración.
~~~
copy running-config startup-config
~~~
**¿Cuál es la versión abreviada más corta del comando copy running-config startup-config?** `cop run star`


#### Paso 3: Examine el archivo de configuración de inicio.
**¿Qué comando muestra el contenido de la NVRAM?** `show startup-config`

**¿Todos los cambios realizados están grabados en el archivo?** Si

### Parte 5: Configurar el S2
#### Configure el S2 con los siguientes parámetros
 - **Nombre del dispositivo:** *S2* **.**
 - **Proteja el acceso a la consola con la contraseña** *letmein* **.**
 - **Configure** *c1$c0* **como la contraseña de** *enable* **y** *itsasecret* **como la contraseña de** *enable secret* **.**
 - **Configure el siguiente mensaje para aquellas personas que inician sesión en el switch**: *Authorized access only. Unauthorized access is prohibited and violators will be prosecuted to the full extent of the law* **.**
 - **Cifre todas las contraseñas de texto no cifrado.**
 - **Asegúrese de que la configuración sea correcta.**
 - **Guarde el archivo de configuración para evitar perderlo si el switch se apaga.**

~~~
enable
configure terminal
hostname S2
exit
configure terminal
line console 0
password letmein
login
exit
exit
enable
configure terminal
enable password c1$c0
exit
exit
enable
config t
enable secret itsasecret
exit
config t
banner motd "Authorized access only. Unauthorized access is prohibited and violators will be prosecuted to the full extent of the law"
service password-encryption
show run
copy running-config startup-config
~~~
