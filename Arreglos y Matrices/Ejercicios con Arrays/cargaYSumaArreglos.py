v1 = []
v2 = []
suma = []

def cargaVectores(vector, cantidad):
    for i in range(cantidad):
        elemento = int(input(f"Ingrese un elemento para la posición {i}: "))
        vector.append(elemento)
    return vector

def sumaVectores(vector1, vector2, sumaVectores):
    for i in range(len(vector1)):
        sumar = vector1[i] + vector2[i]
        sumaVectores.append(sumar)
    return sumaVectores

cantidad = int(input("Ingrese la dimensión de los vectores: "))
cargaVectores(v1, cantidad)
print(v1)
cargaVectores(v2, cantidad)
print(v2)
sumaVectores(v1, v2, suma)
print(suma)