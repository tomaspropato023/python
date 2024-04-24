#EJ 6
import math

AX = int(input("Ingrese el primer valor de A: "))
AY = int(input("Ingrese el segundo valor de A: "))
BX = int(input("Ingrese el primer valor de B: "))
BY = int(input("Ingrese el segundo valor de B: "))

dist = math.sqrt((AX-BX)**2+(AY-BY)**2)

print("La distancia entre A y B es de",dist)