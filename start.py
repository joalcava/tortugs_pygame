#! /usr/bin/python3

"""
 Juego de plataformas: 'Tortugs'
 -----------------------------------
 Jose Alejandro Cardona Valdes.
 Sergio
 Diego
 -----------------------------------
 Universidad Tecnológica de Pereira
 2017-2
"""

import sys
import time

import pygame

import constants as const
import platforms

from pygame.locals import *
from levels import Nivel1, Nivel2, Nivel3
from constants import Color
from player import Player
from menu import Menu

_sonidos = {}
_imagenes = {}


def cargar_sonidos():
    if not _sonidos:
        _sonidos["ataque"] = pygame.mixer.Sound('audio/throw.wav')
    return _sonidos


def cargar_imagenes():
    if not _imagenes:
        _imagenes["cargando"] = pygame.image.load("imagen/cargando-fondo.jpg")
        _imagenes["vida"] = pygame.image.load("imagen/vidas.png").convert_alpha()
        _imagenes["shuriken"] = pygame.image.load("imagen/shuriken/shuriken1.png").convert_alpha()
    return _imagenes


def jugar():
    sonidos = cargar_sonidos()
    imagenes = cargar_imagenes()

    pantalla.blit(imagenes["cargando"], (0, 0))
    pygame.display.flip()

    fin = False
    player = Player()
    niveles = [Nivel1(player), Nivel2(player), Nivel3(player)]
    nivel_actual = niveles[0]
    player_group = pygame.sprite.Group()
    player.level = nivel_actual
    player.rect.x = 250
    player.rect.y = const.ALTO_PANTALLA - player.rect.height - 60

    player_group.add(player)

    imagen_piedra = pygame.image.load("imagen/shuriken/shuriken1.png").convert_alpha()

    clock = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            # Salir
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:

                # Izquierda
                if event.key == pygame.K_LEFT:
                    player.mover_izquierda()

                # Derecha
                if event.key == pygame.K_RIGHT:
                    player.mover_derecha()

                # Salto
                if event.key == pygame.K_UP:
                    player.saltar()

                # Ataque de espada
                if event.key == pygame.K_z:
                    if player.atacando == False:
                        sonidos["ataque"].play()
                        player.atacar()

                # Lanzar shuriken
                if event.key == pygame.K_SPACE:
                    if player.piedra > 0:
                        bala = platforms.Bala('imagen/shuriken/shuriken1.png')
                        bala.direccion = player.direccion
                        bala.jugador = 1
                        if player.direccion == "R":
                            bala.rect.x = player.rect.x + 50
                            bala.rect.y = player.rect.y + 45
                        else:
                            bala.rect.x = player.rect.x - 5
                            bala.rect.y = player.rect.y + 45
                        nivel_actual.lista_bala.add(bala)
                        player.piedra -= 1

                # Pausar
                if event.key == pygame.K_ESCAPE:
                    ter = False
                    fuente = pygame.font.Font('fuentes/ninja-turtles-regular.otf', 80)
                    texto = fuente.render("PAUSA", True, Color.BLANCO)
                    pantalla.blit(texto, (40, const.ALTO_PANTALLA / 2 - 100))
                    pygame.display.flip()
                    fuente = pygame.font.Font('fuentes/ninja-turtles-regular.otf', 30)
                    while not ter:
                        for event in pygame.event.get():  # User did something
                            if event.type == pygame.QUIT:  # If user clicked close
                                ter = True  # Flag that we are done so we exit this loop
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    ter = True
                                if event.key == pygame.K_ESCAPE:
                                    ter = True


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.dx < 0:
                    player.parar()
                if event.key == pygame.K_RIGHT and player.dx > 0:
                    player.parar()















        # Update the player.
        player_group.update()

        # Update items in the level
        nivel_actual.update()

        if player.vida == 0 and player.muerto == False and player.perdio == False:
            player.muerto = True
            player.cont_dead = 0

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            nivel_actual.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            nivel_actual.shift_world(diff)

        # Siguiente nivel
        current_position = player.rect.x + nivel_actual.world_shift
        if current_position < nivel_actual.level_limit:
            player.rect.x = 120
            if nivel_actual.id < len(niveles) - 1:
                fuente = pygame.font.Font('fuentes/ninja-turtles-regular.otf', 80)
                texto = fuente.render("YOU WIN!", True, Color.VERDE)
                pantalla.blit(texto, (40, const.ALTO_PANTALLA / 2 - 100))

                pygame.display.flip()
                time.sleep(4)
                fuente = pygame.font.Font('fuentes/ninja-turtles-regular.otf', 20)
                nivel_actual.id += 1
                if nivel_actual.id == 3:
                    nivel_actual.id += 1
                nivel_actual = niveles[nivel_actual.id + 1]
                player.level = nivel_actual
                player.rect.x = 250
                player.vida = 3
                player.piedra = 5
            current_position = player.rect.x + nivel_actual.world_shift
        if nivel_actual.id == 4 and len(nivel_actual.enemy_list) == 0:
            fuente = pygame.font.Font('fuentes/ninja-turtles-regular.otf', 80)
            texto = fuente.render("GANASTE", True, Color.VERDE)
            pantalla.blit(texto, (40, const.ALTO_PANTALLA / 2 - 100))
            pygame.display.flip()
            time.sleep(4)
            fin = True

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        nivel_actual.draw(pantalla)
        player_group.draw(pantalla)

        x = 5
        y = 5
        for i in range(player.vida):
            pantalla.blit(imagenes["vida"], (x, y))
            x += 25

        x = 5
        y = 30
        for i in range(player.piedra):
            pantalla.blit(imagen_piedra, (x, y))
            x += 30

        fuente = pygame.font.Font('fuentes/ninja-turtles-regular.otf', 20)
        punto = fuente.render("Puntos: " + str(player.puntos), True, Color.BLANCO)
        pantalla.blit(punto, [const.ANCHO_PANTALLA - 155, 5])

        if player.rect.y > const.ANCHO_PANTALLA:
            ayuda = nivel_actual.world_shift * -1
            if (nivel_actual.id == 2) and ((player.rect.x + ayuda > 300) and (player.rect.x + ayuda < 600)):
                nivel_actual.id = 3
                nivel_actual = niveles[nivel_actual.id]
                player.level = nivel_actual
                player.rect.x = 250
                player.rect.y = 100
            else:
                player.perdio = True

        if player.perdio:
            Perdiste = pygame.image.load('imagen/Perdiste.png').convert_alpha()
            pantalla.blit(Perdiste, (150, 250))
            pygame.display.flip()
            time.sleep(4)
            fin = True

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    return nivel_actual.id, player.perdio


