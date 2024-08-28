dimension = int(input("Ingrese la cantidad de alumnos: "))
alumnos = []
nota1 = []
nota2 = []
nota3 = []
promedios = []
for i in range(dimension):
    alumno = str(input("Nombre del alumno: "))
    notaTrim1 = int(input("Nota primer trimestre: "))
    notaTrim2 = int(input("Nota segundo trimestre: "))
    notaTrim3 = int(input("Nota tercer trimestre: "))
    alumnos.append(alumno)
    nota1.append(notaTrim1)
    nota2.append(notaTrim2)
    nota3.append(notaTrim3)

alumnoABuscar = str(input("Ingrese el nombre del alumno al que desee buscar: "))
indiceAlumno = -1
i = 0
while (i < dimension) or (indiceAlumno == -1):
    if alumnos[i] == alumnoABuscar:
        indiceAlumno = i
        promedio = ((nota1[i] + nota2[i] + nota3[i]) / 3)
    i += 1
if indiceAlumno >= 0:
    print(f"El alumno {alumnoABuscar} tiene un promedio de {promedio}")
else:   
    print(f"El alumno {alumnoABuscar} no fue encontrado")