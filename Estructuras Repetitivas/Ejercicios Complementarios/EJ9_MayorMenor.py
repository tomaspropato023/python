#EJ Complementario 9 - Estructuras Repetitivas

limiteNumeros = int(input("Ingrese la cantidad de numeros a ingresar: "))
numeroMenor = limiteNumeros
numeroMayor = limiteNumeros

for i in range(1, limiteNumeros+1):
    numero = int(input("Ingrese un numero: "))
    if (numeroMenor > numero):
        numeroMenor = numero
    else:
        if (numero > numeroMayor):
            numeroMayor = numero

print(f"El numero menor es {numeroMenor}.")
print(f"El numero mayor es {numeroMayor}.")