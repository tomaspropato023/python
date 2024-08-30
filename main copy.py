import tkinter as tk
from tkinter import messagebox

def iniciar_programa():
    ventana_principal = tk.Tk()
    ventana_principal.title("Programa de Educación Sexual Integral (ESI)")
    ventana_principal.geometry("600x400")

    # Texto de bienvenida
    bienvenida_texto = tk.Label(ventana_principal, text="Bienvenido al Programa de Educación Sexual Integral (ESI)", font=("Arial", 14), wraplength=550, justify="center")
    bienvenida_texto.pack(pady=20)

    # Botón para comenzar
    boton_comenzar = tk.Button(ventana_principal, text="Comenzar", font=("Arial", 12), command=lambda: mostrar_informacion(ventana_principal))
    boton_comenzar.pack(pady=20)

    ventana_principal.mainloop()

def mostrar_informacion(ventana):
    ventana.destroy()
    ventana_info = tk.Tk()
    ventana_info.title("Información sobre ESI")
    ventana_info.geometry("600x400")

    # Texto de información
    info_texto = (
        "La Educación Sexual Integral (ESI) es un enfoque pedagógico que busca proporcionar a niños, adolescentes "
        "y jóvenes conocimientos, actitudes y valores que les permitan disfrutar de su salud, bienestar, dignidad "
        "y respeto mutuo.\n\n"
        "La ESI aborda temas como el desarrollo físico y emocional, la identidad de género, la salud sexual y "
        "reproductiva, los derechos humanos, el respeto por la diversidad, y la prevención de situaciones de abuso y violencia."
    )
    
    label_info = tk.Label(ventana_info, text=info_texto, font=("Arial", 12), wraplength=550, justify="left")
    label_info.pack(pady=20)

    # Botón para iniciar el cuestionario
    boton_cuestionario = tk.Button(ventana_info, text="Iniciar Cuestionario", font=("Arial", 12), command=lambda: iniciar_cuestionario(ventana_info))
    boton_cuestionario.pack(pady=20)

    ventana_info.mainloop()

# Declaramos la variable puntaje como global
puntaje = 0

def iniciar_cuestionario(ventana):
    global puntaje  # Usamos la variable global puntaje
    ventana.destroy()
    ventana_cuestionario = tk.Tk()
    ventana_cuestionario.title("Cuestionario ESI")
    ventana_cuestionario.geometry("600x600")

    # Preguntas y respuestas
    preguntas = [
        {
            "pregunta": "¿Cuál es el propósito principal de la ESI?",
            "opciones": ["Prevenir enfermedades", "Proveer conocimientos, actitudes y valores para la salud y bienestar", "Fomentar la abstinencia", "Ninguna de las anteriores"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué temas abarca la ESI?",
            "opciones": ["Solo salud sexual", "Derechos humanos, diversidad, salud sexual y reproductiva", "Solo prevención de enfermedades", "Solo identidad de género"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿A qué edades está dirigida la ESI?",
            "opciones": ["Solo adolescentes", "Solo adultos", "A todas las edades desde la infancia", "Ninguna de las anteriores"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué es el consentimiento en una relación?",
            "opciones": ["Una expectativa", "Algo opcional", "Un acuerdo mutuo sin presión", "No es necesario si hay amor"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cuál es el método anticonceptivo más efectivo para prevenir infecciones de transmisión sexual (ITS)?",
            "opciones": ["Píldoras anticonceptivas", "Condón", "Dispositivo intrauterino (DIU)", "Método del ritmo"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué significa diversidad en el contexto de la ESI?",
            "opciones": ["Aceptar solo a quienes piensan igual", "Reconocer y respetar diferentes identidades, orientaciones y expresiones", "Solo incluir a algunas minorías", "No es relevante para la ESI"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Por qué es importante hablar sobre la salud mental en el contexto de la ESI?",
            "opciones": ["No es importante", "Porque afecta el bienestar integral de las personas", "Porque es una tendencia moderna", "Solo es relevante para algunos grupos"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál es un derecho fundamental relacionado con la ESI?",
            "opciones": ["El derecho a la privacidad", "El derecho a la información sobre salud sexual y reproductiva", "El derecho a la discriminación", "Ninguna de las anteriores"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué implica una relación basada en el respeto mutuo?",
            "opciones": ["Ignorar las opiniones de la otra persona", "Escuchar y valorar las necesidades y deseos del otro", "Imponer creencias personales", "No mostrar emociones"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué es la pubertad?",
            "opciones": ["Un proceso de envejecimiento", "Una etapa de cambios físicos y emocionales en la adolescencia", "Algo que solo les ocurre a los hombres", "Un estado permanente de madurez"],
            "respuesta_correcta": "B"
        }
    ]

    indice_pregunta = [0]  # Usamos una lista para pasar el índice de pregunta por referencia

    # Función para validar respuestas
    def validar_respuesta(respuesta, correcta):
        if respuesta.get() == correcta:
            puntaje += 1

        if indice_pregunta[0] < len(preguntas) - 1:
            indice_pregunta[0] += 1
            mostrar_pregunta()
        else:
            mostrar_resultados()

    # Función para mostrar una pregunta
    def mostrar_pregunta():
        for widget in ventana_cuestionario.winfo_children():
            widget.destroy()

        pregunta = preguntas[indice_pregunta[0]]
        pregunta_texto = tk.Label(ventana_cuestionario, text=pregunta["pregunta"], font=("Arial", 12), wraplength=550, justify="left")
        pregunta_texto.pack(pady=10)

        respuesta = tk.StringVar()  # Variable para almacenar la respuesta seleccionada

        for opcion in pregunta["opciones"]:
            tk.Radiobutton(ventana_cuestionario, text=opcion, variable=respuesta, value=opcion[0], font=("Arial", 10)).pack(anchor="w")

        boton_siguiente = tk.Button(ventana_cuestionario, text="Siguiente", font=("Arial", 12), command=lambda: validar_respuesta(respuesta, pregunta["respuesta_correcta"]))
        boton_siguiente.pack(pady=10)

    # Mostrar la primera pregunta
    mostrar_pregunta()
    ventana_cuestionario.mainloop()

# Función para mostrar los resultados
def mostrar_resultados():
    global puntaje  # Usamos la variable global puntaje
    ventana_resultados = tk.Tk()
    ventana_resultados.title("Resultados")
    ventana_resultados.geometry("600x400")

    resultado_texto = f"Tu conocimiento actual sobre ESI es de {puntaje * 100 / 10:.2f}% basado en este cuestionario."
    label_resultado = tk.Label(ventana_resultados, text=resultado_texto, font=("Arial", 14), wraplength=550, justify="center")
    label_resultado.pack(pady=20)

    estadisticas_texto = (
        "Estadísticas Generales sobre ESI:\n"
        "• El 90% de los estudiantes que reciben ESI reportan un mejor entendimiento de su salud sexual y reproductiva.\n"
        "• Las tasas de embarazo adolescente han disminuido un 15% en regiones con ESI obligatoria.\n"
        "• La aceptación de la diversidad y el respeto mutuo aumentaron en un 20% entre estudiantes que reciben ESI.\n"
    )

    label_estadisticas = tk.Label(ventana_resultados, text=estadisticas_texto, font=("Arial", 12), wraplength=550, justify="left")
    label_estadisticas.pack(pady=20)

    ventana_resultados.mainloop()


iniciar_programa()