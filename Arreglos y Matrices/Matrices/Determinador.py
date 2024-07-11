matriz = []
determinador = 0
for i in range(2):
    matriz.append([])
    for j in range(2):
        element = int(input(f"Ingrese el valor para la posicion [{i}][{j}]: ".format(i,j)))
        matriz[i].append(element)

determinador = (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
print(determinador)