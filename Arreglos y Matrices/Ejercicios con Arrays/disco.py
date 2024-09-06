import random
cantPersonas = 270
personas = ([0]*cantPersonas)
men21 = 0
may21 = 0
for i in range(cantPersonas):
    personas[i] = random.randint(18, 40)
    if personas[i] >= 21:
        may21 += 1
    elif personas[i] < 21:
        men21 += 1

print(personas)
print(f"Hay {may21} personas que tienen 21 años o más, y hay {men21} personas menores de 21")

