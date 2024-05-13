import turtle

# Configuración de la ventana
window = turtle.Screen()
window.setup(width=800, height=600)
window.title("Dibujando Cuentos")

# Creación del objeto Turtle
pen = turtle.Turtle()
pen.speed(0)  # Velocidad máxima

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

# Función para dibujar el cuento del Pez Dorado
def draw_goldfish_story():
    title = "Historia 1: El Pez Dorado"
    narrative = ("En un pequeño arroyo vivía un pez dorado llamado Sunny. Sunny era curioso y siempre exploraba nuevos lugares. "
                 "Un día, siguiendo una corriente, descubrió un jardín encantado lleno de flores brillantes. "
                 "Allí conoció a una mariposa amiga llamada Petal que le mostró el camino de regreso a casa.")
    
    draw_centered_margin_with_title(title)
    
    # Dibujar la narrativa centrada
    pen.penup()
    pen.goto(0, 150)
    pen.pendown()
    pen.write(narrative, align="center", font=("Arial", 12, "italic"))

# Función para dibujar el cuento del Árbol Parlante
def draw_talking_tree_story():
    title = "Historia 2: El Árbol Parlante"
    narrative = ("En el corazón del bosque había un árbol muy especial llamado Oli. Oli podía hablar con todos los animales del bosque "
                 "y les contaba historias mágicas. Un día, cuando una ardilla llamada Nuez perdió su nuez favorita, "
                 "Oli la ayudó a encontrarla entre las hojas. Desde entonces, Nuez y Oli se convirtieron en grandes amigos.")
    
    draw_centered_margin_with_title(title)
    
    # Dibujar la narrativa centrada
    pen.penup()
    pen.goto(0, 150)
    pen.pendown()
    pen.write(narrative, align="center", font=("Arial", 12, "italic"))

# Función para dibujar el cuento del Viaje del Globo de Papel
def draw_paper_balloon_journey_story():
    title = "Historia 3: El Viaje del Globo de Papel"
    narrative = ("En una soleada tarde de verano, Ana encontró un viejo periódico y decidió hacer un globo de papel. "
                 "Con la ayuda de su abuelo, lanzaron el globo al cielo. Mientras volaba, el globo llevaba un mensaje de amor y paz. "
                 "Al día siguiente, recibieron una carta de agradecimiento de una familia que encontró el globo y se sintió feliz al leer el mensaje.")
    
    draw_centered_margin_with_title(title)
    
    # Dibujar la narrativa centrada
    pen.penup()
    pen.goto(0, 150)
    pen.pendown()
    pen.write(narrative, align="center", font=("Arial", 12, "italic"))

# Solicitar el nombre del usuario
user_name = turtle.textinput("Nombre", "¿Cuál es tu nombre?")
# Solicitar el color favorito del usuario
user_color = turtle.textinput("Color Favorito", "¿Cuál es tu color favorito?")

# Ofrecer las opciones de cuento
story_choice = turtle.numinput("Selección de Cuento", f"Hola {user_name}! Elige un cuento:\n1. El Pez Dorado\n2. El Árbol Parlante\n3. El Viaje del Globo de Papel", minval=1, maxval=3)

# Dibujar el cuento seleccionado
if story_choice == 1:
    draw_goldfish_story()
elif story_choice == 2:
    draw_talking_tree_story()
elif story_choice == 3:
    draw_paper_balloon_journey_story()

# Mantener la ventana abierta
window.mainloop()
