#EJ Calificaciones
import math

nombreAlumno = str(input("Ingrese el nombre del alumno: "))
nota1 = 0
nota2 = 0
nota3 = 0
resultadoFinal = 0

while (nombreAlumno != ""):
    nota1 = int(input("Nota de parte practica: "))
    nota2 = int(input("Nota de problemas: "))
    nota3 = int(input("Nota de parte teorica: "))

    if (nota1 >= 0 and nota1 <= 10) and (nota2 >= 0 and nota2 <= 10) and (nota3 >= 0 and nota3 <= 10):
        resultadoFinal = math.trunc((nota1*0.1)+(nota2*0.5)+(nota3*0.4))
        print(f"La nota final de {nombreAlumno} es {resultadoFinal}")
    else:
        print("Error.")
    nombreAlumno = str(input("Ingrese el nombre del siguiente alumno: "))