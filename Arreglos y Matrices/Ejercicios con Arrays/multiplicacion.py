v1 = [1, 2, 3]
v2 = [4, 5, 6]
v3 = [2, 1, 2]
v4 = [1, 2, 1]

def multiplicarArreglo(arreglo1, arreglo2, arreglo3, arreglo4):
    vResultado = []
    for i in range(len(arreglo1)):
        producto = arreglo1[i] * arreglo2[i] * arreglo3[i] * arreglo4[i]
        vResultado.append(producto)
    return vResultado

print(multiplicarArreglo(v1, v2, v3, v4))