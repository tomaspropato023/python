pisos = 10
departamentos = 2

edificio = [[0 for _ in range(departamentos)] for _ in range(pisos)]
totalPisos = [0 for _ in range(pisos)]
total = 0
for i in range(pisos):
    for j in range(departamentos):
        edificio[i][j] = int(input(f"Cantidad de habitantes en el departamento {i+1} del piso {j+1}: ".format(i,j)))
        total += edificio[i][j]
        totalPisos[i] += edificio[i][j]

print(edificio)
print(total)
for i in range(pisos):
    print(f"El piso {i} tiene un total de {totalPisos[i]} habitantes.")