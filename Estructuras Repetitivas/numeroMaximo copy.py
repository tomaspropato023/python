# EJ Encontrar el numero maximo

temp = int
tempMax = 0
tempMin = 0
numerosPositivos = 0
numerosNegativos = 0
contador = 0
while (temp != 0):
    temp = int(input("Ingrese la temperatura: "))
    if (temp > tempMax):
        tempMax = temp
    if (temp < tempMin):
        tempMin = temp
    if (temp > 0):
        numerosPositivos += 1
    elif (temp < 0):
        numerosNegativos += 1

contador = numerosPositivos + numerosNegativos
print(f"La temperatura maxima es {tempMax}°C y la temperatura minima es {tempMin}°C")
print(f"Hay {numerosPositivos} numeros positivos, y equivale a un",((numerosPositivos/contador)*100),"% del total")
print(f"Hay {numerosNegativos} numeros negativos, y equivale a un",((numerosNegativos/contador)*100),"% del total")