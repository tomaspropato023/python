array = []
dimension = int(input("Ingrese la longitud del arreglo: "))
multiplo = int(input("Ingrese un numero: "))
for i in range(1, dimension+1):
    numero = multiplo * i
    array.append(numero)
print(array)