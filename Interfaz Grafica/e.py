import tkinter as tk

root = tk.Tk()
root.title("Hola Mundo con Tkinter")
root.geometry("300x200")
label = tk.Label(root, text="¡Hola Mundo!")
label.pack(anchor="center",pady=50)
root.mainloop()