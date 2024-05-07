# EJ 6 - Estructuras Selectivas

print("Ingrese los valores: ")
NUM = int(input("Tipo de Cálculo: "))
V = int(input("Ingrese V: "))

funcion  = {
    1: 100*V,
    2: 100**V,
    3: 100/V,
}

VAL = funcion.get(NUM, 0)

print("\nSALIDA: ")
print("-------------------------------------------------------")
print(VAL)