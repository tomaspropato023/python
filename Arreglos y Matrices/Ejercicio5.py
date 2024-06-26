#EJ 5 - Arreglos y Matrices
# ??
matriz = []
dimensionMatriz = int(input("Ingrese la dimensión de las matrices: "))

if (1 <= dimensionMatriz) and (dimensionMatriz <= 100):
    for i in range(dimensionMatriz):
        matriz.append( [] )
        for j in range(dimensionMatriz):
            elemento = input(" A[{}][{}]: ".format(i,j))
            matriz[i].append(int(elemento))
    BAND = True
    i = 0
    while (i < dimensionMatriz) and (BAND == True):
        j = 0
        while (j < i) and (BAND == True):
            if matriz[i][j] == matriz[j][i]:
                j += 1
            else:
                BAND = False
        i += 1
    if BAND == True:
        print("SIMETRICA")
    else:
        print("ASIMETRICA")
else:
    print("Dimension incorrecta")