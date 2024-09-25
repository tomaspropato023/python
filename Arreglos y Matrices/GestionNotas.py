def calcular_promedios(estudiantes):
    promedios = {}
    for estudiante, asignaturas in estudiantes.items():
        promedios[estudiante] = {}
        for asignatura, notas in asignaturas.items():
            promedio = sum(notas) / len(notas) if notas else 0
            promedios[estudiante][asignatura] = promedio
    return promedios

def promedios_altos(promedios, umbral):
    print(f"Estudiantes con promedio mayor a {umbral} en alguna asignatura:")
    for estudiante, asignaturas in promedios.items():
        for asignatura, promedio in asignaturas.items():
            if promedio > umbral:
                print(f"{estudiante} en {asignatura} con promedio {promedio:.2f}")

def agregar_nota(estudiantes, estudiante, asignatura, nota):
    if estudiante in estudiantes:
        if asignatura in estudiantes[estudiante]:
            estudiantes[estudiante][asignatura].append(nota)
        else:
            estudiantes[estudiante] = {asignatura:[nota]}

estudiantes = {
    "Juan Perez": {"Matematicas": [8, 9, 7], "Historia": [6, 8]},
    "Maria Garcia": {"Matematicas": [10, 9, 9], "Historia": [7, 8]},
    "Ana Lopez": {"Matematicas": [5, 6], "Historia": [9, 10]}
}

promedios = calcular_promedios(estudiantes)
promedios_altos(promedios, 8)
agregar_nota(estudiantes, "Juan Perez", "Matematicas", 10)
print("Nuevas notas de Juan Perez:", estudiantes["Juan Perez"])