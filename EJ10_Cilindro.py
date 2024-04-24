#EJ 10
import math

print("Ingrese el radio y altura del cilindro")
radio = float(input("Radio: "))
altura = float(input("Altura: "))

volumen = math.pi * radio**2 * altura
area = 2*math.pi*radio*(radio+altura)

print("El volumen del cilindro es",volumen,"y el area es de",area)