# 1erPARCIAL - SÁBADO - 12/10/24 -

    Por favor COMPLETAR:
    - NOMBRE:
    - APELLIDO:
    - Cuenta GitHub:

## (1pt.) Ejercicio 1

Generar una *lista por compresión* que contenga los números pares que sean divisibles por $3$, $5$ y $7$ (desde $0$ hasta un número limite $N$).


## (2pt.) Ejercicio 2

Escribir una función que permita *cifrar o descifrar* una cadena de caracteres. La función debe retornar la cadena de caracteres cifrada o descifrada, según sea requerido. 

El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter (excepto los espacios) se multiplica por el valor de un caracter y luego se aplica el módulo $26$ (cantidad de letras totales), para obtener un nuevo caracter. Por defecto, el valor del caracter a multiplicar es el caracter <code>'T'</code>.

*<u>Importante:</u>*
- Pensar en los parametros que los métodos/funciones reciben


## (1pt.) Ejercicio 3

Implementar una *función iterativa* que reciba $2$ enteros <code>n</code> y <code>b</code> y devuelva <code>True</code> sii <code>n</code> es potencia de <code>b</code>.

**<u>Ejemplos:</u>**
- <code>es_potencia_ite(8, 2) -> True</code>
- <code>es_potencia_ite(64, 4) -> True</code>
- <code>es_potencia_ite(70, 10) -> False</code>


*<u>Importante:</u>*
- Pensar en los parametros que los métodos/funciones reciben


## (1pt.) Ejercicio 4

Implementar una *función recursiva* que reciba $2$ enteros <code>n</code> y <code>b</code> y devuelva <code>True</code> sii <code>n</code> es potencia de <code>b</code>.

**<u>Ejemplos:</u>**
- <code>es_potencia_rec(8, 2) -> True</code>
- <code>es_potencia_rec(64, 4) -> True</code>
- <code>es_potencia_rec(70, 10) -> False</code>


*<u>Importante:</u>*
- Pensar en los parametros que los métodos/funciones reciben


## (2pt.) Ejercicio 5

Definir una clase <code>Persona</code>, la cual tenga como *atributos el nombre, el apellido la fecha de nacimiento, la dirección, el DNU y el email* de una persona.

La clase debe contener al menos los siguientes métodos:
- Métodos qur permitan actualizar los datos de la persona.
- Un método <code>age()</code> que nos devuelva la edad de la persona 'calculándolo con la fecha actual' (pista: debemos importar el módulo '<code>datetime</code>')

*<u>Importante:</u>*
- Pueden agregar más atributos y métodos, si lo consideran necesario.
- Pensar en los parametros que los métodos reciben


## (1pt.) Ejercicio 6

Modificar la clase <code>Persona</code> agregando un atributo <code>edad</code> que se calcule automaticamente cuando se instancie la clase y se actualice cada vez que se llame al método <code>age()</code> (realizar los cambios en el archivo <code>Ejercicio5.py</code>.

*<u>Importante:</u>*
- Pensar en los parametros que los métodos/funciones reciben, hay que comprobarlos?

## (2pt.) Ejercicio 7

Sobrecargar los métodos <code>\_\_str\_\_</code>, <code>\_\_eq\_\_</code>, <code>\_\_lt\_\_</code> y <code>\_\_gt\_\_</code> de la clase <code>Persona</code>.

*<u>Nota:</u> los métodos <code>\_\_lt\_\_</code> y <code>\_\_gt\_\_</code> comparan las edades de dos Personas.*

*<u>Importante:</u>*
- Pensar en los parametros que los métodos reciben, hay que comprobarlos?
