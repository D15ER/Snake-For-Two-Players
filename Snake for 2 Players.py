from http.client import FOUND
import turtle
import time
import random

posponer = 0.1# Constante que indica posponer el proceso elt tiempo indicado

# Marcador

Score_uno = 0
High_uno = 0

Score_dos = 0
High_dos = 0

#Configuracion de la ventana

window = turtle.Screen() #Crea la ventana Grafica
window.title("Snake for 2 Players") #Indica el titulo de en la ventana
window.bgcolor("black") # Elige el color de fondo
window.setup(width =600 , height = 600) # Indica la resolucion de la ventana grafica
window.tracer(0)

#Cabeza de Serpiente - Jugador 1

cabeza_uno = turtle.Turtle() #Creacion de la flecha
cabeza_uno.speed(0) # El dibujo es automatico
cabeza_uno.shape("square") # Cambia la forma de la flecha
cabeza_uno.color("blue") # Se le indica el color de la flecha
cabeza_uno.penup() # No deja rastro cuando se arrastra
cabeza_uno.goto(100,0) # Indicamos la posicion del comienzo de la flecha
cabeza_uno.direction = "stop" # Le indicamos la direccion por donde moverse

#Cabeza de Serpiente - Jugador 2

cabeza_dos = turtle.Turtle() #Creacion de la flecha
cabeza_dos.speed(0) # El dibujo es automatico
cabeza_dos.shape("square") # Cambia la forma de la flecha
cabeza_dos.color("Pink") # Se le indica el color de la flecha
cabeza_dos.penup() # No deja rastro cuando se arrastra
cabeza_dos.goto(-100,0) # Indicamos la posicion del comienzo de la flecha
cabeza_dos.direction = "stop" # Le indicamos la direccion por donde moverse

# Creacion de Comida

comida = turtle.Turtle() # Creacion de a comida 
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,200)

#Cuerpos de la serpientes

segmentos_uno = []
segmentos_dos = []

# Texto de Score 1
texto_uno = turtle.Turtle()
texto_uno.speed(0)
texto_uno.color("White")
texto_uno.penup()
texto_uno.hideturtle() #Esconder la pluma
texto_uno.goto(0,260)
#Write es como un print
texto_uno.write ("Jugador 1: 0       High Score: 0", align = "center" , font=("Courier",14,"normal"))

# Texto de Score 2
texto_dos = turtle.Turtle()
texto_dos.speed(0)
texto_dos.color("White")
texto_dos.penup()
texto_dos.hideturtle() #Esconder la pluma
texto_dos.goto(0,-260)
#Write es como un print
texto_dos.write ("Jugador 2: 0       High Score: 0", align = "center" , font=("Courier",14,"normal"))



#Instrucciones de movimientos

movimientos = turtle.Turtle()
movimientos.speed(0)
movimientos.color("white")
movimientos.penup()
movimientos.hideturtle()
movimientos.goto(0,-150)
movimientos.write("Jugador 2 : W - S - A - D        Jugador 1: Up - Down - Rigth - Left" , align = "center" , font =("Courier" , 10 , "normal"))

#Segundos antes de comenzar

segundo_uno = turtle.Turtle()
segundo_uno.speed(0)
segundo_uno.color("white")
segundo_uno.goto(0,0)
segundo_uno.hideturtle()
segundo_uno.penup()
segundo_uno.write("1" , align= "center" , font= ("Courier" , 130 , "normal"))
time.sleep(1)
segundo_uno.undo() # dehase la ultima accion de la tortuga

segundo_dos = turtle.Turtle()
segundo_dos.speed(0)
segundo_dos.color("white")
segundo_dos.goto(0,0)
segundo_dos.hideturtle()
segundo_dos.penup()
segundo_dos.write("2" , align= "center" , font= ("Courier" , 130 , "normal"))
time.sleep(1)
segundo_dos.undo() # dehase la ultima accion de la tortuga

segundo_tres = turtle.Turtle()
segundo_tres.speed(0)
segundo_tres.color("white")
segundo_tres.goto(0,0)
segundo_tres.hideturtle()
segundo_tres.penup()
segundo_tres.write("3" , align= "center" , font= ("Courier" , 130 , "normal"))
time.sleep(1)
segundo_tres.undo() # dehase la ultima accion de la tortuga

