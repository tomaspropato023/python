# Ejercicio 3

print("-----------------------------------------")
print("Ejercicio 3: Puntaje Final")
print("-----------------------------------------")

print("Ingrese el numero de respuestas correctas: ")
RC = int(input())
print("Ingrese el numero de respuestas incorrectas")
RI = int(input())
print("Ingrese el numero de respuestas en blanco")
RB = int(input())

PCR = RC*3
PCI = RI*-1
PRB = RB*0
PF = PCR+PCI+PRB

print("El puntaje total es ", PF)