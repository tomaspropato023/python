#EJ 4 - Arreglos y Matrices

arreglo1 = []
arreglo2 = []
sumaArreglos = []
print("Ingrese la dimension de la matriz, con un maximo de 100")
filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

for i in range (filas):
    arreglo1.append( [] )
    arreglo2.append( [] )
    sumaArreglos.append( [] )
    for j in range (columnas):
        arreglo1[i].append(int(input("A({})({}): ".format(i+1,j+1))))
        arreglo2[i].append(int(input("B({})({}): ".format(i+1,j+1))))
        sumaArreglos[i].append(arreglo1[i][j] + arreglo2[i][j])

print(arreglo1)
print(arreglo2)
print(sumaArreglos)