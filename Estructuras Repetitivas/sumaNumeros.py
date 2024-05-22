num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
if num1 > num2:
    suma = num1
    mayor = num1
    menor = num2
else:
    suma = num2
    mayor = num2
    menor = num1
for i in range (menor, mayor):
    suma+=i
print(suma)