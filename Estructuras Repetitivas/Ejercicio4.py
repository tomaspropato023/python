#EJ 4 - Estructuras Repetitivas

num = int(input("Introduzca un numero: "))

while (num > 0):
    resto = num % 10
    print(resto)
    num = num // 10
