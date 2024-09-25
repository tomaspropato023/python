sucursales = int(input("Ingrese la cantidad de sucursales: "))
listaProductos = ["Camisas", "Pantalones", "Chaquetas"]
productos = 3

empresa = [[0 for _ in range(productos)] for _ in range(sucursales)]
productoMasVendido = [0 for _ in range(sucursales)]
ventasTotales = [0 for _ in range(sucursales)]
promedios = [0 for _ in range(productos)]
j = 0
for i in range(sucursales):
    empresa[i][j] = int(input(f"Ventas en camisas en la sucursal {i+1}: "))
    empresa[i][j+1] = int(input(f"Ventas en pantalones en la sucursal {i+1}: "))
    empresa[i][j+2] = int(input(f"Ventas en chaquetas en la sucursal {i+1}: "))
    
i = 0;
while i < sucursales:
    while j < productos:
        
        j+=1;
    i+=1;
