# EJ Tabla Multiplicacion

numero = int(input("Ingrese un numero: "))
multiplicador = int(input("Ingrese hasta que numero desea multiplicar: "))

indice = 1

while (indice <= multiplicador):
    print(f"{numero} x {indice} =", numero * indice)
    indice += 1
