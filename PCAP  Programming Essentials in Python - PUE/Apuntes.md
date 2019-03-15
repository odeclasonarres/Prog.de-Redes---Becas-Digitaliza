### 0.
### 1.
### 2.
### 3.

### 4. Módulos, excepciones y strings
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

##### Errores y excepciones
Para capturar errores usaremos excepciones. 63 tipos de excepciones jerarquizadas. En caso de elegir se queda con la primera que encuentre que valga para ese caso(incluso si hay otras más concretas)----> Hay que poner las excepciones concretas antes que las más generales.

Try-except
~~~
try:
   :
   :
   :
except:
   :
   :
   :
~~~

Manejar dos excepciones a la vez
~~~
try:
   :
   :
except(exc1,exc2):
   :
   :
~~~

Podemos dejar que una función retorne una excepción para manejarla fuera de la misma, o incluso en otro módulo en busca de la cláusula que la maneje.

**raise**: palabra reservada que "fuerza" una excepción, de cara a probar sin tener que buscar ejemplos de ejecución. Ejemplo:
~~~
def badfun(n):
	raise ZeroDivisionError

try:
	badfun(0)
except ArithmeticError:
	print('What did you do?')
print('THE END')
~~~

**assert**: evalúa una expresión, si es verdadera, un valor numérico distinto de cero, una cadena no vacía o cualquier otro valor distinto a None, no hará nada; de lo contrario, genera una excepción AssertionError


Tipos de excepciones útiles:
~~~
BaseException: la más general
Exception: incluye todas las excepciones causadas por errores resultado de un mal funcionamiento del código.
    BaseException ← Exception
IndexError:list index out of range
    BaseException ← Exception ← LookupError ← IndexError
ArithmeticError:excepciones causadas por operaciones aritméticas  
    BaseException ← Exception ← ArithmeticError
ZeroDivisionError: division by zero
    BaseException ← Exception ← ArithmeticError ← ZeroDivisionError
OverflowError: una operación produce un número demasiado grande para poder almacenarlo.
    BaseException ← Exception ← ArithmeticError ← OverflowError
AssertionError:
ImportError: cuando falla una importación.
  BaseException ← Exception ← StandardError ← ImportError
LookupError:incluye todas las excepciones causadas por errores resultantes de referencias no válidas a diferentes colecciones (listas, diccionarios, tuplas, etc.)
    BaseException ← Exception ← LookupError
KeyError:
  BaseException ← Exception ← LookupError ← KeyError: excepción concreta provocada cuando intenta acceder a un elemento de colección no existente.
MemoryError: se genera cuando una operación no se puede realizar por falta de memoria
    BaseException ← Exception ← MemoryError
KeyboardInterrupt:el usuario interrumpe la ejecución con atajos de teclado.
    BaseException ← KeyboardInterrupt    
~~~

##### Strings
~~~
len(cadena)--->devuelve la longitud, puede ser 0(vacía)
\--->Caractecter de escape(para poner delante de ').
'''xxxxxxxx'''--->Cadenas multilínea
+--->Concatenado de cadenas. Se puede sobrecargar.
*--->replicado. Se puede sobrecargar.
ord(caracter)--->valor ASCII/UNICODE de un carácter específico
chr(numero)--->devuelve un caracter
min(cadena)--->devuelve el carácter con menos valor de la cadena
max(cadena)--->devuelve el de más valor
text.index('x')--->devuelve la posición en la que está x, si no está-->ValueError
text.find("texto")---> similar a index pero sin posibilidad de errores.
list('texto')--->Crea una lista con los carácteres de texto como elementos.
text.count('x')--->devuelve la cantidad de veces que está x en la cadena.
text.capitalize()--->Pone la primera letra en mayúscula y el resto en minúsculas.
text.endswith("")--->Devuelve True/False en función de si text acaba con el texto que le pasas




~~~

Pueden ser tratadas como listas en muchos casos:
  - Indexación
  - Iteración
  - Aplicar el `in`----> `'f' in text`

Pero son inmutables, métodos que no funcionan:
~~~
del text[0]
text.append("assdfdfdf")
text.insert(0,"a")
~~~

¿Cómo hacer cambios?
~~~
text= "a"+text
~~~
