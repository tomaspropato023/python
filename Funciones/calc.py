print("Ingrese los numeros: ");
numero1 = int(input());
numero2 = int(input());
opcion = int(input("Presione 1 para sumar los numeros, 2 para restarlos o cualquier otro numero para salir: "));

def dibujarGuiones(numero):
    guion = ""
    for i in range(1, numero+1):
        guion += "-"
    print(guion)



if opcion == 1:
    dibujarGuiones(40)
    print("La suma es:", (numero1 + numero2))
    dibujarGuiones(40)
if opcion == 2:
    dibujarGuiones(30)
    print("La resta es:", (numero1 - numero2))
    dibujarGuiones(30)

if opcion > 2:
    print("Error")



