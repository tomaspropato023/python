sucursales = int(input("Ingrese la cantidad de sucursales: "))
productos = 3

empresa = [[0 for _ in range(productos)] for _ in range(sucursales)]
ventasTotales = [0 for _ in range(sucursales)]
i = 0; j = 0; total = 0; mayor = 0
while i < sucursales:
    empresa[i][j] = int(input(f"Ventas en camisas en la sucursal {i+1}: "))
    empresa[i][j+1] = int(input(f"Ventas en pantalones en la sucursal {i+1}: "))
    empresa[i][j+2] = int(input(f"Ventas en chaquetas en la sucursal {i+1}: "))
    i += 1;

for i in range(sucursales):
    for j in range(productos):
        ventasTotales[i] += empresa[i][j]
        if ventasTotales[i] > mayor:
            mayor = ventasTotales[i]
            indice = i
        total += empresa[i][j]
print(total)
print(f"La sucursal con mayor valor es la sucursal {indice} con un total de {mayor}")

