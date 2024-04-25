#EJ Complementario 7
import math

b = float(input("Ingrese el valor del segundo lado: "))
c = float(input("Ingrese el valor del tercer lado: "))
alfa = float(input("Ingrese el valor del ángulo en grados sexagesimales: "))

a = math.sqrt(b**2+c**2-2*b*c*math.cos(alfa*math.pi/180))

print("El valor del primer lado es:",a)
