import tkinter as tk

def convertir_cant():
    litros = float(entry_litros.get())
    galones = litros * 0.264
    label_galones.config(text=f"La cantidad en galones es {galones:.2f} gal.")

ventana = tk.Tk()
ventana.title("Conversor de distancia")

label_instrucciones = tk.Label(ventana, text="Ingrese la cantidad en litros:")
label_instrucciones.pack()
entry_litros = tk.Entry(ventana)
entry_litros.pack()
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_cant)
boton_convertir.pack()
label_galones = tk.Label(ventana, text="")
label_galones.pack()

ventana.mainloop()