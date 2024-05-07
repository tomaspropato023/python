#EJ 8
compra = int(input("Ingrese el valor de la compra: "))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))
mes = str(input("Ingrese el mes de la compra: "))
precioTotal = compra * cantidad
descuento = 0.85
if mes == "octubre":
    subtotal = precioTotal * descuento
    print("Tiene un descuento del 15%. El valor total de la compra es $",subtotal)
else:
    print("El valor total es $",precioTotal)