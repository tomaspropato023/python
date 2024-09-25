def agregar_paciente(pacientes, nombre, diagnostico, costo):
    pacientes.append([nombre,diagnostico,costo])

def calcular_costo_total(pacientes):
    return sum(paciente[2] for paciente in pacientes)

def listar_pacientes_costosos(pacientes, umbral):
    print(f"Pacientes con un costo mayor a {umbral}:")
    for paciente in pacientes:
        if paciente[2]>umbral:
            print(f"Nombre: {paciente[0]}, Diagnóstico: {paciente[1]}, Costo: ${paciente[2]}")

pacientes = [["Juan Perez", "Gripe", 200], ["Maria Garcia", "Fractura", 1500], ["Ana Lopez", "Diabetes", 3500]]

agregar_paciente(pacientes, "Carlos Diaz", "Alergia", 2500)
costo_total = calcular_costo_total(pacientes)
print(f"Costo total de tratamiento: ${costo_total}")
listar_pacientes_costosos(pacientes, 1000)