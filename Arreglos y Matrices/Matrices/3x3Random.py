import random as r

filas = 3
columnas = 3

matriz = []

for i in range(filas):
    matriz.append( [] )
    for j in range(columnas):
        numero = r.randint(0, 9-1)
        matriz[i].append(numero)


for i in matriz:
    print("[", end=" ")
    for j in i:
        print(j, end=' ')
    print("]")