#EJ Complementario 13 - Estructuras Repetitivas

cantidadEmpleados = int(input("Ingrese la cantidad de empleados: "))
i = 1
sueldoMayor = 0
for i in range (1, cantidadEmpleados+1):
    sueldo = float(input("Ingrese los sueldos de los empleados: "))
    if (sueldo > sueldoMayor):
        sueldoMayor = sueldo
        numeroOrden = i

print(f"El empleado N°{numeroOrden} tiene el mayor sueldo, el cual es ${sueldoMayor}")