import turtle 
import random
import time

delay = 0.01
score = 0
high_score = 0
# Windows config
# El modulo turtle con la clase Screen sirve para crear la ventana
windows = turtle.Screen()
windows.title("Snake game")
windows.bgcolor("black")
windows.setup(width=1000,height=600)

# Texto

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,300)
texto.write("Score: 0        High Score: 0", align="center", font =("Courier",22,"normal"))



# Snake 
"""Construimos el cuerpo de la serpiente"""

## Head

head = turtle.Turtle()
head.speed(0)
head.goto(0,0) # Punto de partida
head.color("yellow")
head.shape("square") #Forma de cabeza
head.penup() #Para que al mover no deje un camino o lienzo
head.direction ="stop"

## Body

body_now = []



# Food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,80)

# Functions
""" Programacion de los movimientos de la serpiente"""
def arriba():
    if head.direction != "down":
        head.direction = "up"
def abajo():
    if head.direction != "up":
        head.direction = "down"
def izquierda():
    if head.direction != "right":
        head.direction = "left"
def derecha():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor() # Si la tecla es "up" obtenemos las cordenadas 
        head.sety(y + 20) # Aqui modificamos las coordenadas avanzando 20 pasos
    elif head.direction == "down":
        y = head.ycor() 
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor() 
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor() 
        head.setx(x + 20)   
# Keyboard
""" Configuramos los metodos para escuchar el teclado"""
windows.listen() # Dejamos a la ventana escuchando 
windows.onkeypress(arriba,"Up")  # Cuando alguien presione una tecla de movimiento, le ordenamos que se mueva con la funcion creada
windows.onkeypress(abajo,"Down")
windows.onkeypress(izquierda,"Left")
windows.onkeypress(derecha,"Right")


while True:
    windows.update()

    # Definimos el rango de espacio donde se movera la serpiente y en caso se salga regrese al punto de origen
    
    if head.xcor()>980 or head.xcor()<-980 or head.ycor()>580 or head.ycor()<-580:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        texto.clear()
        score = 0
        high_score = 0
                 
        texto.write("Score: 0        High Score: 0", align="center", font =("Courier",22,"normal"))

        body_now.clear()
    # Programamos la colision entre la cabeza y el cuerpo de la serpiente
    for segment in body_now:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                texto.clear()
                score = 0
                high_score = 0
                 
                texto.write("Score: 0        High Score: 0", align="center", font =("Courier",22,"normal"))
        # Hidden
                for body in body_now:
                    body.goto(-5000,5000)

        # Clean lists : Es necesario limpiar el segmento que deja la serpiente en caso colisione
        
                body_now.clear()
        
    if head.distance(food) < 20:
        x = random.randint(-480,480)
        y = random.randint(-280,280)
        food.goto(x,y)

        #Se crea un nuevo segmento que se añadira a la lista cuando se coma la manzana 
        body_new =turtle.Turtle()
        body_new.speed(0)
        body_new.shape("square")
        body_new.color("gray")
        body_new.penup()
        body_now.append(body_new) #Agrego el nuevo segmento "body_new" al body now al final

        score += 10
        if score > high_score:
            high_score = score
        
        texto.clear()
        
        texto.write("Score: {}        High Score: {}".format(score,high_score), align="center", font =("Courier",22,"normal"))
        
    body_total = len(body_now) #Obtengo el rango de la lista
    for index in range(body_total - 1,0,-1): #Recorremos el rango de la lista
        x = body_now[index-1].xcor() #Obtener la coordenada del ultimo elemento de la lista
        y = body_now[index-1].ycor() #Obtener la coordenada del ultimo elemento de la lista
        body_now[index].goto(x,y)   #Sigue o ve las coordenadas indicadas
    
    if body_total > 0: 
        x = head.xcor() #Pedimos las coordenadas de la cabeza de la serpiente
        y = head.ycor()
        body_now[0].goto(x,y) #El cuerpo se unira a la cabeza

    
    time.sleep(delay)    
    move()



turtle.mainloop()

