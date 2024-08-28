def calcular_promedio(nota1, nota2, nota3):
    return ((nota1 + nota2 + nota3) / 3)

def buscar(alum_buscado, alumnos, alum_num):
    for indice in range(alum_num):
        if alumnos[indice] == alum_buscado.casefold():
            return indice
    return -1

def promedio_notas_estudiantes():
    alum_num = int(input("Ingrese el número de alumnos: "))
    alumno = [None] * alum_num
    nota1 = [0] * alum_num
    nota2 = [0] * alum_num
    nota3 = [0] * alum_num

    for i in range(alum_num):
        alumno[i] = input("Nombre: ")
        nota1[i] = int(input("Nota del primer trimestre: "))
        nota2[i] = int(input("Nota del segundo trimestre: "))
        nota3[i] = int(input("Nota del tercer trimestre: "))

    alum_buscado = input("Ingrese el nombre del alumno a buscar: ")
    ind_alum = buscar(alum_buscado, alumno, alum_num)

    if ind_alum != 1:
        promedio = calcular_promedio(nota1[ind_alum], nota2[ind_alum], nota3[ind_alum])
        print(f"El promedio de {alum_buscado.title()} es {promedio}.")
    else:
        print(f"No se pudo encontrar a {alum_buscado.title()}")

promedio_notas_estudiantes()