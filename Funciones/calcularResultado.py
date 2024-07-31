def dibujarGuiones(numero):
    guion = ""
    for i in range(1, numero+1):
        guion += "-"
    print(guion)

def calculadora(numero1, numero2, operador):
    match operador:
        case 1:
            resultado = numero1 + numero2
            dibujarGuiones(opcion*10)
            print(f"El resultado es: {resultado}")
            dibujarGuiones(opcion*10)
        case 2:
            resultado = numero1 - numero2
            dibujarGuiones(opcion*20)
            print(f"El resultado es: {resultado}")
            dibujarGuiones(opcion*20)
        case 3:    
            resultado = numero1 * numero2
            dibujarGuiones(opcion*30)
            print(f"El resultado es: {resultado}")
            dibujarGuiones(opcion*30)
        case 4:
            resultado = numero1 / numero2
            dibujarGuiones(opcion*40)
            print(f"El resultado es: {resultado}")
            dibujarGuiones(opcion*40)
        case _:
            print("e")
            KeyboardInterrupt

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo número: "))
opcion = int(input("Elija la operacion con 1, 2, 3 o 4. Cualquier otra tecla para salir: "))
calculadora(numero1, numero2, opcion)