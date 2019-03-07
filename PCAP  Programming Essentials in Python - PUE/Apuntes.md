

### 4. Módulos
##### Importar módulos
Para importar un módulo y usar sus entidades:
~~~
import modulo
print(modulo.entidad)
~~~

Para importar solo algunas entidades de un módulo y usarlas(sin tener que hacer referencia al módulo):
~~~
from modulo import entidad
print(entidad)
~~~

Para importar todas las entidades de un módulo:
~~~
from modulo import *
~~~

Si importas entidades, puedes reescribirlas
~~~
from math import pi
print(pi) ###Imprimirá 3.141592653589793
pi=3
print(pi) ###Imprimirá 3
~~~

Importar con un alias. Tanto un módulo como una entidad
~~~
import modulo as alias
print(alias.entidad)
################
from  modulo import entidad as alias
print(alias)
~~~

La función dir() lista las entidades de un módulo:
~~~
import modulo
dir(modulo)
~~~

##### Módulos y paquetes
¿Cómo convertir un conjunto de módulos jerarquizados en un paquete? Creando un archivo `__init.py__` en cualquiera de las carpetas del paquete. Además hay que añadirlo a las rutas en las que Python lo busca.
~~~
from sys import path
path.append('..\\modulos')
~~~

##### Errores
Para capturar errores usaremos excepciones. Tipos de excepciones
~~~
ZeroDivisionError: division by zero
IndexError: list index out of range

~~~

Try-catch
~~~

~~~
