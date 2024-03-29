import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SLASH:
        return("-")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def pantallaFinal(screen,ListaUsuarios,nombreUsuario):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    #IMAGEN DE FONDO
    background = pygame.image.load("fondo.jpg").convert() #cargo la imagen de fondo
    screen.blit(background, [0,0]) #Coloco la posicion

    #TEXTO PARA PEDIRLE EL NOMBRE EN PANTALLA
    defaultFontGrande2= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE2) #Asigno la fuente.
    screen.blit(defaultFontGrande2.render("INGRESE SU NOMBRE", 1, COLOR_NARANJA), (240, 250)) #Muestro en pantalla el mensaje de que gano.

    #Linea Horizontal
    pygame.draw.line(screen, (255, 165, 0), (250, ALTO-250) , (500, ALTO-250), 2)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(nombreUsuario, 1, COLOR_TEXTO), (350, 330))



def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano,
                correctas, incorrectas, casi,palabraCorrecta,PalabrasAcertadas,termino):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFont2= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA2)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    #IMAGEN DE FONDO
    background = pygame.image.load("fondo.jpg").convert() #cargo la imagen de fondo
    screen.blit(background, [0,0]) #Coloco la posicion

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (600, ALTO-70) , (200, ALTO-70), 5)
    #muestra lo que escribe el jugador
    screen.blit(defaultFont2.render(palabraUsuario, 1, COLOR_TEXTO), (350, 490))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra las palabras anteriores, las que se fueron arriesgando
    pos = 0

    for palabra in listaDePalabrasUsuario:
        screen.blit(defaultFontGrande.render(palabra, 1, COLOR_LETRAS), (ANCHO//2-len(palabra)*TAMANNO_LETRA_GRANDE//4,20 + 80 * pos))
        pos += 1

    #muestra el abcdario, falta ponerle color a las letras
    abcdario = ["qwertyuiop", "asdfghjklm", "zxcvbnm"]
    y=0
    for abc in abcdario:
        x = 0
        for letra in abc:
            color = COLOR_LETRAS
            x += TAMANNO_LETRA
            #SI LA LETRA ES CORRECTA

            for letra2 in correctas: #Recorro las letras correctas
                 if letra==letra2: #Si la letra correcta, coincide con la letra en abcdario
                  color = COLOR_AZUL #Reemplazo por el color azul

            #SI LA LETRA ES INCORRECTA
            for letra3 in incorrectas: #Recorro las letras incorrectas
                 if letra==letra3: #Si las letra incorrecta, coincide con la letra en abcdario
                  color = COLOR_TIEMPO_FINAL #Reemplazo por el color rojo
            screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
        y += TAMANNO_LETRA

    #GANAR JUEGO
    if termino==1:

        screen.fill(COLOR_FONDO) #Limpia la pantalla anterior, la deja en negro.
        #IMAGEN DE FONDO
        background = pygame.image.load("ganaste.jpg").convert() #cargo la imagen de fondo
        screen.blit(background, [0,-20]) #Coloco la posicion

        defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE) #Asigno la fuente.
        defaultFontGrande2= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE2) #Asigno la fuente.
        mostrarpalabra="Usted acerto: "+str(puntos)+" palabras"

        #MUESTRA EN PANTALLA EL MENSAJE GANO
        screen.blit(defaultFontGrande.render("GANASTEE!", 1, COLOR_NARANJA), (180, 50)) #Muestro en pantalla el mensaje de que gano.
        screen.blit(defaultFontGrande2.render(mostrarpalabra, 1, COLOR_TIEMPO_FINAL), (220, 150))

    #PERDER JUEGO
    if len(listaDePalabrasUsuario)==5 and not(gano) or termino==2: #Si el usuario hizo 5 intentos, pierde.
        screen.fill(COLOR_FONDO) #Limpia la pantalla anterior, la deja en negro.

        #IMAGEN DE FONDO
        background = pygame.image.load("perdiste.jpg").convert() #cargo la imagen de fondo
        screen.blit(background, [0,-20]) #Coloco la posicion

        #SONIDO CUANDO PIERDE
        pygame.mixer.music.load("derrota.mp3")
        pygame.mixer.music.play()

        defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE) #Asigno la fuente.
        defaultFontGrande2= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE2) #Asigno la fuente.
        mostrarpalabra="La palabra correcta es: "+palabraCorrecta.upper()

        #MUESTRA EN PANTALLA EL MENSAJE PERDIO
        screen.blit(defaultFontGrande.render("PERDIO :(", 1, COLOR_NARANJA), (180, 50)) #Muestro en pantalla el mensaje de que gano.
        screen.blit(defaultFontGrande2.render(mostrarpalabra, 1, COLOR_TIEMPO_FINAL), (220, 150))








