#EJ 8
print("Ingrese el mes: ")
mes = str(input())
print("Ingrese el valor de la compra: ")
compra = int(input())
descuento = 0.85
if mes == "octubre":
    print("Tiene un descuento del 15%. El valor total de la compra es $",(compra*descuento))
else:
    print("El valor total es $",compra)