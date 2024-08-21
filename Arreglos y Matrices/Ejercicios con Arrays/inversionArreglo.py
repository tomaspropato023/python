arreglo = []

def cargaVectores(vector, cantidad):
    for i in range(cantidad):
        elemento = int(input(f"Ingrese un elemento para la posición {i}: "))
        vector.append(elemento)
    return vector

def inversionVectores(vector, cantidad):
    aux = 0
    indiceIzq = 0
    indiceDer = cantidad - 1
    while indiceIzq < indiceDer:
        aux = vector[indiceIzq]
        vector[indiceIzq] = vector[indiceDer]
        vector[indiceDer] = aux
        indiceIzq += 1
        indiceDer -= 1
    return vector

dimension = int(input("Ingrese la dimensión del arreglo: "))

cargaVectores(arreglo, dimension)
print(arreglo)
inversionVectores(arreglo, dimension)
print(arreglo)
