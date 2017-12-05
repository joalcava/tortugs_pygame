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

pygame.init()
pygame.mixer.init(44100, -16, 3, 2048)
pygame.font.init()
pygame.display.set_caption("Turtle ninja")
_pantalla = pygame.display.set_mode((const.ANCHO_PANTALLA, const.ALTO_PANTALLA))

_imagenes = {
    "cargando": pygame.image.load("imagen/cargando-fondo.jpg"),
    "vida": pygame.image.load("imagen/vidas.png").convert_alpha(),
    "shuriken_small": pygame.image.load("imagen/shuriken_small.png").convert_alpha(),
    "perdiste": pygame.image.load("imagen/perdiste.png").convert_alpha(),
    "instrucciones": pygame.image.load('imagen/instrucciones.jpg'),
    "creditos": pygame.image.load('imagen/instrucciones.jpg'),
    "historia1": pygame.image.load('imagen/historia1.jpg'),
    "historia2": pygame.image.load('imagen/historia2.jpg'),
    "historia3": pygame.image.load('imagen/historia3.jpg'),
    "historia4": pygame.image.load('imagen/historia4.jpg'),
}


def cargar_imagenes():
    if not _imagenes:
        _imagenes["cargando"] = pygame.image.load("imagen/cargando-fondo.jpg")
        _imagenes["vida"] = pygame.image.load("imagen/vidas.png").convert_alpha()
        _imagenes["shuriken_small"] = pygame.image.load("imagen/shuriken_small.png").convert_alpha()
        _imagenes["perdiste"] = pygame.image.load("imagen/perdiste.png").convert_alpha()
    return _imagenes


