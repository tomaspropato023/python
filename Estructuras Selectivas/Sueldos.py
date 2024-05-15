sueldo = int(input("Ingrese su salario actual: "))
if sueldo > 0 and sueldo <= 15000:
    sueldo *= 1.2
    print("Tiene un aumento del 20%. Su salario pasa a ser de $",sueldo)
elif sueldo >= 15001 and sueldo <= 20000:
    sueldo *= 1.1
    print("Tiene un aumento del 10%. Su salario pasa a ser de $",sueldo)
elif sueldo >= 20001 and sueldo <= 25001:
    sueldo *= 1.05
    print("Tiene un aumento del 5%. Su salario pasa a ser de $",sueldo)
else:
    print("No tiene aumento. Su salario sigue siendo de $", sueldo)
    