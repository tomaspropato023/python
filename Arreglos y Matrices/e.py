import random

array = []
arrayLength = int(input("Ingrese la longitud del arreglo: "))
for i in range(1, arrayLength+1):
    element = random.randint(1, 100)
    array.append(element)
array.sort(reverse=True)
print(array)
