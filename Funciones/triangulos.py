def calculoArea(base, altura):
    area = (base*altura)/2
    return area

def calculoTriangulos():
    resultado = 0
    for i in range(1, 100+1):
        resultado = calculoArea(i, i*2)
        print(f"El resultado es: {resultado}")

calculoTriangulos()