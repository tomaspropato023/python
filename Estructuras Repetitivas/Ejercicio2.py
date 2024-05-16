#EJ 2 - Estructuras Repetitivas

numero = int(input("Ingrese un numero: "))

while (numero > 0):
    suma = 0

    for i in range (1, numero+1):
        if numero % i == 0:
            suma += i
    print(f"La suma de los divisores es {suma}")
    numero = int(input("Ingrese un numero negativo: "))