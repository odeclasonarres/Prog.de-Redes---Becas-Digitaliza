### 0.
### 1.
### 2.
### 3.

### 4. MÓDULOS, EXCEPCIONES Y STRINGS
##### Importar módulos
Para importar un módulo y usar sus entidades:
~~~
:::python
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
text.startswith()--->
text.endswith("")--->Devuelve True/False en función de si text acaba con el texto que le pasas
text.isalnum()--->Devuelve True si solo hay letras y dígitos.
text.isalpha()---> Si hay letras solo
text.isdigit()---> Si hay dígitos solo
text.islower()---> Si hay solo minúsculas
text.isupper()---> Si solo hay mayúsculas
text.isspace()---> Si solo hay espacios
text.lower()---> cambia las mayúsculas a minúsculas.
upper
swapcase
separador.join([lista de strings])
text.lstrip(texto)--->Elimina de la cadena el texto, o los espacios en blanco si no hay parámetro, al principio de la la cadena.
rstrip--->al final de la cadena.
strip--->al principio y al final de la cadena.
text.replace("original","cambio")
rfind
split

title
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

Comparaciones de strings  
~~~
Las mayúsculas son menores que las minúsculas
~~~

Ordenar listas de strings
~~~
sorted(lista de strings)---->Crea una lista nueva y la ordena.
lista de strings.sort()--->Ordena la ya existente
~~~

Castear numero a string y viceversa
~~~
str(numero)
int(12)
float(1.2)
~~~

**Comparar strings**: se determina comparando el primer carácter diferente. Cuando comparas dos cadenas de diferentes longitudes y la más corta es idéntica al comienzo de una más larga, la cadena más larga se considera mayor


### 5. PROGRAMACIÓN ORIENTADA A OBJETOS
##### Conceptos básicos
Python: enfoque procesal y de objetos.

##### Del enfoque procesal al objeto
Encapsulamiento:
  - `__nombre`: privado(sea un método o un atributo)

Contructores:
~~~
def _init_(self): <---Contructor público

def __init__(self): <---Constructor privado
~~~
##### Atributos
Se pueden crear y añadir en el constructor o en cualquier momento de la vida del objeto(variables instancia) ---> Cada objeto de una clase puede tener atributos diferentes.

Cada objeto tiene un diccionario(`__dict__`) en en el que recogen los nombres y valores de sus atributos.

_Cómo se añaden atributos fuera del constructor_: Fijando el valor del nuevo atributo.
  - Con un método en la propia clase. En este caso será un atributo de la clase(aunque no todos los objetos lo tengan)

~~~
def setAtributo(self,val=2):
      self.atributoNuevo = val
~~~
  - Directamente
~~~
objeto.atributoNuevo=valor
~~~

*Variables de clase*: Variables comunes a todos los objetos de la clase


*Comprobar la existencia de un atributo*

El acceso a un atributo que no tiene un objeto concreto causa una excepción AttributeError .

Función `hasattr(objeto,'nombreatributo')`: retorna un booleano. También puede operar en clases.


##### Métodos
Todos los métodos tienen que tener el parámetro self. En `_dict__` también están.

`__module__` indica donde está definida una clase.

*Introspección*: Capacidad de un programa para examinar el tipo o las propiedades de un objeto en tiempo de ejecución.

*Reflexión*: Capacidad de un programa para manipular los valores, propiedades y / o funciones de un objeto en tiempo de ejecución.

`__str__()`: sobreescribirlo

##### Herencia
La herencia es la práctica de pasar atributos y métodos de la superclase (definida y existente) a una clase recién creada, llamada subclase.

En el constructor invocar explicitamente el constructor de la superclase
~~~
class SubClase(SuperClase):
  def __init__(self):
    SuperClase.__init__(self)
    self.atributopropio=valor
~~~

Función `issubclas(subclase, superclase)`: booleano si se cumple la relación. Cada clse se considera subclase de si misma

Función `isinstance(objeto, clase)`

