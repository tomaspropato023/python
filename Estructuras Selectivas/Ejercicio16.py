# EJ 16 - Estructuras Selectivas
import math;

opcion = int(input("Ingrese 1 para calcular el área de un triángulo, Ingrese 2 para calcular el area de un círculo: "))

if (opcion == 1):
    print("Área del triángulo: ")
    ladoTriangulo = float(input("Ingrese el lado del triángulo: "))
    areaTriangulo = (math.sqrt(3)/4) * math.pow(ladoTriangulo, 2)
    print("El área del triangulo es",areaTriangulo)
elif (opcion == 2):
    print("Área del círculo: ")
    radioCirculo = float(input("Ingrese el radio del círculo: "))
    areaCirculo = math.pi * math.pow(radioCirculo, 2)
    print("El área del circulo es",areaCirculo)
else:
    print("Error.")
    StopIteration