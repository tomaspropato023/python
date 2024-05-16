#EJ 3 - Estructuras Repetitivas

PRIM = 1
ULTI = 1000

contador = int
j = int
primo = bool

contador = 0
for i in range(PRIM, ULTI):
    primo = True
    j = 2
    while (i > j) and (primo == True):
        if (i % j == 0):
            primo = False
        else:
            j += 1
    if primo == True:
        print(f"{i} es primo.")
        contador += 1
print(f"Entre {PRIM} y {ULTI} hay {contador} numeros primos.")