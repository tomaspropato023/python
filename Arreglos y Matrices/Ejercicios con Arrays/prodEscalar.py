v1 = []
v2 = []

def productoEscalar(vector1, vector2):
    resultado = 0
    for i in range(len(vector1)):
        valor = vector1[i] * vector2[i]
        resultado += valor
    return resultado

def cargaVectores(vector, cantidad):
    for i in range(cantidad):
        elemento = int(input(f"Ingrese un elemento para la posición {i}: "))
        vector.append(elemento)
    return vector

dimension = int(input("Ingrese la dimensión de los arreglos: "))


cargaVectores(v1, dimension)
print(v1)
cargaVectores(v2, dimension)
print(v2)

print(f"El resultado es: {productoEscalar(v1, v2)}")