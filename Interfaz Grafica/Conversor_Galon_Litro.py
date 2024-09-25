import tkinter as tk

def convertir_cant():
    galones = float(entry_galones.get())
    litros = galones * 3.785
    label_litros.config(text=f"La cantidad en litros es {litros:.2f} gal.")

ventana = tk.Tk()
ventana.title("Conversor de distancia")

label_instrucciones = tk.Label(ventana, text="Ingrese la cantidad en galones:")
label_instrucciones.pack()
entry_galones = tk.Entry(ventana)
entry_galones.pack()
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_cant)
boton_convertir.pack()
label_litros = tk.Label(ventana, text="")
label_litros.pack()

ventana.mainloop()