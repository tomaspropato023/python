#EJ 3 - Estructuras Repetitivas

PRIMERNUM = 2
ULTINUM = 1000

primo = bool

contador = 0
for i in range(PRIMERNUM, ULTINUM):
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
print(f"Entre {PRIMERNUM} y {ULTINUM} hay {contador} numeros primos.")