FIGTH = turtle.Turtle()
FIGTH.speed(0)
FIGTH.color("white")
FIGTH.goto(0,0)
FIGTH.hideturtle()
FIGTH.penup()
FIGTH.write("FIGTH" , align= "center" , font= ("Courier" , 130 , "normal"))
time.sleep(1)
FIGTH.undo() # dehase la ultima accion de la 

movimientos.undo()


#
# 
# #
# #
# # No terminado
# Funcion de laberinto
"""def laberinto():
    laberinto = turtle.Turtle()
    laberinto.speed(0)
    laberinto("Red")
    laberinto.goto()
    laberinto.penup()
    time.sleep(10)"""
 

#Funciones de direccion Jugador 1

# AL activar algunas de estas funciones la direccion de la flecha se direccionara a la misma


def arriba_uno(): 
    cabeza_uno.direction = "up"
def abajo_uno():
    cabeza_uno.direction = "down"
def derecha_uno():
    cabeza_uno.direction = "rigth"
def izquierda_uno():
    cabeza_uno.direction = "left"

#Funciones de direccion Jugador 2
def arriba_dos():
    cabeza_dos.direction = "up"
def abajo_dos():
    cabeza_dos.direction = "down"
def derecha_dos():
    cabeza_dos.direction = "rigth"
def izquierda_dos():
    cabeza_dos.direction = "left"


#Funciones de movimientos Jugador 1

def mov_uno():
    if cabeza_uno.direction == "up": # Funcion para moverse hacia arriba
        y = cabeza_uno.ycor() # Pide la cordenada de la cabeza en Y
        cabeza_uno.sety(y + 20) # La cabeza_uno se mueve de la cordenada 20 pixeles
    
    if cabeza_uno.direction == "down": # Funcion para moverse hacia ABAJO
        y = cabeza_uno.ycor() # Pide la cordenada de la cabeza_uno en Y
        cabeza_uno.sety(y -  20) # La cabeza_uno se mueve de la cordenada 20 pixeles

    if cabeza_uno.direction == "rigth": # Funcion para moverse hacia la DERECHA
        x = cabeza_uno.xcor() # Pide la cordenada de la cabeza_uno en X
        cabeza_uno.setx(x + 20) # La cabeza_uno se mueve de la cordenada 20 pixeles
        
    if cabeza_uno.direction == "left": # Funcion para moverse hacia la IZQUIERDA
        x = cabeza_uno.xcor() # Pide la cordenada de la cabeza_uno en X
        cabeza_uno.setx(x - 20) # La cabeza se mueve de la cordenada 20 pixeles

# Funciones de movimientos Jugador 2

def mov_dos():
    if cabeza_dos.direction == "up": # Funcion para moverse hacia arriba
        y = cabeza_dos.ycor() # Pide la cordenada de la cabeza en Y
        cabeza_dos.sety(y + 20) # La cabeza_dos se mueve de la cordenada 20 pixeles
    
    if cabeza_dos.direction == "down": # Funcion para moverse hacia ABAJO
        y = cabeza_dos.ycor() # Pide la cordenada de la cabeza_dos en Y
        cabeza_dos.sety(y -  20) # La cabeza_dos se mueve de la cordenada 20 pixeles

    if cabeza_dos.direction == "rigth": # Funcion para moverse hacia la DERECHA
        x = cabeza_dos.xcor() # Pide la cordenada de la cabeza_dos en X
        cabeza_dos.setx(x + 20) # La cabeza_dos se mueve de la cordenada 20 pixeles
        
    if cabeza_dos.direction == "left": # Funcion para moverse hacia la IZQUIERDA
        x = cabeza_dos.xcor() # Pide la cordenada de la cabeza_dos en X
        cabeza_dos.setx(x - 20) # La cabeza se mueve de la cordenada 20 pixeles


# Teclado

window.listen() # Verificar los eventos del teclado

# Corremos la funcion arriba si apretamos la tecla "Up"

#onkeypress genera una respuesta cada vez que tocamos una tecla

