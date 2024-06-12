#EJ Complementario 4 - Estructuras Repetitivas

terminos = int(input("Ingrese el numero de terminos: "))
contador = 5
suma = 0

for i in range(1, terminos+1):
    contador += 5
    suma += contador

print(f"La suma de la serie es {suma}")