def jugar():
    _pantalla.blit(_imagenes["cargando"], (0, 0))
    pygame.display.flip()

    fin = False
    player = Player()
    niveles = [Nivel1(player), Nivel2(player)]#, Nivel3(player)]
    nivel_actual = niveles[0]
    player_group = pygame.sprite.Group()
    player.nivel_actual = nivel_actual
    player.rect.x = 250
    player.rect.y = const.ALTO_PANTALLA - player.rect.height - 60

    player_group.add(player)

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
                    if player.atacando is False:
                        player.atacar()

                # Lanzar shuriken
                if event.key == pygame.K_SPACE:
                    if player.shurikens > 0:
                        shuriken = platforms.Shuriken(player.direccion, True)
                        if player.direccion == "R":
                            shuriken.rect.x = player.rect.x + 30
                            shuriken.rect.y = player.rect.y + 5
                        else:
                            shuriken.rect.x = player.rect.x - 30
                            shuriken.rect.y = player.rect.y + 5
                        nivel_actual.balas.add(shuriken)
                        player.shurikens -= 1

                # Pausar
                if event.key == pygame.K_ESCAPE:
                    pausa_terminada = False
                    fuente = pygame.font.Font('fuentes/ninja-turtles-regular.otf', 80)
                    texto = fuente.render("PAUSA", True, Color.BLANCO)
                    _pantalla.blit(texto, (40, const.ALTO_PANTALLA / 2 - 100))
                    pygame.display.flip()
                    while not pausa_terminada:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pausa_terminada = True
                                fin = True
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    pausa_terminada = True
                                if event.key == pygame.K_ESCAPE:
                                    pausa_terminada = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.dx < 0:
                    player.parar()
                if event.key == pygame.K_RIGHT and player.dx > 0:
                    player.parar()

        # Actualizacion de grupos
        player_group.update()
        nivel_actual.update()

        # Muerto?
        if player.vida == 0 and player.muerto is False and player.perdio is False:
            player.muerto = True
            player.cont_dead_frame = 0

        # Mover el mundo a la izquierda
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            nivel_actual.mover_mundo(-diff)

        # Mover el mundo a la derecha
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            nivel_actual.mover_mundo(diff)

        # Siguiente nivel
        posicion_actual = player.rect.x + nivel_actual.sumatoria_de_cambio
        if posicion_actual < nivel_actual.limite:
            player.rect.x = 120
            if nivel_actual.id < len(niveles) - 1:
                nivel_actual = niveles[nivel_actual.id + 1]
                player.nivel_actual = nivel_actual
                player.rect.x = 250
                player.vida += 2
                player.shurikens += 10
                fuente = pygame.font.Font('fuentes/ninja-turtles-regular.otf', 80)
                texto = fuente.render("GANASTE!", True, Color.VERDE)
                _pantalla.blit(texto, (40, const.ALTO_PANTALLA / 2 - 100))
                pygame.display.flip()
                time.sleep(4)
        if nivel_actual.id == 2 and len(nivel_actual.enemigos) == 0:
            fuente = pygame.font.Font('fuentes/ninja-turtles-regular.otf', 80)
            texto = fuente.render("BOO YAH, GANASTE!", True, Color.VERDE)
            _pantalla.blit(texto, (40, const.ALTO_PANTALLA / 2 - 100))
            pygame.display.flip()
            time.sleep(4)
            fin = True

        # Draw
        nivel_actual.draw(_pantalla)
        player_group.draw(_pantalla)

        # Dibujar vidas en _pantalla
        x = 5
        for i in range(player.vida):
            _pantalla.blit(_imagenes["vida"], (x, 5))
            x += 30
            if x > 600: break

        # Dibujar shurikens en _pantalla
        x = 5
        for i in range(player.shurikens):
            _pantalla.blit(_imagenes["shuriken_small"], (x, 40))
            x += 26
            if x > 780: break

        fuente = pygame.font.Font('fuentes/ninja-turtles-regular.otf', 20)
        texto = fuente.render("Puntos: " + str(player.puntos), True, Color.BLANCO)
        _pantalla.blit(texto, [const.ANCHO_PANTALLA - 180, 5])

        # Cayendo fuera de la plataforma
        if player.rect.y > const.ANCHO_PANTALLA:
            aux = nivel_actual.sumatoria_de_cambio * -1
            print(aux)
            if nivel_actual.id == 2 and (player.rect.x + aux) > 300 and (player.rect.x + aux) < 600:
                nivel_actual.id = 3
                nivel_actual = niveles[nivel_actual.id]
                player.nivel_actual = nivel_actual
                player.rect.x = 250
                player.rect.y = 100
            else:
                player.perdio = True

        if player.perdio:
            _pantalla.blit(_imagenes["perdiste"], (0, 0))
            pygame.display.flip()
            pygame.time.wait(4000)
            fin = True


        clock.tick(60)
        pygame.display.flip()

    return nivel_actual.id, player.perdio


def instrucciones():
    reloj = pygame.time.Clock()
    fin_instrucciones = False
    while not fin_instrucciones:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin_instrucciones = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fin_instrucciones = True
        _pantalla.blit(_imagenes["instrucciones"], [0, 0])
        reloj.tick(20)
        pygame.display.flip()


def historia():
    reloj = pygame.time.Clock()
    fin_historia = False
    pag = 1
    while not fin_historia:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin_historia = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pag += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fin_historia = True
                else:
                    pag += 1
                    if pag == 5:
                        return
        _pantalla.blit(_imagenes["historia" + str(pag)], [0, 0])
        reloj.tick(20)
        pygame.display.flip()


def salir():
    sys.exit(0)


def creditos():
    reloj = pygame.time.Clock()
    fin_instrucciones = False
    while not fin_instrucciones:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin_instrucciones = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fin_instrucciones = True
        _pantalla.blit(_imagenes["creditos"], [0, 0])
        reloj.tick(20)
        pygame.display.flip()


if __name__ == '__main__':
    _fin = False

    opciones = [
        ("JUGAR", jugar),
        ("HISTORIA", historia),
        ("INSTRUCCIONES", instrucciones),
        ("CREDITOS", creditos),
        ("SALIR", salir)
    ]

    # Iniciar
    menu = Menu(opciones)
    while not _fin:
        for e in pygame.event.get():
            if e.type == QUIT:
                _fin = True

        menu.actualizar()
        menu.imprimir(_pantalla)

        pygame.display.flip()
        pygame.time.delay(10)
