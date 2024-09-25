import tkinter as tk

def convertir_distancia():
    millas = float(entry_millas.get())
    kilometros = millas * 0.621
    label_kilometros.config(text=f"La distancia en kilometros es {kilometros:.2f} mi.")

ventana = tk.Tk()
ventana.title("Conversor de distancia")

label_instrucciones = tk.Label(ventana, text="Ingrese la distancia en kilometros:")
label_instrucciones.pack()
entry_millas = tk.Entry(ventana)
entry_millas.pack()
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_distancia)
boton_convertir.pack()
label_kilometros = tk.Label(ventana, text="")
label_kilometros.pack()

ventana.mainloop()