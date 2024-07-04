array = []
dimension = int(input("Ingrese la dimension del arreglo: "))
negativos = 0
for i in range(1, dimension+1):
    numero = int(input("Ingrese un numero: "))
    array.append(numero)

for i in range(len(array)):
    if array[i] < 0:
        negativos += 1
        print(f"{array[i]} es negativo")

print(f"Hay {negativos} numeros negativos en el arreglo")