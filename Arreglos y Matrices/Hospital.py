columnas = 3
filas = int(input("Ingrese la cantidad de pacientes: "))

registroPacientes = [["_" for _ in range(columnas)] for _ in range(filas)]
costoMayor = [0 for _ in range(filas)]
total = 0; i = 0; j= 0


while i < filas:
    registroPacientes[i][j] = str(input(f"Ingrese el nombre del paciente {i+1}: "))
    registroPacientes[i][j+1] = str(input("Diagnostico: "))
    costo = int(input("Costo del tratamiento: "))
    total += costo
    if costo > 25000:
        costoMayor[i] = costo
    registroPacientes[i][j+2] = str(costo)
    i+=1

print(registroPacientes)





