def calculoPotencia (base, exponente):
    if exponente == 0:
        return 1
    else:
        return (base**exponente)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = calculoPotencia(base, exponente)

print(f"El resultado es: {resultado}")