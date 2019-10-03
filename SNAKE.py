

import pygame
import time
import os, pygame
import random
import sys

def load_image(name):
    path = os.path.join('', name)
    return pygame.image.load(path).convert()

pygame.init()

icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)


Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
Azul = (0, 0, 255)
Verde = (0, 128, 0)
Morado = (170,0,170)


ancho = 800
altura = 500


superficie = pygame.display.set_mode((ancho,altura))
pygame.display.set_caption('SNAKE')


background = load_image('selva.png')

superficie.blit(background, [0, 0])


reloj = pygame.time.Clock()

serp_tamano = 20


font = pygame.font.SysFont("arial.ttf", 30)
      

def pausa():
    pausado = True
   
    while pausado:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        background = load_image('selva_pause.png')
        superficie.blit(background, [0, 0])
        #superficie.fill(blanco)      
        message_to_screen("Pausa", Negro, -50)
        message_to_screen("Para continuar presione C. Para terminar presione Q", Rojo, 50)
        pygame.display.update()
        reloj.tick(5)


def puntos(score):
    text = font.render("Puntos: "+str(score), True, Negro)
    superficie.blit(text, [0,0])

def Velocidad(speed):
    text = font.render("Velocidad: "+str(speed), True, Negro)
    superficie.blit(text, [200,0])

def intro_juego():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        background = load_image('selva_inicio.png')
        superficie.blit(background, [0, 0])
        message_to_screen("Bienvenid@", Negro, -150)
        message_to_screen("El objetivo del juego es controlar una serpiente usando", Azul, -90)
        message_to_screen("teclas flechas de movimiento para comer manzanas", Azul, -60)
        message_to_screen("Manzanas Rojas: serpiente +1, puntaje +1, cada 3 puntos velocidad +1 .", Rojo, -30)
        message_to_screen("Manzanas Lilas: Serpiente +10, puntaje +1", Morado, 0)
        message_to_screen("Manzanas Verdes: Rapidez +1, puntaje +1", Verde, 30)
        message_to_screen("Si la serpiente toca el borde o se toca a si misma, pierdes.", Negro, 60)
        message_to_screen("Para pausar partida, presiona tecla P.", Azul, 90)
        message_to_screen("Para Iniciar partida, presiona tecla C.", Azul, 120)
        message_to_screen("Para terminar de jugar y salir, presiona tecla Q.", Azul, 150)
        pygame.display.update()
        reloj.tick(15)

def serpiente(serp_tamano, listaSerpiente):
     
    for i in listaSerpiente:
        pygame.draw.rect(superficie, Negro, [i[0],i[1],serp_tamano,serp_tamano])

def text_objetos(text, color):
    textSuperficie = font.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()

def message_to_screen(msg, color, y_displace=0):
    textSur, textRect = text_objetos(msg, color)
    textRect.center = (ancho/2), (altura/2)+ y_displace
    superficie.blit(textSur, textRect)


    
    
def gameLoop():

    cuentarojas = 0
    CPS = 15

    gameExit = False
    gameOver = False

    mover_x = 300
    mover_y = 300

    mover_x_cambio = 0
    mover_y_cambio = 0

    listaSerpiente = []
    largoSerpiente = 1

#Manzana Roja
    azarManzana_01_X = round(random.randrange(0, 300 - 20)/20.0)*20.0
    azarManzana_01_Y = round(random.randrange(0, 300 - 20)/20.0)*20.0

#Manzana Verde
    azarManzana_02_X = round(random.randrange(0, 300 - 20)/20.0)*20.0
    azarManzana_02_Y = round(random.randrange(0, 300 - 20)/20.0)*20.0

