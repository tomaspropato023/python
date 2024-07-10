filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

matriz = []

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        element = int(input(f"Ingrese un valor para la posicion [{i}][{j}]: ".format(i,j)))
        matriz[i].append(element)

print(matriz)