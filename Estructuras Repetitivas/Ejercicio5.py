#EJ 5 - Estructuras Repetitivas

x = int(input("Introduzca el valor de x: "))

e = 1
num = 1
den = 1
i = 1

#DO

num = x**num
den = den*i
i = i+1
e = e + num/den

while not (num/den < 0.00001):
    num = x**num
    den = den*i
    i = i+1
    e = e + num / den

print(f"e, elevado a {x} es: {e}")
