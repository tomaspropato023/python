#EJ Complementario 5 - Estructuras Repetitivas

suma = 0
terminos = int(input("Ingrese la cantidad de terminos: "))

for i in range(1, terminos+1):
    if i % 2 == 0:
        suma = suma - (1/i)
    else:
        suma = suma + (1/i)

print(f"La suma será {suma}")