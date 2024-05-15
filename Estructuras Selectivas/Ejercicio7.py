# EJ 7 - Estructuras Selectivas

num = int(input("Ingrese un numero del 1 al 10: "))

if num > 0 and num <= 10:
    if num % 2 == 0:
        print("El numero es par.")
    else:
        print("El numero es impar")
else:
    print("Fuera de rango.")