import turtle

# Función para dibujar una flor
def dibujar_flor(t, colores):
    t.speed(0)  # Configurar la velocidad de dibujo
    for _ in range(4):  # Repetir 4 veces para dibujar los pétalos
        for color in colores:  # Iterar sobre los colores de los pétalos
            t.color(color)
            t.begin_fill()  # Comenzar el relleno del pétalo
            t.circle(50, 180)  # Dibujar un arco de círculo
            t.left(90)  # Girar hacia la izquierda
            t.circle(50, 180)  # Dibujar otro arco de círculo
            t.end_fill()  # Finalizar el relleno del pétalo
            t.left(90)  # Girar hacia la izquierda para la siguiente iteración
        t.right(90)  # Girar hacia la derecha para la siguiente fila de pétalos
        t.penup()  # Levantar el lápiz
        t.forward(100)  # Moverse hacia adelante para la siguiente flor
        t.pendown()  # Bajar el lápiz
        t.right(180)  # Girar hacia la derecha para la siguiente fila de flores

# Función para borrar las flores
def borrar_flor(dibujar_flor):
    pen.clear(dibujar_flor)

# Función para dibujar un tronco de árbol
def dibujar_tronco(t, colores):
    t.speed(0)
    for _ in range(1):
        for colores in colores:  # Iterar sobre los colores del arbol
            t.penup() 
            t.pendown()
            t.color("Brown")
        t.begin_fill()
        t.forward(50)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(100)
        t.end_fill()

# Función para dibujar las hojas del árbol
def dibujar_hojas(t, coloreando):
    t.speed(0)
    for _ in range(1):  # Dibujar una capa de hojas
         for coloreando in coloreando:  # Iterar sobre los colores del arbol
            t.penup()
            t.pendown()
            t.color("green")
            t.begin_fill()
            t.circle(60)
            t.end_fill()

# Función para dibujar una ave
def dibujar_ave(t, color_cuerpo, color_alas):
    t.speed(0)
    t.penup()
    t.color(color_cuerpo)
    t.goto(50, 50)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()
    t.goto(40, 50)
    t.pendown()
    t.color(color_alas)
    t.begin_fill()
    t.circle(20, -100)
    t.right(120)
    t.circle(20, -100)
    t.end_fill()

# Función para dibujar un lago
def dibujar_lago(t, color_agua):
    t.speed(0)
    t.penup()
    t.goto(-100, -180)
    t.pendown()
    t.color(color_agua)
    t.begin_fill()
    t.circle(80)
    t.end_fill()

# Función para dibujar un pez saltando
def dibujar_pez(t, color_cuerpo, color_aletas):
    t.speed(0)
    t.penup()
    t.color(color_cuerpo)
    t.goto(-100, -100)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.goto(-90, -100)
    t.pendown()
    t.color(color_aletas)
    t.begin_fill()
    t.circle(5, -100)
    t.right(120)
    t.circle(5, -100)
    t.end_fill()

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
    pen.goto(8, -270)
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
    borrar_panel()
    draw_centered_margin_with_title(f"Panel {panel + 1}")
    draw_centered_text(narrativas[panel])
    if panel == len(narrativas) - 1:
        mostrar_cuestionario()

# Función para borrar el panel anterior
def borrar_panel():
    pen.clear()

# Función para mostrar el cuestionario
def mostrar_cuestionario():
    preguntas = [
        "¿Cuál es el nombre del pez protagonista?",
        "¿Qué descubrió el pez un día siguiendo una corriente?",
        "¿Cómo se llama la ave amiga que el pez conoce en el jardín encantado?",
    ]
    respuestas_correctas = ["Sunny", "un jardin encantado", "Petal"]
    puntaje = 0
    
    print("Responde las siguientes preguntas:")
    for i, pregunta in enumerate(preguntas):
        respuesta = input(pregunta + "\n")
        while respuesta.lower() != respuestas_correctas[i].lower():  # Mientras la respuesta sea incorrecta
            print("Incorrecto. Inténtalo de nuevo.")
            respuesta = input(pregunta + "\n")
        print("¡Correcto!")
        puntaje += 1
    
    print("Tu puntaje final es:", puntaje, "de", len(preguntas))

# Solicitar el nombre del usuario
user_name = turtle.textinput("Nombre", "¿Cuál es tu nombre?")
# Solicitar el color favorito del usuario
user_color = turtle.textinput("Color Favorito", "¿Cuál es tu color favorito?")
#Solicitar la edad del usuario 
user_edad = turtle.textinput ("Edad", "cual es tu edad?")
# Lista de narrativas de cada panel
narrativas = [
    "En un pequeño arroyo vivía un pez dorado llamado Sunny.\nSunny era curioso y siempre exploraba nuevos lugares.",
    "Un día,\n siguiendo una corriente,\n descubrió un jardín encantado lleno de flores brillantes.",
    "Allí conoció a una ave amiga llamada Petal,\n que le mostró el camino de regreso a casa.",
    "Juntos,\n Sunny y Petal exploraron el jardín,\n encontrando cascadas mágicas y árboles llenos de frutas exóticas.",
    "Después de pasar un día maravilloso en el jardín,\n Sunny se despidió de Petal con la promesa de regresar pronto.",
    "Con el corazón lleno de alegría y nuevas experiencias,\n Sunny nadó de regreso a su arroyo,\n ansioso por contar sus aventuras a sus amigos."
]

# Configuración de la ventana
window = turtle.Screen()
window.setup(width=800, height=600)
window.title("Cuento: El Pez Dorado")

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

# Dibujar las flores
alex = turtle.Turtle()
alex.penup()
alex.goto(-10, 30)
dibujar_flor(alex, ["red", "orange", "yellow", "purple"])

# Dibujar el tronco del árbol
tronco = turtle.Turtle()
tronco.penup()
tronco.goto(-10, 30)
dibujar_tronco(tronco, ["Brown"])

# Dibujar las hojas del árbol
hojas = turtle.Turtle()
hojas.penup()
hojas.goto(-10, 30)
dibujar_hojas(hojas, ["green"])

# Dibujar la ave
ave = turtle.Turtle()
dibujar_ave(ave, "black", "orange")

# Dibujar el lago
lago = turtle.Turtle()
dibujar_lago(lago, "blue")

# Dibujar el pez saltando
pez = turtle.Turtle()
dibujar_pez(pez, "orange", "yellow")

# Mantener la ventana abierta
window.mainloop()
