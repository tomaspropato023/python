print("Ingrese tres numeros: ")
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3:
    print (n1,"es mayor que",n2,"y",n3)
if n2 > n1 and n2 > n3:
    print (n2,"es mayor que",n1,"y",n3)
if n3 > n1 and n3 > n2:
    print (n3,"es mayor que",n1,"y",n2)