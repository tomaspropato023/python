import tkinter as tk

def convertir_temp():
    fahrenheit = float(entry_fahrenheit.get())
    celsius = (fahrenheit - 32) * 5/9
    label_resultado.config(text=f"La temperatura en grados Celsius es: {celsius:.2f}")

ventana = tk.Tk()
ventana.title("Conversor de Temperatura")

label_instrucciones = tk.Label(ventana, text="Ingrese la temperatura en grados Fahrenheit:")
label_instrucciones.pack()
entry_fahrenheit = tk.Entry(ventana, justify="center")
entry_fahrenheit.pack()
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_temp)
boton_convertir.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

ventana.mainloop()