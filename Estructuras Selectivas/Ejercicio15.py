#EJ 15 - Estructuras Selectivas

print("Ingrese los valores de la función cuadrática: ")
num1 = float(input())
num2 = float(input())
num3 = float(input())

discriminante = num2**2 - 4*(num1*num3)
if discriminante > 0:
    raiz1 = ((-num2) + discriminante ** 0.5)/2*num1
    raiz2 = ((-num2) - discriminante ** 0.5)/2*num1
    print("Raices reales:", raiz1, raiz2)
else:
    print("Raices irracionales.")