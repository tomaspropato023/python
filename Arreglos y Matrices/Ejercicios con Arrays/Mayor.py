array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
mayor = 0
for i in range(len(array)):
    if array[i] > mayor:
        mayor = array[i]
        posicion = i
print(mayor, posicion)