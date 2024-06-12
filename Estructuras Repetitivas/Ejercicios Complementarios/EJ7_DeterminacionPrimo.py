#EJ Complementario 7 - Estructuras Repetitivas

contador = 0
numero = int(input("Ingrese un numero: "))

for i in range(2, numero):
    if numero % i == 0:
        contador += 1
if contador == 0:
    print("El numero es primo.")
else:
    print("El numero no es primo.")