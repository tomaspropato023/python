#EJ 2 - Arreglos y Matrices

suma = 0
media = 0
contador = 0
arregloTemperaturas = []
for i in range (1, 11):
    temperatura = float(input("Ingrese la temperatura: "))
    arregloTemperaturas.append(temperatura)
    suma += temperatura

media = suma / len(arregloTemperaturas)
for tempElement in arregloTemperaturas:
    if tempElement >= media:
        contador += 1
        print(f"{tempElement} es mayor a la media")

print(f"La media es {media}")
print(f"El total de temperaturas mayores o iguales a la media es {contador}")