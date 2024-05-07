#EJ 9
num = int(input("Ingrese un numero: "))
if num == 0:
    print("El numero no es par ni impar.")
else:
    if num != 0 and num % 2 == 0:
        print("El numero es par.")
    else:
        print("El numero es impar.")