print ("Ingrese un numero")
num = int(input())
if num <= 0:
    print("Se ha producido un error")
    StopIteration
else:
    print ("Del numero",num,"su potencia es",(num**2),"y su raiz es",(num**0.5))