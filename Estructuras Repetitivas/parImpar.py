num = int(input("Ingrese un numero: "))

while (num <= 0):
    num = int(input("Vuelva a ingresar un numero: "))

if num % 2 == 0:
    print("El numero es par.")
else:
    print("El numero es impar.")