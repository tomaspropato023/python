#EJ Complementario 8

va = float(input("Ingrese la velocidad del primer cuerpo: "))
vb = float(input("Ingrese la velocidad del segundo cuerpo: "))
distancia = float(input("Ingrese la distancia que separa a los cuerpos: "))

tiempoEncuentro = distancia/(va+vb)

print("Los cuerpos se encontrarán en",tiempoEncuentro,"segundos.")