switcher = {
    1: "Medalla de oro",
    2: "Medalla de plata",
    3: "Medalla de bronce"
}

posicion = int(input("Indique la posición del competidor: "))
posicionLlegada = switcher.get(posicion, "Mención de participación.")
print(posicionLlegada)