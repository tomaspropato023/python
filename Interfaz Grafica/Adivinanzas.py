import tkinter as tk
from tkinter import messagebox

def verificar_respuesta(respuesta, solucion):
    if respuesta.casefold() == solucion:
        messagebox.showinfo("Resultado", "¡Correcto!")
    else:
        messagebox.showinfo("Resultado", f"Incorreto. La respuesta era {solucion}.")

def ejercicio_1():
    ventana = tk.Toplevel()
    ventana.title("Adivinanza")

    adivinanza = "Blanco por dentro, verde por fuera. Si quieres que te lo diga, espera."
    solucion = "pera"

    label = tk.Label(ventana, text=adivinanza)
    label.pack()

    respuesta = tk.Entry(ventana)
    respuesta.pack()

    boton = tk.Button(ventana, text="Verificar", command=lambda: verificar_respuesta(respuesta.get(), solucion))
    boton.pack()

def ejercicio_2():
    ventana = tk.Toplevel()
    ventana.title("Adivinanza")

    adivinanza = "Tiene ojos y no puede ver, tiene agua y no puede beber"
    solucion = "a"

    label = tk.Label(ventana, text=adivinanza)
    label.pack()

    opciones = [
        ("a) Un pez", "a"),
        ("b) Un río", "b"),
        ("c), Un espejo", "c")
    ]

    respuesta = tk.StringVar()

    for opcion, valor in opciones:
        radio = tk.Radiobutton(ventana, text=opcion, variable=respuesta, value=valor)
        radio.pack(anchor="w")


    boton = tk.Button(ventana, text="Verificar", command=lambda: verificar_respuesta(respuesta.get(), solucion))
    boton.pack()

