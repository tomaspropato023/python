sueldo = int(input("Ingrese su salario actual: "))
if sueldo > 0 and sueldo <= 15000:
    sueldoConAumento = sueldo * 1.2
    print("Tiene un aumento del 20%. Su salario pasa a ser de $",sueldoConAumento)
elif sueldo >= 15001 and sueldo <= 20000:
    sueldoConAumento = sueldo * 1.1
    print("Tiene un aumento del 10%. Su salario pasa a ser de $",sueldoConAumento)
elif sueldo >= 20001 and sueldo <= 25001:
    sueldoConAumento = sueldo * 1.05
    print("Tiene un aumento del 5%. Su salario pasa a ser de $",sueldoConAumento)
else:
    print("No tiene aumento. Su salario sigue siendo de $", sueldo)
    