#EJ Complementario 3 - Estructuras Repetitivas

b = 2

for i in range(1, 29):
    contador = 0
    for x in range(2, b//2):
        if b % x == 0:
            contador += 1
            x = b
    if contador == 0:
        print(f"El cubo de {b} es {b**3}.")
    b += 1