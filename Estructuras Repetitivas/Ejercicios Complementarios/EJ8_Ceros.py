#EJ Complementario 8 - Estructuras Repetitivas

cantidadNumeros = int(input("Ingrese la cantidad de numeros: "))
contadorCeros = 0
for i in range (1, cantidadNumeros+1):
    numeros = int(input("Ingrese los numeros: "))
    if numeros == 0:
        contadorCeros += 1

print(f"Hay {contadorCeros} ceros")