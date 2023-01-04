#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *

from funcionesVACIAS import *

#Funcion principal
def main():

        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()
        #Preparar la ventana
        pygame.display.set_caption("La escondida...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        termino=0
        esigual=0
        pantallaFin=0
        palabraUsuario = ""
        nombreUsuario=""
        ListaUsuarios=[]
        listaPalabrasDiccionario=[]
        ListaDePalabrasUsuario = [] #Aca guardo las palabras que ya ingreso el usuario.
        PalabrasAcertadas=[] #Aca guardo todas las palabras acertadas
        correctas = []
        incorrectas = []
        casi = []
        gano = False

        archivo= open("lemario.txt","r")
        #lectura del diccionario
        lectura(archivo, listaPalabrasDiccionario, LARGO)
        print(listaPalabrasDiccionario)

        #elige una al azar
        palabraCorrecta=nuevaPalabra(listaPalabrasDiccionario) #Usa la funcion nuevaPalabra y le carga la listaPalabrasDiccionario para que elija una al azar.
        print(palabraCorrecta)
        dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos,segundos, gano, correctas, incorrectas, casi,palabraCorrecta,PalabrasAcertadas,termino)
        intentos = 5
        while segundos > 55:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra #es la palabra que escribe el usuario

                    #PALABRA DEL USUARIO REPETIDA (OPCIONAL SIN REPETIDOS)

                    for i in range(len(ListaDePalabrasUsuario)):
                        if palabraUsuario==ListaDePalabrasUsuario[i]: #Si la palabra que ingreso el usuario, coincide con una de las anteriores
                            esigual=1
                        else:
                            esigual=0

                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]

                    if e.key == K_RETURN and esigual==0:
                            #falta hacer un control para que sea una palabra de la longitud deseada
                            #falta controlar que la palabra este en el diccionario
                            gano = revision(palabraCorrecta, palabraUsuario, correctas, incorrectas, casi)
                            ListaDePalabrasUsuario.append(palabraUsuario)

                            #OPCIONAL TOTALMENTE POR TIEMPO.

                            if gano:
                                PalabrasAcertadas.append(palabraUsuario)
                                print(PalabrasAcertadas)
                                ListaDePalabrasUsuario=[] #Hago que se vacie la lista de palabras ingresadas
                                correctas = []
                                incorrectas = []
                                casi = []
                                puntos=puntos+1 #Sumo un punto
                                palabraCorrecta=nuevaPalabra(listaPalabrasDiccionario)
                                print(palabraCorrecta)

                            palabraUsuario = "" #Hago que se vacie lo que escribio el usuario.
                          #  intentos -= 1



            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos,segundos, gano, correctas, incorrectas, casi,palabraCorrecta,PalabrasAcertadas,termino)
            pygame.display.flip()


#PANTALLA INGRESE NOMBRE USUARIO

        pantallaFinal(screen,ListaUsuarios,nombreUsuario)
        while pantallaFin==0:

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    nombreUsuario += letra #es la palabra que escribe el usuario



                    if e.key == K_BACKSPACE:
                        nombreUsuario = nombreUsuario[0:len(nombreUsuario)-1]

                    if e.key == K_RETURN:
                            #gano = revision(palabraCorrecta, palabraUsuario, correctas, incorrectas, casi)
                            ListaUsuarios.append(nombreUsuario)
                            pantallaFin=1

            #Dibujar de nuevo todo
            pantallaFinal(screen,ListaUsuarios,nombreUsuario)
            pygame.display.flip()

        #SE ACABO EL TIEMPO

        if len(PalabrasAcertadas)>0:
            termino=1
        else:
            termino=2

        screen.fill(COLOR_FONDO)
        dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos,segundos, gano, correctas, incorrectas, casi,palabraCorrecta,PalabrasAcertadas,termino)
        pygame.display.flip()


        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

        archivo.close()
#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
