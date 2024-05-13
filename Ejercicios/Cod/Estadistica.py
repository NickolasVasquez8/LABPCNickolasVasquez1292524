import turtle

# Configuración de la ventana
window = turtle.Screen()
window.setup(width=800, height=600)
window.title("Cuento: El Pez Dorado")

# Lista de narrativas de cada panel
narrativas = [
    "En un pequeño arroyo vivía un pez dorado llamado Sunny.\n Sunny era curioso y siempre exploraba nuevos lugares.",
    "Un día, siguiendo una corriente, descubrió un jardín encantado lleno de flores brillantes.",
    "Allí conoció a una mariposa amiga llamada Petal que le mostró el camino de regreso a casa."
]

# Función para dibujar el margen con título centrado
def draw_centered_margin_with_title(title):
    # Dibujar el margen
    pen.penup()
    pen.goto(-350, 200)
    pen.pendown()
    pen.pensize(3)
    pen.color("black")
    for _ in range(2):
        pen.forward(700)
        pen.right(90)
        pen.forward(400)
        pen.right(90)
    
    # Dibujar el título centrado
    pen.penup()
    pen.goto(0, 230)
    pen.pendown()
    pen.write(title, align="center", font=("Arial", 20, "bold"))

# Función para dibujar el texto centrado
def draw_centered_text(text):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.write(text, align="center", font=("Arial", 12, "normal"))

# Función para cambiar al panel anterior
def panel_anterior():
    global panel_actual
    if panel_actual > 0:
        panel_actual -= 1
        dibujar_panel(panel_actual)

# Función para cambiar al siguiente panel
def panel_siguiente():
    global panel_actual
    if panel_actual < len(narrativas) - 1:
        panel_actual += 1
        dibujar_panel(panel_actual)

# Función para dibujar un panel específico
def dibujar_panel(panel):
    pen.clear()
    draw_centered_margin_with_title(f"Panel {panel + 1}")
    draw_centered_text(narrativas[panel])

# Configurar las teclas de flecha izquierda y derecha para cambiar de panel
window.listen()
window.onkeypress(panel_anterior, "Left")
window.onkeypress(panel_siguiente, "Right")

# Crear el objeto Turtle
pen = turtle.Turtle()
pen.speed(0)  # Velocidad máxima

# Panel actual
panel_actual = 0

# Dibujar el primer panel
dibujar_panel(panel_actual)

# Creación del objeto Turtle
pen = turtle.Turtle()
pen.speed(0)  # Máxima velocidad




# Mantener la ventana abierta
window.mainloop()
