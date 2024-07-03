arreglo1 = []
arreglo2 = []
sumaDeArreglo = 0

dimensionArreglos = int(input("Ingrese la dimensión de los arreglos: "))
for i in range(1, dimensionArreglos+1):
    valor = int(input(f"Ingrese un valor para la posición {i} en el arreglo 1: "))
    arreglo1.append(valor)
for j in range(1, dimensionArreglos+1):
    valor = int(input(f"Ingrese un valor para la posicion {j} en el arreglo 2: "))
    arreglo2.append(valor)

i = 0
sumaDeArreglo = [arreglo1[i] + arreglo2[i] for i in range(len(arreglo1))]
print(sumaDeArreglo)