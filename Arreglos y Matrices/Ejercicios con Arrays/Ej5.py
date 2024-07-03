array1 = []
array2 = []
dimensionArreglos = int(input("Ingrese la dimensión de los arreglos: "))
for i in range(1, dimensionArreglos+1):
    nombre = str(input("Ingrese un nombre: "))
    longitudNombre = len(nombre)
    array1.append(nombre)
    array2.append(longitudNombre)

for i in range(dimensionArreglos):
    print(array1[i], "=", array2[i])