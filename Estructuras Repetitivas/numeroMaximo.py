# EJ Encontrar el numero maximo

temp = int
tempMax = 0
tempMin = 0
while (temp != 0):
    temp = int(input("Ingrese la temperatura: "))
    if (temp > tempMax):
        tempMax = temp
    if (temp < tempMin):
        tempMin = temp
print(f"La temperatura maxima es {tempMax}°C y la temperatura minima es {tempMin}°C")