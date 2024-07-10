import random as r

filas = 3
columnas = 3

matriz = []

for i in range(filas):
    matriz.append( [] )
    for j in range(columnas):
        numero = r.randint(0, 10)
        matriz[i].append(numero)

print(matriz)