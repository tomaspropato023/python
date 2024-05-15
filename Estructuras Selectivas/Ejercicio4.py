#EJ 4 - Estructuras Selectivas

sueldo = float(input("Ingrese su sueldo: "))
if sueldo < 1000:
    aumento = sueldo * 0.15
    sueldo += aumento
print("Su sueldo es $",sueldo)