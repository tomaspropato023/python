# EJ Tabla Multiplicacion

numero = int(input("Ingrese un numero: "))
multiplicador = int(input("Ingrese hasta que numero desea multiplicar: "))

for i in range (1, multiplicador+1):
    print(f"{numero} x {i} =", (numero*i))
    i += 1