#EJ 3 - Arreglos y Matrices

limiteArreglo = int(input("Ingrese el limite del arreglo: "))
vector = []
if (1 <= limiteArreglo) and (limiteArreglo <= 200):
    for i in range(1, limiteArreglo+1):
        elemento = int(input(f"Ingrese un numero para la posicion {i}: "))
        vector.append(elemento)
else:
    print("El numero de elementos en el vector es incorreto.")
    exit

i = 0

arregloOrdenado = []

for elemento in vector:
    if elemento not in arregloOrdenado:
        arregloOrdenado.append(elemento)

arregloOrdenado.sort()

print("El arreglo ordenado es: ")
print(arregloOrdenado)
