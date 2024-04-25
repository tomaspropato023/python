#EJ 10

print("Ingrese un numero: ")
num = int(input())
while num == 0:
    print ("Vuelva a ingresar un numero")
    num = int(input())
if num != 0 and num % 2 == 0:
    print("El numero es par.")
if num % 2 == 1:
    print("El numero es impar.")