costoArt = float(input("Ingrese el precio del artículo: "))
marca = str(input("Ingrese la marca del producto: "))

if (costoArt >= 2000) and (marca == "NOSY"):
    precioAparato = costoArt * 0.9
    precioTotal = precioAparato * 0.95
elif (costoArt >= 2000) and (marca != "NOSY"):
    precioTotal = costoArt * 0.9
elif (costoArt < 2000) and (marca == "NOSY"):
    precioTotal = costoArt * 0.95
elif (costoArt < 2000) and (marca != "NOSY"):
    precioTotal = costoArt
precioTotal *= 1.2
print("Usted pagará $",precioTotal)