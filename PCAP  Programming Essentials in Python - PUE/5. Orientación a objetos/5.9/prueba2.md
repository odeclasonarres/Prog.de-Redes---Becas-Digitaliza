ord(caracter)--->valor ASCII/
Lee la cantidad de caracteres que le pases, si no se le pasa nada, se lee entero.

Al pasarle un código de error devuelve una cadena con el significado.
En un lugar de la mancah de cuyo nombre no quero acordarme


5.9.5 Tratando con archivos de texto


Otro método, que trata el archivo de texto como un conjunto de líneas, no de caracteres, es readlines () .

El método readlines () , cuando se invoca sin argumentos, intenta leer todo el contenido del archivo y devuelve una lista de cadenas, un elemento por línea de archivo.

Si no está seguro de que el tamaño del archivo sea lo suficientemente pequeño y no quiera probar el sistema operativo, puede convencer al método readlines () de que no lea más de un número especificado de bytes a la vez (el valor de retorno sigue siendo el mismo). - Es una lista de una cadena).

El tamaño máximo de búfer de entrada aceptado se pasa al método como su argumento.

Puede esperar que readlines () pueda procesar el contenido de un archivo con mayor eficacia que readline () , ya que es posible que deba invocarse menos veces.



Nota: cuando no hay nada que leer del archivo, el método devuelve una lista vacía. Úsalo para detectar el final del archivo.



En la medida del tamaño del búfer, puede esperar que su aumento pueda mejorar el rendimiento de entrada, pero no hay una regla de oro para ello: intente encontrar los valores óptimos usted mismo.

Hemos modificado el código para mostrarle cómo usar readlines () →



Hemos decidido utilizar un búfer de 15 bytes. No creo que sea una recomendación.

Hemos utilizado este valor para evitar la situación en la que la primera invocación de readlines () consume todo el archivo.

Queremos que el método se vea obligado a trabajar más duro y demostrar sus capacidades.



Hay dos bucles anidados en el código: el externo usa el resultado de readlines () para iterarlo, mientras que el interno imprime las líneas carácter por carácter.

 
