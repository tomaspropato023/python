#EJ 6 - Estructuras Repetitvas

valor1 = 1
valor2 = 0
suma = valor1 + (2 * valor2)
contador = 0

while (suma < 300):     
    valor2 = valor1
    valor1 = suma
    suma = valor1 + (2 * valor2)
    contador += 1

print(f"El rango es {contador} y el resultado es {suma}.")  