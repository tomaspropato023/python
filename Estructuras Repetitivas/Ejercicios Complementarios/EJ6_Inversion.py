#EJ Complementario 6 - Estructuras Repetitivas
auxiliar1 = 0
auxiliar2 = 0
numero = int(input("Ingrese un numero: "))
i = 10
while (i <= numero):
    auxiliar1 = numero % 10
    numero = numero // 10
    auxiliar2 = (auxiliar2 * 10) + auxiliar1

auxiliar2 = (auxiliar2 * 10) + numero
print(f"El numero invertido será {auxiliar2}")  