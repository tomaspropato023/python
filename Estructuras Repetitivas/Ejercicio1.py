#EJ 1 - Estructuras Repetitivas

capital = -1
interes = 0
tiempo = 0

while capital < 0 or interes <= 0 or interes >= 100 or tiempo <= 0:
    print("Introduzca el capital, interes y tiempo apropiados: ")
    capital = int(input())
    interes = int(input())
    tiempo = int(input())

for i in range (tiempo):
    capital = capital * (1 + interes/100)

print(f"Usted tiene ${capital} pesos.")