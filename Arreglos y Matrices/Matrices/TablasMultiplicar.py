limite = int(input("Ingrese hasta que tabla quiera imprimir: "))
matriz = [[1 for _ in range(limite)] for _ in range(limite)]

for i in range(0, limite):
    multiplicador = 1; indice = i+1
    for j in range(0, limite):
        matriz[i][j] *= indice*multiplicador
        multiplicador += 1
        

for i in matriz:
    aux = i[0]
    print(f"Tabla del {aux}: ", end="[ ")
    for j in i:
        print(j, end=" ")
    print("]", end="")
    print()
