length = int(input("Ingrese la dimension del arreglo: "))
multiplo = int(input("Ingrese un numero: "))
array = length*[multiplo]
for i in range(length):
    array[i] = multiplo * i
print(array)