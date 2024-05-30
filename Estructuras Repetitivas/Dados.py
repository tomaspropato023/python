#EJ Dados

dados = int(input("Ingrese la cantidad de dados a tirar: "))

porcentaje = (1/(6**dados))*100
chance = 6**dados

print(f"Hay {porcentaje}% de probabilidades de sacar 6 en {dados} dados")
print(f"{dados}/{chance} | {porcentaje: .2f}%")