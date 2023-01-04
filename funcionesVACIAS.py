from principal import *
from configuracion import *
from random import choice
import random
import math



def nuevaPalabra(lista):
    random=choice(lista) #Recibe una lista y de la lista devuelve un elemento al azar.
    return random

def lectura(archivo, salida, largo): #Lee el archivo que fue abierto y carga en la salida solo las palabras que tengan la longitud indicada por largo.

#LECTURA DEL ARCHIVO Y ARMADO DE LA CADENA

    contenido=archivo.read() #Leo el archivo, y guardo el contenido del documento.
    largo=4
    listarchivo=[]
    cadenavacia=""
    cadenasinsalto=""
    for letra in contenido: #Recorro el contenido del archivo.
        cadenavacia=cadenavacia+letra #Armo una cadena
        if letra=="\n": #Si llega al elemento de salto de linea "\n"
            for quitar in cadenavacia: #Recorro la cadenavacia para quitar los saltos de linea
                if quitar!="\n": #Si los elementos son distintos del salto de linea, armo una cadena con la palabra sin el salto de linea.
                 cadenasinsalto=cadenasinsalto+quitar
            listarchivo.append(cadenasinsalto) #Armo una lista con las palabras.
            cadenavacia="" #Vuelvo a vaciar la cadena para que en la siguiente iteracion comience con la sig palabra.
            cadenasinsalto="" #Vuelvo a vaciar la cadena para que en la siguiente iteracion comience con la sig palabra.

#SALIDA DE PALABRAS CON LIMITE DE LONGITUD

    for i in range(len(listarchivo)): #Hago que i recorra desde el elemento 0 hasta la longitud de la lista.
        longitudpalabra=len(listarchivo[i]) #Obtengo la longitud de la palabra en el index que me estoy ubicando.
        if longitudpalabra==largo: #Si la longitud de la palabra es igual al rango indicado.
            salida.append(listarchivo[i]) #Cargo en la salida la palabra.



def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):


#ESTA LA LETRA EN LA PALABRA CORRECTA

    def esta(letra): #Toma la letra a comparar como parametro
         for char3 in palabraCorrecta:
             if letra==char3:
                return True  #Si la letra de la palabra del usuario, coincide con alguna de la palabraCorrecta, devuelvo true.

# SI LA LETRA SE REPITE EN LA LISTA CORRECTAS

    def repetidaCorrectas(letra,correctas):
         if len(correctas)==0: #Si la lista esta vacia, devolver true.
            return True
         for char5 in correctas: #Recorro los elementos de la lista correctas
            if letra==char5: #Si coincide la letra, con la letra de la lista correctas, devolver false.
                return False
         return True

# SI LA LETRA SE REPITE EN LA LISTA INCORRECTAS

    def repetidaIncorrectas(letra,incorrectas):
         if len(incorrectas)==0: #Si la lista esta vacia, devolver true.
            return True
         for char6 in incorrectas: #Recorro los elementos de la lista incorrectas
            if letra==char6: #Si coincide la letra, con la letra de la lista incorrectas, devuelvo false.
                return False
         return True


#LISTA CON LETRAS CORRECTAS

    for char2 in palabra: #Recorro la palabra ingresada por el usuario.
         if esta(char2) and repetidaCorrectas(char2,correctas): #Si coincide con las letras de la palabra correcta
            correctas.append(char2) #Cargo en la lista las letras correctas.

#LISTA CON LETRAS INCORRECTAS

    for char4 in palabra: #Recorro la palabra ingresada por el usuario.
         if not esta(char4) and repetidaIncorrectas(char4,incorrectas): #Si no coincide con las letras de la palabra correcta
            incorrectas.append(char4) #Cargo en la lista las letras incorrectas.


#EFECTOS DE SONIDOS (OPCIONAL)

    #SONIDO SI HAY AL MENOS UNA CORRECTA.

    if len(correctas)>=1 and palabraCorrecta!=palabra:
        pygame.mixer.music.load("acierto.mp3")
        pygame.mixer.music.play()

     #SONIDO SI TODAS SON INCORRECTAS

    if len(correctas)==0:
        pygame.mixer.music.load("error.mp3")
        pygame.mixer.music.play()

    #SONIDO CUANDO GANA
    if palabraCorrecta==palabra:
        pygame.mixer.music.load("victoria.mp3")
        pygame.mixer.music.play()

#GANA O NO

    if palabraCorrecta==palabra:
         return True
    else:
        return False









