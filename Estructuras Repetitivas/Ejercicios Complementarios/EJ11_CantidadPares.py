#EJ Complementario 11 - Estructuras Repetitivas

contadorPares = 0
for i in range(1, 101):
    numeros = int(input("Ingrese un numero: "))
    if (numeros % 2 == 0):
        contadorPares += 1

print(f"En 100 numeros enteros hay {contadorPares} numeros pares.")