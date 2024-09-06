filas = 20
butacas = 3
colectivo = [[0 for _ in range(butacas)] for _ in range(filas)]

def imprimirMatriz(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

def compraPasaje():
    posX = -1
    posY = -1
    imprimirMatriz(colectivo)
    while (posX < 0 or posX > filas) & (posY < 0 or posY > butacas): 
        posX = int(input("¿Qué fila quiere? "))
        posY = int(input("¿Cuál butaca quiere? "))
    comprobarAsiento(posX, posY)

def comprobarAsiento(posicionX, posicionY):
    for i in range(filas):
        for j in range(butacas):
            if (i == posicionX) & (j == posicionY):
                if colectivo[i][j] == 0:
                    colectivo[i][j] = 1
                    print("Gracias por su compra!")
                    compraPasaje()
                else:
                    print("Asiento ocupado.")
                    compraPasaje()

compraPasaje()