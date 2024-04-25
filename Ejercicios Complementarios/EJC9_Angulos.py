#EJ Complementario 9
import math

x = float(input("Ingrese el ángulo en radianes: "))
sexagesimal = x*180/math.pi
centesimal = x*200/math.pi
print(x,"en sexagesimales es",sexagesimal,"y en centesimales es",centesimal)