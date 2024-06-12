#EJ Complementario 2 - Estructuras Repetitivas

cubo = 0
MINIMO = 2
MAXIMO = 20
PASO = 2
for i in range (MINIMO, MAXIMO+1, PASO):
    cubo = i**3
    print(f"El cubo de {i} es: {cubo}.")