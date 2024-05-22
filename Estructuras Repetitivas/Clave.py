#EJ Eureka

CLAVE = "eureka"

claveIngr = str(input("Ingrese la clave: "))
contador = 0

while (contador < 2) and (claveIngr.casefold() != CLAVE):
    claveIngr = str(input("Clave incorrecta. Vuelva a ingresar la clave: "))
    contador += 1

if claveIngr.casefold() != CLAVE:
    print("Ha agotado los intentos.")
    StopIteration
else:
    print("Clave correcta.")
    exit