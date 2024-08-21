listaColoresAulas = ["Azul", "Verde", "Amarillo"]
listaCapacidadAulas = [40, 35, 30]
cantidadAlumnos = int(input("Ingrese la cantidad de alumnos inscriptos al curso: "))

capacidadAulaAux = listaCapacidadAulas[0]
indiceAulaAux = 0
for i in range(1, len(listaCapacidadAulas)):
    capacidadAulaActual = listaCapacidadAulas[i]
    if (capacidadAulaActual >= cantidadAlumnos) and (capacidadAulaActual < capacidadAulaAux):
        capacidadAulaAux = capacidadAulaActual
        indiceAulaAux = i
colorAula = listaColoresAulas[indiceAulaAux]
print(f"El aula indicada para la cantidad ingresada de alumnos es el aula {colorAula} con una capacidad máxima de {capacidadAulaAux}")