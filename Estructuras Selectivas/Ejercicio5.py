#EJ 5 - Estructuras Selectivas

anio = int(input("Ingrese un año: "))
if (anio % 400 == 0) or (anio % 4 == 0) and (anio % 100 != 0):
    print ("El año es bisiesto.")
else:
    print ("El año no es bisiesto.")