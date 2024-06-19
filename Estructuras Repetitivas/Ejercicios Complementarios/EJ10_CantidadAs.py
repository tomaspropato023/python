#EJ Complementario 10 - Estructuras Repetitivas

cantidadDeAs = 0
for i in range(1, 51):
    letras = input("Ingrese los caracteres: ")
    if (letras.casefold() == "a"):
        cantidadDeAs += 1
print(f"En 50 caracteres hay {cantidadDeAs} caracteres 'A'")