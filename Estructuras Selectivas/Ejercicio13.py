#EJ 13 - Estructuras Selectivas

velocidad1 = float(input("Ingrese la velocidad del primer vehículo: "))
velocidad2 = float(input("Ingrese la velocidad del segundo vehículo: "))
distancia = float(input("Ingrese la distancia que separa a los vehículos: "))

if velocidad1 > 0 and velocidad2 > 0:
    tiempo = distancia / (velocidad1+velocidad2)
    print(tiempo)
else:
    print("Error.")
    StopIteration