#EJ 6
import math

AX = float(input("Ingrese el primer valor de A: "))
AY = float(input("Ingrese el segundo valor de A: "))
BX = float(input("Ingrese el primer valor de B: "))
BY = float(input("Ingrese el segundo valor de B: "))

dist = math.sqrt((AX-BX)**2+(AY-BY)**2)

print("La distancia entre A y B es de",dist)