#Manzana Lila
    azarManzana_03_X = round(random.randrange(0, 300 - 20)/20.0)*20.0
    azarManzana_03_Y = round(random.randrange(0, 300 - 20)/20.0)*20.0

    pulsar_sonido = pygame.mixer.Sound("snake_Song.ogg")
    pulsar_sonido.set_volume(0.50)
    pulsar_sonido.play(18)
    

    
    while not gameExit:

        while gameOver == True:


      
            
            superficie.blit(background, [0, 0])
            pulsar_sonido.stop()
            message_to_screen("Game Over", Negro, -50)
            message_to_screen("Para continuar presione C. Para terminar presione Q", Rojo, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    


    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mover_x_cambio = -serp_tamano
                    mover_y_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    mover_x_cambio = serp_tamano
                    mover_y_cambio = 0
                elif event.key == pygame.K_UP:
                    mover_y_cambio = -serp_tamano
                    mover_x_cambio = 0
                elif event.key == pygame.K_DOWN:
                    mover_y_cambio = serp_tamano
                    mover_x_cambio = 0   
                elif event.key == pygame.K_p:
                    pulsar_sonido.set_volume(0.0)
                    pausa()
                    pulsar_sonido.set_volume(0.50)


                     
                
        if mover_x >= ancho or mover_x < 0 or mover_y >= altura or mover_y < 0:
            
            pygame.mixer.music.load("dead-Song.ogg")
            pygame.mixer.music.play(1)
            gameOver = True
            pygame.mixer.music.stop


        mover_x += mover_x_cambio
        mover_y += mover_y_cambio
      
        superficie.blit(background, [0, 0])

        pygame.draw.rect(superficie, Rojo, [azarManzana_01_X, azarManzana_01_Y, 20, 20])

        pygame.draw.rect(superficie, Verde, [azarManzana_02_X, azarManzana_02_Y, 20, 20])

        pygame.draw.rect(superficie, Morado, [azarManzana_03_X, azarManzana_03_Y, 20, 20])

        cabezaSerpiente = []
        cabezaSerpiente.append(mover_x)
        cabezaSerpiente.append(mover_y)
        listaSerpiente.append(cabezaSerpiente)
        if len(listaSerpiente) > largoSerpiente:
            del listaSerpiente[0]

        for eachSegment in listaSerpiente[:-1]:
            if eachSegment == cabezaSerpiente:
                pygame.mixer.music.load("dead-Song.ogg")
                pygame.mixer.music.play(1)
                gameOver = True
                pygame.mixer.music.stop


        serpiente(serp_tamano,listaSerpiente)
        puntos(largoSerpiente-1)
        Velocidad(CPS -15)# se restan 15 para que contador no tome en cuenta el valor inical que es de 15 y comience de 0
        pygame.display.update()

        

        if mover_x == azarManzana_01_X and mover_y == azarManzana_01_Y:
            pygame.mixer.music.load("Eat01-Song.ogg")
            azarManzana_01_X = round(random.randrange(0, ancho -20)/20.0)*20.0
            azarManzana_01_Y = round(random.randrange(0, altura -20)/20.0)*20.0
            largoSerpiente += 1
            cuentarojas += 1
            if cuentarojas % 3 == 0:
                CPS += 1
            
            pygame.mixer.music.play(0)
            
       

        if mover_x == azarManzana_02_X and mover_y == azarManzana_02_Y:
            pygame.mixer.music.load("Eat02-Song.ogg")
            azarManzana_02_X = round(random.randrange(0, ancho -20)/20.0)*20.0
            azarManzana_02_Y = round(random.randrange(0, altura -20)/20.0)*20.0
            largoSerpiente += 1
            CPS +=1
            
            pygame.mixer.music.play(0)
            


        if mover_x == azarManzana_03_X and mover_y == azarManzana_03_Y:
            pygame.mixer.music.load("Eat03-Song.ogg")
            azarManzana_03_X = round(random.randrange(0, ancho -20)/20.0)*20.0
            azarManzana_03_Y = round(random.randrange(0, altura -20)/20.0)*20.0
            largoSerpiente += 10
            
            pygame.mixer.music.play(0)
            

        reloj.tick(CPS)


    pygame.quit()
    sys.exit()

intro_juego()
gameLoop()
