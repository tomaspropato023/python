def esPalindrom(palabra):
    izq = 0
    der = len(palabra) - 1
    while izq < der:
        if palabra[izq] != palabra[der]:
            return False
        izq += 1
        der -= 1
    return True

print(esPalindrom("pipepip"))