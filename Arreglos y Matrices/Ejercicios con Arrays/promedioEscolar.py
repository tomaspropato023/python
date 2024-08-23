def cargaAlumnos(cantidad):
    i = 0
    alumnos = []
    primerTrimestre = []
    segundoTrimestre = []
    tercerTrimestre = []
    while i < cantidad:
        alumno = str(input("Nombre del alumno: "))
        alumnos.append(alumno)
        trimestre1 = int(input("Nota del primer trimestre: "))
        trimestre2 = int(input("Nota del segundo trimestre: "))
        trimestre3 = int(input("Nota del tercer trimestre: "))
        primerTrimestre.append(trimestre1)
        segundoTrimestre.append(trimestre2)
        tercerTrimestre.append(trimestre3)
        i+=1
    promedioNotas(alumnos, primerTrimestre, segundoTrimestre, tercerTrimestre)

def promedioNotas(listaAlumnos, notasTrim1, notasTrim2, notasTrim3):
    promedios = []
    for i in range(len(listaAlumnos)):
        promedio = ((notasTrim1[i] + notasTrim2[i] + notasTrim3[i]) / 3)
        promedios.append(promedio)
        print(f"El alumno {listaAlumnos[i]} tiene un promedio de {promedios[i]}")
        

dimension = int(input("Ingrese la cantidad de alumnos: "))
cargaAlumnos(dimension)
