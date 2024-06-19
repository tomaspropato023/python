#EJ Complementario 12 - Estructuras Repetitivas

i = 2
contadorDePares = 0
while (contadorDePares < 10):
    if (i % 2 == 0):
        cubo = i**3
        print(f"{i} / {cubo}")
        contadorDePares += 1
    i += 1