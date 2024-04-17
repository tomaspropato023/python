# Ejercicio 5

print("-----------------------------------------")
print("Ejercicio 5: Micro discos")
print("-----------------------------------------")

print("Ingrese la cantidad de GB del disco duro: ")
GB = float(input())

MG = GB * 1024
MD = MG / 1.44

print("\nSALIDA: ")
print("-----------------------------------------------------")
print(MD)
print("Se necesitan ", round(MD)," para hacer una copia de seguridad")