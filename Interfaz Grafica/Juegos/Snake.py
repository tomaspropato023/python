import tkinter as tk
import random

# Dimensiones del tablero de juego
ANCHO = 20
ALTO = 20

# Tamaño de cada celda en píxeles
TAMANO_CELDA = 20

# velocidad de movimiento de la serpiente (en milisegundos)
velocidad = 100

class SnakeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake")
        
        self.canvas = tk.Canvas(root, width=ANCHO * TAMANO_CELDA, height=ALTO * TAMANO_CELDA, bg="black")
        self.canvas.pack()
        
        # Enfocar el lienzo para capturar las teclas
        self.canvas.focus_set()
        
        self.canvas.bind("<KeyPress>", self.tecla_presionada)
        
        self.iniciar_juego()
    

    def iniciar_juego(self):
        self.tablero = [[0] * ANCHO for _ in range(ALTO)]
        self.snake = [(ANCHO // 2, ALTO // 2)]
        self.direccion = (0, 1)  # Iniciar moviéndose hacia abajo
        self.comida = self.generar_comida()
        self.puntuacion = 0
        self.actualizar_tablero()
        self.root.after(velocidad, self.mover_serpiente)
    
    def generar_comida(self):
        while True:
            x = random.randint(0, ANCHO - 1)
            y = random.randint(0, ALTO - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    def actualizar_tablero(self):
        self.canvas.delete("all")
        
        for x, y in self.snake:
            self.canvas.create_rectangle(x * TAMANO_CELDA, y * TAMANO_CELDA,
                                         (x + 1) * TAMANO_CELDA, (y + 1) * TAMANO_CELDA, fill="green")
        
        x, y = self.comida
        self.canvas.create_oval(x * TAMANO_CELDA, y * TAMANO_CELDA,
                                (x + 1) * TAMANO_CELDA, (y + 1) * TAMANO_CELDA, fill="red")
        
        self.canvas.create_text(50, 10, text=f"Puntuación: {self.puntuacion}", fill="white")
    
    
    def tecla_presionada(self, event):
        if event.keysym == "Left" and self.direccion != (1, 0):
            self.direccion = (-1, 0)
        elif event.keysym == "Right" and self.direccion != (-1, 0):
            self.direccion = (1, 0)
        elif event.keysym == "Up" and self.direccion != (0, 1):
            self.direccion = (0, -1)
        elif event.keysym == "Down" and self.direccion != (0, -1):
            self.direccion = (0, 1)

    def mover_serpiente(self):
        x, y = self.snake[0]
        dx, dy = self.direccion
        nuevo_x = (x + dx) % ANCHO
        nuevo_y = (y + dy) % ALTO
        
        if (nuevo_x, nuevo_y) in self.snake[1:]:
            self.mostrar_fin_juego()
            return
        
        self.snake.insert(0, (nuevo_x, nuevo_y))
        
        if (nuevo_x, nuevo_y) == self.comida:
            self.puntuacion += 10
            self.comida = self.generar_comida()
        else:
            self.snake.pop()
        
        self.actualizar_tablero()
        
        self.root.after(velocidad, self.mover_serpiente)
    
    def mostrar_fin_juego(self):
        self.canvas.delete("all")
        self.canvas.create_text(ANCHO * TAMANO_CELDA // 2, ALTO * TAMANO_CELDA // 2,
                                text=f"Fin del juego\nPuntuación: {self.puntuacion}", fill="white",
                                font=("Helvetica", 16), anchor="center")
# Crear ventana principal
root = tk.Tk()
app = SnakeApp(root)
root.mainloop()