def instrucciones():
    pygame.mouse.set_visible(False)
    pygame.init()
    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(None, 25)
    ver_pag = True
    pag = 1
    terminar = False
    dim = [1100, 630]
    while not terminar and ver_pag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pag += 1
                if pag == 2:
                    ver_pag = False
        pantalla.fill(Color.NEGRO)
        if pag == 1:
            fondo = pygame.image.load('imagen/Instr.jpg')
            fondo = pygame.transform.scale(fondo, dim)
            pantalla.blit(fondo, [0, 0])
            texto = fuente.render('Historia parte 1: ', True, Color.BLANCO)
            pantalla.blit(texto, [10, 10])

        reloj.tick(20)
        pygame.display.flip()


def historia():
    pygame.mouse.set_visible(False)
    pygame.init()
    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(None, 25)
    ver_pag = True
    pag = 1
    terminar = False
    dim = [1100, 630]
    while not terminar and ver_pag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminar = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pag += 1
                if pag == 7:
                    ver_pag = False
        pantalla.fill(Color.NEGRO)
        if pag == 1:
            fondo = pygame.image.load('imagen/h1.png')
            fondo = pygame.transform.scale(fondo, dim)
            pantalla.blit(fondo, [0, 0])
            texto = fuente.render('Historia parte 1: ', True, Color.BLANCO)
            pantalla.blit(texto, [10, 10])

        if pag == 2:
            fondo = pygame.image.load('imagen/night2.png')
            pantalla.blit(fondo, [0, 0])
            texto = fuente.render('Historia parte 1: ', True, Color.BLANCO)
            pantalla.blit(texto, [10, 10])

        if pag == 4:
            fondo = pygame.image.load('imagen/night3.png')
            pantalla.blit(fondo, [0, 0])
            texto = fuente.render('Historia parte 1: ', True, Color.BLANCO)
            pantalla.blit(texto, [10, 10])

        if pag == 3:
            fondo = pygame.image.load('imagen/h2.png')
            fondo = pygame.transform.scale(fondo, dim)
            pantalla.blit(fondo, [0, 0])
            texto = fuente.render('Historia parte 1: ', True, Color.BLANCO)
            pantalla.blit(texto, [10, 10])

        if pag == 5:
            fondo = pygame.image.load('imagen/h3.png')
            fondo = pygame.transform.scale(fondo, dim)
            pantalla.blit(fondo, [0, 0])
            texto = fuente.render('Historia parte 1: ', True, Color.BLANCO)
            pantalla.blit(texto, [10, 10])

        if pag == 6:
            fondo = pygame.image.load('imagen/blablabla.jpg')

            pantalla.blit(fondo, [0, 0])
            texto = fuente.render('Historia parte 1: ', True, Color.BLANCO)
            pantalla.blit(texto, [10, 10])

        reloj.tick(20)
        pygame.display.flip()
        # time.sleep(5)


def salir():
    sys.exit(0)


def creditos():
    pass


if __name__ == '__main__':
    # Inicializadores
    pygame.init()
    pygame.mixer.init(44100, -16, 3, 2048)
    pygame.font.init()
    pygame.display.set_caption("Turtle ninja")

    # Variables
    pantalla = pygame.display.set_mode((const.ANCHO_PANTALLA, const.ALTO_PANTALLA))

    fin = False

    opciones = [
        ("JUGAR", jugar),
        ("HISTORIA", historia),
        ("INSTRUCCIONES", instrucciones),
        ("CREDITOS", creditos),
        ("SALIR", salir)
    ]

    # Iniciar
    menu = Menu(opciones)
    while not fin:
        for e in pygame.event.get():
            if e.type == QUIT:
                fin = True

        menu.actualizar()
        menu.imprimir(pantalla)

        pygame.display.flip()
        pygame.time.delay(10)
