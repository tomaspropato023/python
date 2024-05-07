# EJ 12 - Estructuras Selectivas

print("Ingrese la fecha: ")
anio = int(input("Año: "))
mes = int(input("Mes: "))
dia = int(input("Día: "))

if dia > 0 and dia < 30:
    print(dia+1)
    print(mes)
    print(anio)
else:
    if mes > 0 and mes < 12:
        print("1")
        print(mes+1)
        print(anio)
    else:
        print("1")
        print("1")
        print(anio+1)