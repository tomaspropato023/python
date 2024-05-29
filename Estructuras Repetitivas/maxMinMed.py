#EJ Maximo-Minimo-Promedio
prom = 0
contador = 0
suma = 0

num = int(input("Ingrese un numero: "))
Max = num
Min = num

while (num != 0):
    if (num > Max):
        Max = num
    if (num < Min):
        Min = num
    suma += num
    contador += 1
    num = int(input("Ingrese un numero: "))
    

prom = suma / contador

print(f"Numero maximo: {Max}")
print(f"Numero minimo: {Min}")
print(f"Media: {prom}")
