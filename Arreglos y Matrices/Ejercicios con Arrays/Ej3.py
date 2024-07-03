array = []
suma = 0
for i in range(1, 11):
    element = int(input(f"Ingrese un valor para la posicion {i}: "))
    array.append(element)
    suma += element
media = suma / len(array)
print(f"La media es {media}")