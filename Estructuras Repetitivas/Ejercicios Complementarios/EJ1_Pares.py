#EJ Complementario 1 - Estructuras Repetitivas

contador = 0

for i in range (1, 101):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        contador += 1


print(f"Hay {contador} numeros pares.")