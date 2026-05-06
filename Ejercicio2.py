#Ejercicio 2
#Escribir una función que permita cifrar o descifrar una cadena de caracteres. 
#La función debe retornar la cadena de caracteres cifrada o descifrada, 
#según sea requerido. El algoritmo de cifrado a utilizar será muy sencillo: 
##a cada caracter (excepto los espacios) se multiplica por el valor de un caracter;
##y luego se aplica el módulo 26 (cantidad de letras totales), para obtener un nuevo caracter. 
#Por defecto, el valor del caracter a multiplicar es el caracter 'T'.
#Importante:
#- Pensar en los parametros que los métodos reciben



def cifrado(frase, cifrar = True / / None): 
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    # mensaje => es frase 
    desplazamiento = 20 # = a la 'T'
    cadena_resultado = ""
    if cifrar:
        for letra in mensaje:
            if letra.lower() in alfabeto:
                indice = alfabeto.index(letra.lower())
                indice_cifrado = (indice + desplazamiento) % 26
                if letra.isupper():
                    mensaje_cifrado += alfabeto[indice_cifrado].upper()
                else:
                    mensaje_cifrado += alfabeto[indice_cifrado]
            else:
                mensaje_cifrado += letra
    else: 
        ### ALG INVERSO ##

    return cadena_resultado 

#alfabeto = "abcdefghijklmnopqrstuvwxyz"
#mensaje 
#desplazamiento = 
#cadena_resultado = ""
#for letra in mensaje:
#    if letra.lower() in alfabeto:
#        indice = alfabeto.index(letra.lower())
#        indice_cifrado = (indice + desplazamiento) % 26
#        if letra.isupper():
#            mensaje_cifrado += alfabeto[indice_cifrado].upper()
#        else:
#            mensaje_cifrado += alfabeto[indice_cifrado]
#    else:
#        mensaje_cifrado += letra