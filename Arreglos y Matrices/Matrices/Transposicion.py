matriz = [[7, 2, 11], 
         [9, 1, 27],
         [18, 16, 2]]
matrizTranspuesta = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matrizTranspuesta[j][i] = matriz[i][j]
print(matrizTranspuesta)