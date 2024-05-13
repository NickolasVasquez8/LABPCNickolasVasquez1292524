import turtle

# Función para dibujar un arroyo con líneas rectas
def dibujar_arroyo(t, ancho, largo):
    t.speed(0)  # Establecer la velocidad más rápida
    t.width(ancho)  # Establecer el ancho del arroyo
    for _ in range(largo):
        t.color("blue")  # Establecer el color del arroyo
        t.forward(10)  # Avanzar en línea recta
        t.penup()  # Levantar el lápiz para moverse sin dibujar
        t.right(90)  # Girar a la derecha
        t.forward(5)  # Moverse hacia adelante (lateralmente)
        t.left(90)  # Girar a la izquierda
        t.pendown()  # Bajar el lápiz para dibujar

# Crear una ventana de dibujo
ventana = turtle.Screen()
ventana.bgcolor("lightblue")

# Crear un objeto Turtle
alex = turtle.Turtle()
alex.shape("turtle")

# Posicionar a Alex para empezar a dibujar el arroyo
alex.penup()
alex.goto(-200, -100)
alex.pendown()

# Dibujar el arroyo
dibujar_arroyo(alex, 5, 100)

# Mantener la ventana abierta
ventana.mainloop()
