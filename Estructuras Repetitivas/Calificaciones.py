#EJ Calificaciones

nombreAlumno = str(input("Ingrese el nombre del alumno: "))
nota1 = 0
nota2 = 0
nota3 = 0
resultado = 0

while (nombreAlumno != ""):
    nota1 = int(input("Nota de parte practica: "))
    nota2 = int(input("Nota de problemas: "))
    nota3 = int(input("Nota de parte teorica: "))

    if (nota1 <= 0) or (nota2 <= 0) or (nota3 <= 0):
        print("Error.")
    else:
        resultado = nota1+nota2+nota3
        print("La incidencia de la parte práctica en la nota es:", (resultado*0.1))
        print("La incidencia de la parte problemática en la nota es:", (resultado*0.5))
        print("La incidencia de la parte teórica en la nota es:", (resultado*0.4))
    
    nombreAlumno = str(input("Ingrese el nombre del siguiente alumno: "))