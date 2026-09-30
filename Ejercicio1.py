#Ejercicio 1
#Generar una lista por compresión que contenga los números pares 
#que sean divisibles por 3, 5 y 7 (desde 0 hasta un número limite N).
def lista_pares_divisibles(N)
L = [ x for x in range(N+1) if x %2 == 0 and x  %3 == 0 and x % 5 == 0 and x % 7 == 0]
return L  