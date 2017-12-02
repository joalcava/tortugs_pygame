import pygame


class Cursor:

    def __init__(self):
        self.image = pygame.image.load('imagen/shuriken.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.y_objetivo = 205
        self.rect.x = 55
        self.rect.y = self.y_objetivo
        self.dy = 29
        self.y_aux = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y_aux += (self.y_objetivo - self.y_aux) / 10.0
        self.rect.y = int(self.y_aux)

    def seleccionar(self, indice):
        self.y_objetivo = 205 + indice * self.dy

    def imprimir(self, pantalla):
        pantalla.blit(self.image, self.rect)
