#EJ 6 - Arreglos y Matrices
montos = []

sucursales = int(input("Ingrese el numero de sucursales: "))
tiempo = int(input("Ingrese el numero de años: "))


print("------------------------------------------------")
for i in range(tiempo):
    montos.append( [] )

    for j in range(sucursales):
        print("Ingrese ventas de la sucursal", j+1, "en el año", i+1)
        venta = int(input())
        montos[i].append(venta)
    
maximo = 0
for j in range(sucursales):
    suma = 0
    for i in range(tiempo):
        suma += montos[i][j]
    print("El numero de ventas en la sucursal", j+1,"es", suma)
    if suma > maximo:
        maximo = suma
        sucursal = j + 1
    print(f"La sucursal que mas vendió fue {sucursal}")


maximo = 0
for i in range(tiempo):
    suma = 0
    for j in range(sucursales):
        suma += montos[i][j]
    promedio = suma/sucursales

    print("El promedio de ventas del año",i+1,"es",promedio)

    if promedio > maximo:
        maximo = promedio
        anio = i+1
print(f"El año con mayor promedio es {anio}")