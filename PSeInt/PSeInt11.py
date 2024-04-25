# EJ 11

print("Para acceder al curso de grado superior necesita un titulo de bachiller. ¿Tiene uno?")
bachiller = str(input())
if bachiller == "si":
    print("Puede acceder al curso.")
else:
    print("¿Ha superado una prueba de acceso?")
    pruebaacceso = str(input())
    if pruebaacceso == "si":
        print("Felicidades, puede acceder al curso.")
    else:
        print("Lo sentimos, no puede acceder al curso.")