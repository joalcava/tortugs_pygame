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

import pygame

from cursor import Cursor
from opcion import Opcion
from constants import Color


class Menu:

    def __init__(self, opciones):
        self.fondo = pygame.image.load("imagen/fondo-menu.jpg").convert()
        self.fuente = pygame.font.Font('fuentes/ninja-turtles-regular.otf', 80)
        self.texto = self.fuente.render('TURTLE NINJA ', True, Color.VERDE)
        self.opciones = list()
        self.cursor = Cursor()
        self.seleccionado = 0
        self.total = len(opciones)
        self.mantiene_pulsado = False
        self.sonido_menu = pygame.mixer.Sound('audio/an_8_bit_story.ogg')
        self.sonido_menu.play(loops=-1)
        self.construir_opciones(opciones)

    def construir_opciones(self, opciones):
        fuente = pygame.font.Font('fuentes/HKGrotesk-Bold.otf', 22)
        fuente.set_bold(True)

        y_pos = 205
        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, y_pos, funcion))
            y_pos += 30

    def actualizar(self):
        key = pygame.key.get_pressed()
        if not self.mantiene_pulsado:
            if key[pygame.K_UP] and self.seleccionado > 0:
                self.seleccionado -= 1
            elif key[pygame.K_DOWN] and self.seleccionado < self.total-1:
                self.seleccionado += 1
            elif key[pygame.K_RETURN]:
                self.sonido_menu.stop()
                self.opciones[self.seleccionado].activar()
                self.sonido_menu.play(loops=-1)

        self.mantiene_pulsado = \
            key[pygame.K_UP] \
            or key[pygame.K_DOWN] \
            or key[pygame.K_RETURN]
        self.cursor.seleccionar(self.seleccionado)
        self.cursor.actualizar()

        for opt in self.opciones:
            opt.destacar(False)
        self.opciones[self.seleccionado].destacar(True)

    def imprimir(self, pantalla):
        pantalla.blit(self.fondo, (0, 0))
        pantalla.blit(self.texto, [10, 10])
        self.cursor.imprimir(pantalla)
        for opcion in self.opciones:
            opcion.imprimir(pantalla)