Operador `is`: si dos variables identifican al mismo objeto.

Función `super())`

*Herencia múltiple*:
~~~
class SubClase(SuperClase1, SuperClase2):
~~~
¿Conflicto entre nombres? la subclase se queda con la que esté primero en su definición

*Composición*: proyecta una clase como un contenedor capaz de almacenar y usar otros objetos (derivados de otras clases) donde cada uno de los objetos implementa una parte del comportamiento de una clase deseada

`__bases__`

##### Excepciones
try-except-else-finally
~~~
~~~
##### Generadores y cierres
Un generador de Python es una pieza de código especializado capaz de producir una serie de valores y controlar el proceso de iteración.

yield


##### Procesando archivos
Superclase IOBase
 - TextIOBase
 - BufferedIOBase
 - RawIOBase

**Apertura de flujos**
~~~
steam = open(file, mode, encoding)
~~~
Tipos de mode:
  - *r*: lectura. el archivo tiene que existir
  - *w*: escritura. el archivo asociado con el flujo no necesita existir ; Si no existe se creará, si existe, se borrará lo anterior
  - *a*: añadir. como escribir pero sin borrar lo que había previamente
  - *r+*: leer y actualizar. el archivo asociado con el flujo debe existir y debe poder escribirse; de ​​lo contrario, la función open () genera una excepción.
  - *w+*: escribir y actualizar. el archivo asociado con el flujo no necesita existir ; Si no existe se creará; El contenido anterior del archivo permanece intacto.
  - *b*/*t* al final del modo: binario / texto. Si no se espeficica, por defecto es texto.


**Flujos preabiertos**: importados del módulo sys.
  - *sys.stdin*(entrada estándar): se asocia con el teclado, se abre antes de leer y se considera la fuente de datos principal para los programas en ejecución.
  - *sys.stdout*(salida estándar): se asocia con la pantalla, antes de abrir para escritura, considerada como el objetivo principal para la salida de datos por el programa en ejecución
  - *sys.stderr*(salida de error estándar): se asocia con la pantalla, antes de abrirla para escribir, y se considera el lugar principal donde el programa en ejecución debe enviar información sobre los errores encontrados durante su trabajo

**Cierre de flujos**
~~~
stream.close()
~~~
genera una excepción IOError en caso de error

**Diagnosticar problemas de flujo**
El objeto IOError tiene un atributo errno que identifica el código de error.
Hay muchas opciones de error, para facilitar el diagnóstico:
  - `strerror()`: del módulo os. Al pasarle un código de error devuelve una cadena con el significado.

**Archivos de texto**
 - *Codificación del texto*: utf-8
 - Son iterables
 - *Leer carácteres del archivo*: read(cantidad). Lee la cantidad de caracteres que le pases, si no se le pasa nada, se lee entero. Si no hay nada que leer, devuelve cadena vacía.
~~~
try:
      stream = open(file, "rt")
      texto = stream.read()
      stream.close()
except IOError as e:
      ...
~~~
 - *Leer filas del archivo*: readline(). Lee línea a línea del archivo.
 - *Escribir*:
~~~
try:
      stream = open(file,"wt")
      stream.write("xxxxxxx")
      stream.close()
except IOError as e:
      ...
~~~

**Archivos binarios**
 - *bytearray*: una de las clases especializadas que Python utiliza para almacenar datos amorfos. Los datos amorfos son datos que no tienen una forma específica, son solo una serie de bytes. En el caso de los bytearray, enteros con valor entre 0 y 255.
 - *Escribir bytes en el flujo*:write(bytearray que sea)
~~~
data=bytearray(10)
try:
	    bf = open('file.bin', 'wb')
        bf.write(data)
	    bf.close()
except IOError as e:
      ...
~~~
 - *Leer bytes del flujo*:readinto()
~~~
data = bytearray(10)
try:
	   bf = open('file.bin', 'rb')
	   bf.readinto(data)
	   bf.close()
except IOError as e:
     ...
~~~
