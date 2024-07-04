array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
mayor = 0
segundoMayor = 0
for i in range(len(array)):
    if array[i] > mayor:
        mayor = array[i]
    if (array[i] > segundoMayor) and (array[i] < mayor):
        segundoMayor = array[i]
print(mayor)
print(segundoMayor)