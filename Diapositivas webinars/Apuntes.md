## Sesión 1.
## Sesión 2.
## Sesión 3.
## Sesión 4.
## Sesión 5.

## Sesión 6. Contextualización de SDN y Programación de Redes

##### 1. Evolución de las Redes
Redes físicas--->Lenguajes de programación--->Ciberseguridad

##### 2. ¿Por qué SDN?
La topología actual, diversa, surge de dos problemáticas:
  - **Gestión de las redes**: pese a la diversidad de técnicas, no eran óptimas para tanta infraestructura cambiante al ser manuales.
  - **Inestabilidad de las redes**: Las rutas dinámicas se cargan la estabilidad, teniendo que hacer ajustes continuos, para monitorizar parámetros y reaccionar.

Como solución surge SDN(Software Define Networks, redes definidas por software): la idea es separar el plano del control(lógica de análisis de los datos) del plano de los datos(envío de los datos); ¿cómo? añadiendo controlador en la red(servidor con visión general y que establece ajustes y configuraciones en la red). Beneficios:
 - La mayor parte de las configuraciones de la red se realizan en el controlador, reduciendo el proceso repetitivo de hacerlo a mano.
 - En el lado del cliente no hay que modificar nada, se implementa OpenFlow.

 Plano de datos y de control:
 - *Plano de datos*(capa de infraestructura): efectuar el envío de datos en si. (elementos de la red)
   - *D-CPI*(Data-controller plane interface): Comunica los dispositivos con el controlador con una interfaz(southboud interface). Por lo generalmediante el protocolo OpenFlow.
 - *Plano de control*(capa de control): el objetivo es tomar decisiones sobre dónde enviar los datos. (Controlador SDN)
   - *A-CPI*(Application-controller plane interface): Comunica las interfaces NBIs(northbound interfaces) con las aplicaciones SDN.
 - *Plano de aplicación*(capa de aplicación): Aplicaciones que comunican peticiones de red hacia el controlador. (Aplicaciones SDN).
[Diapositiva 21 - Sesion6 ]

##### 3. ¿Qué es OpenFlow?
Protocolo que se usa por defecto en SDN. Para cada tipo de datos tiene una regla de flujo de datos(flow table), para reducir peticiones de actuación al servidor.

29:00

##### 4. Abstracción y virtualización de redes
##### 5. Gestión de Redes
##### 6. Devnet: Introducción a APIC-EM

## Sesión 7. APIs, RESTful APIs, y respuestas en JSON y XML

##### APIC-EM
Controlador de servidor (Enterprise module)

##### APIs

##### REST APIs

##### Formato de datos y parseado
###### XML
###### JSON

##### Práctica

## Sesión 8.

## Sesión 9.
