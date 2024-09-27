import tkinter as tk
import random

class JuegoAdivinarNumero:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el numero")

        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

        self.label_instrucciones = tk.Label(root, text="Estoy pensando en un numero entre 1 y 100.")
        self.label_instrucciones.pack()

        self.label_suposicion = tk.Label(root, text="¿Cuál número es?")
        self.label_suposicion.pack()

        self.entry_suposicion = tk.Entry(root)
        self.entry_suposicion.pack()

        self.boton_verificar = tk.Button(root, text="Verificar", command=self.verificar_suposicion)
        self.boton_verificar.pack()
        
        self.label_resultado = tk.Label(root, text="")
        self.label_resultado.pack()

    def verificar_suposicion(self):
        suposicion = int(self.entry_suposicion.get())
        self.intentos += 1
        if suposicion < self.numero_secreto:
            resultado = "Demasiado bajo."
        elif suposicion > self.numero_secreto:
            resultado = "Demasiado alto."
        else:
            resultado = f"Adivinaste el numero en {self.intentos} intentos!"
            self.boton_verificar.config(state="disabled")   
        self.label_resultado.config(text=resultado)


root = tk.Tk()
app = JuegoAdivinarNumero(root)
root.mainloop()