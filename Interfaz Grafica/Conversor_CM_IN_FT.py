import tkinter as tk

def convertir_longitud():
    try:
        centimetros = float(entry_centimetros.get())
        pulgadas = centimetros / 2.54
        pies = centimetros / 30.48

        label_resultado_pulgadas.config(text=f"La longitud en pulgadas es: {pulgadas:.2f} in.")
        label_resultado_pies.config(text=f"La longitud en pies es: {pies:.2f} ft.")
    except ValueError:
        label_resultado_pulgadas.config(text="Por favor, ingrese una longitud válida en centímetros.")

ventana = tk.Tk()
ventana.title("Conversor de Longitud")

label_instrucciones = tk.Label(ventana, text="Ingrese la longitud en centímetros:")
label_instrucciones.pack()

entry_centimetros = tk.Entry(ventana)
entry_centimetros.pack()

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_longitud)
boton_convertir.pack()

label_resultado_pulgadas = tk.Label(ventana, text="")
label_resultado_pulgadas.pack()
label_resultado_pies = tk.Label(ventana, text="")
label_resultado_pies.pack()

ventana.mainloop()