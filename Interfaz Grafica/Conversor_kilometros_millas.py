import tkinter as tk

def convertir_distancia():
    kilometros = float(entry_kilometros.get())
    millas = kilometros / 1.609
    label_millas.config(text=f"La distancia en millas es {millas:.2f} mi.")

ventana = tk.Tk()
ventana.title("Conversor de distancia")

label_instrucciones = tk.Label(ventana, text="Ingrese la distancia en kilómetros:")
label_instrucciones.pack()
entry_kilometros = tk.Entry(ventana)
entry_kilometros.pack()
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_distancia)
boton_convertir.pack()
label_millas = tk.Label(ventana, text="")
label_millas.pack()

ventana.mainloop()