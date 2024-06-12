#EJ Complementario 10
import math

print("Ingrese los valores del primer punto.")
x1 = float(input())
y1 = float(input())
z1 = float(input())

print("Ingrese los valores del segundo punto.")
x2 = float(input())
y2 = float(input())
z2 = float(input())

distancia = math.sqrt((z2-z1)**2+(y2-y1)**2+(x2-x1)**2)
print("La distancia entre los dos puntos es:",distancia)