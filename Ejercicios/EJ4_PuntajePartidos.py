# Ejercicio 4
print("Ejercicio 4: Puntaje total de Partidos")

print("Ingrese el numero de partidos ganados: ")
PG = int(input())
print("Ingrese el numero de partidos empatados: ")
PE = int(input())
print("Ingrese el numero de partidos perdidos: ")
PP = int(input())

PPG = PG * 3
PPE = PE * 1
PPP = PP * 0

PT = PPG+PPE+PPP

print("\nSalida: ")
print("-------------------------------")
print("El puntaje total es ", PT)