#Teclado Jugador Numero 1

window.onkeypress(arriba_uno, "Up") # Se mueve hacia arriba
window.onkeypress(abajo_uno, "Down") # Se mueve hacia abajo
window.onkeypress(derecha_uno, "Right") # Se mueve hacia la derecha
window.onkeypress(izquierda_uno, "Left") # Se mueve hacia la izquierda

#Teclado Jugador Numero 2

window.onkeypress(arriba_dos, "w") # Se mueve hacia arriba
window.onkeypress(abajo_dos, "s") # Se mueve hacia abajo
window.onkeypress(derecha_dos, "d") # Se mueve hacia la derecha
window.onkeypress(izquierda_dos, "a") # Se mueve hacia la izquierda

while True: # Bucle principal del juego
    window.update() # Actualizacion del bucle

    # Colisiones bordes Jugador 1
    if cabeza_uno.xcor() > 280 or cabeza_uno.xcor() < -280 or cabeza_uno.ycor() > 280 or cabeza_uno.ycor() < -280:
        time.sleep(1)
        cabeza_uno.goto(100,0)
        cabeza_uno.direction = "stop" 

        #Esconder los segmentos
        for segmento in segmentos_uno:
            segmento.goto(1000,1000)

        #Limpiar segmentos_uno
        segmentos_uno.clear()

        #Resetear marcador
        Score_uno = 0
        texto_uno.clear()
        texto_uno.write ("Jugador 1: {}       High Score: {}".format(Score_uno,High_uno), align = "center" , font=("Courier",14,"normal"))

    # Colisiones bordes Jugador 2
    if cabeza_dos.xcor() > 280 or cabeza_dos.xcor() < -280 or cabeza_dos.ycor() > 280 or cabeza_dos.ycor() < -280:
        time.sleep(1)
        cabeza_dos.goto(-100,0)
        cabeza_dos.direction = "stop" 

        #Esconder los segmentos
        for segmento in segmentos_dos:
            segmento.goto(1000,1000)

        #Limpiar segmentos_uno
        segmentos_dos.clear()

        #Resetear marcador
        Score_dos = 0
        texto_dos.clear()
        texto_dos.write ("Jugador 2: {}       High Score: {}".format(Score_dos,High_dos), align = "center" , font=("Courier",14,"normal"))

        



    # Comida jugador 1
    if cabeza_uno.distance(comida) < 20: # Vamos a verificar la distancia que hay entre la cabeza_uno y la comida
        
        x = random.randint(-280 ,280) # Indicamos un parametro aleatorio para el ejex entre los pixeles que pasamos como segundo
        y = random.randint(-280 ,280)
        comida.goto(x,y)

        nuevo_segmento_uno = turtle.Turtle() #Se crea la cola de la serpiente
        nuevo_segmento_uno.speed(0)
        nuevo_segmento_uno.shape("square")
        nuevo_segmento_uno.color("Grey")
        nuevo_segmento_uno.penup()
        segmentos_uno.append(nuevo_segmento_uno)

        #Aumentar marcador

        Score_uno += 10

        if Score_uno > High_uno:
            High_uno = Score_uno

        texto_uno.clear()
        texto_uno.write ("Jugador 1: {}       High Score: {}".format(Score_uno,High_uno), align = "center" , font=("Courier",14,"normal"))

    #Comida Jugador 2

    if cabeza_dos.distance(comida) < 20: # Vamos a verificar la distancia que hay entre la cabeza_dos y la comida
        
        x = random.randint(-280 ,280) # Indicamos un parametro aleatorio para el ejex entre los pixeles que pasamos como segundo
        y = random.randint(-280 ,280)
        comida.goto(x,y)

        nuevo_segmento_dos = turtle.Turtle() #Se crea la cola de la serpiente
        nuevo_segmento_dos.speed(0)
        nuevo_segmento_dos.shape("square")
        nuevo_segmento_dos.color("Grey")
        nuevo_segmento_dos.penup()
        segmentos_dos.append(nuevo_segmento_dos)

        #Aumentar marcador

        Score_dos += 10

        if Score_dos > High_dos:
            High_dos = Score_dos

        texto_dos.clear()
        texto_dos.write ("Jugador 2: {}       High Score: {}".format(Score_dos,High_dos), align = "center" , font=("Courier",14,"normal"))

    #Colisiones con el cuerpo Jugador 1

    for segmento1 in segmentos_uno:
        if segmento1.distance(cabeza_uno) < 20:
            time.sleep(1)
            cabeza_uno.goto(100,0)
            cabeza_uno.direction = "stop"

            #Esconder los segmentos_uno
            for segmento1 in segmentos_uno:
                segmento1.goto(1000,1000)
            
            #Resetear marcador
            segmentos_uno.clear()
            Score_uno = 0
            texto_uno.clear()
            texto_uno.write ("Jugador 1: {}       High Score: {}".format(Score_uno,High_uno), align = "center" , font=("Courier",14,"normal"))

        #Colision entre jugador 2 contra el 1    
        if segmento1.distance(cabeza_dos) < 20:
            time.sleep(1)
            cabeza_dos.goto(-100,0)
            cabeza_dos.direction = "stop"

            for segmento2 in segmentos_dos:
                segmento2.goto(1000,1000)

            segmentos_dos.clear()
            Score_dos = 0
            texto_dos.clear()
            texto_dos.write ("Jugador 2: {}       High Score: {}".format(Score_dos,High_dos), align = "center" , font=("Courier",14,"normal"))
    
    #Colisiones con el cuerpo Jugador 2
    
    for segmento2 in segmentos_dos:
        if segmento2.distance(cabeza_dos) < 20:
            time.sleep(1)
            cabeza_dos.goto(-100,0)
            cabeza_dos.direction = "stop"

            #Esconder los segmentos_uno
            for segmento2 in segmentos_dos:
                segmento2.goto(2000,1000)
            
            #Resetear marcador
            segmentos_dos.clear()
            Score_dos = 0
            texto_dos.clear()
            texto_dos.write ("Jugador 2: {}       High Score: {}".format(Score_dos,High_dos), align = "center" , font=("Courier",14,"normal"))

     #Colision entre jugador 1 contra el 2    
        if segmento2.distance(cabeza_uno) < 20:
            time.sleep(1)
            cabeza_uno.goto(100,0)
            cabeza_uno.direction = "stop"

            for segmento1 in segmentos_uno:
                segmento1.goto(1000,1000)

            segmentos_uno.clear()
            Score_uno = 0
            texto_uno.clear()
            texto_uno.write ("Jugador 1: {}       High Score: {}".format(Score_uno,High_uno), align = "center" , font=("Courier",14,"normal"))

    


    #Mover el cuerpo de la serpiente Jugador 1

    totalseg_uno = len(segmentos_uno) # Verificamos cuantos segmentos_uno hay en la lista
    for index1 in range(totalseg_uno -1 ,0 ,-1):
        x = segmentos_uno[index1 - 1].xcor() # Pedimos la coordenada X del segmento2
        y = segmentos_uno[index1 - 1].ycor() # Pedimos la coordenada Y del segmento
        segmentos_uno[index1].goto(x,y) # Nos movemos

    if totalseg_uno > 0: 
        x = cabeza_uno.xcor()
        y = cabeza_uno.ycor()
        segmentos_uno[0].goto(x,y)


    #Mover el cuerpo de la serpiente Jugador 2

    totalseg_dos = len(segmentos_dos) # Verificamos cuantos segmentos_dos hay en la lista
    for index2 in range (totalseg_dos -1 ,0 ,-1):
        x = segmentos_dos[index2 - 1].xcor() # Pedimos la coordenada X del segmento
        y = segmentos_dos[index2 - 1].ycor() # Pedimos la coordenada Y del segmento
        segmentos_dos[index2].goto(x,y) # Nos movemos

    if  totalseg_dos > 0: 
        x = cabeza_dos.xcor()
        y = cabeza_dos.ycor()
        segmentos_dos[0].goto(x,y)

    mov_uno() # Jugador 1
    mov_dos() # Jugador 2
    

    time.sleep(posponer) # Ejecutacion de la funcion con un segundo de posposicion


# AUTOR: MATIAS DIAZ DE OTAZU
