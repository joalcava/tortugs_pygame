import pygame
from spritesheet_functions import SpriteSheet

#        (x, y, alto, ancho)
PASTO1 = (448, 193, 64, 64)
PASTO2 = (384, 257, 128, 64)
PASTO3 = (0, 65, 192, 64)
TIERRA1 = (0, 138, 64, 64)
TIERRA2 = (0, 138, 128, 64)
TIERRA3 = (0, 138, 192, 64)
ARBOL = (0, 256, 192, 192)
ROCA = (0, 453, 192, 60)
FLORES = (192, 29, 64, 35)
PLANTA = (141, 0, 42, 64)
MUNECONIEVE = (448, 512, 64, 134)
SNOWPLANT = (65, 0, 63, 64)
BOLANIEVE = (193, 449, 65, 62)
ARBOLNIEVE = (188, 512, 134, 63)
PLANTANIGHT = (64, 2, 66, 62)
ROCANIGHT = (192, 513, 130, 126)
COFREVERT = (0, 510, 64, 129)
COFREHORI = (64, 514, 128, 64)
FUEGO = (0, 259, 129, 125)
TRAJE = (133, 257, 56, 127)
PUERTA = (0, 405, 129, 172)
HERRAMIENTAS = (320, 512, 189, 127)
LAMPARA = (130, 383, 225, 183)


class Objeto(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data, id):
        pygame.sprite.Sprite.__init__(self)
        if id == 0:
            sprite_sheet = SpriteSheet("imagen/grass.png")
        if id == 1:
            sprite_sheet = SpriteSheet("imagen/night.png")
        if id == 2:
            sprite_sheet = SpriteSheet("imagen/castle.png")

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()


class Plataforma(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data, id):
        pygame.sprite.Sprite.__init__(self)
        if id == 0:
            sprite_sheet = SpriteSheet("imagen/grass.png")
        if id == 1:
            sprite_sheet = SpriteSheet("imagen/night.png")
        if id == 2:
            sprite_sheet = SpriteSheet("imagen/castle.png")

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()


class PlataformaEnMovimiento(Plataforma):
    dx = 0
    dy = 0
    limite_arriba = 0
    limite_abajo = 0
    limite_izq = 0
    limite_der = 0
    nivel = None
    player = None

    def update(self):
        self.rect.x += self.dx

        colision = pygame.sprite.collide_rect(self, self.player)
        if colision:
            if self.dx < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right

        self.rect.y += self.dy

        colision = pygame.sprite.collide_rect(self, self.player)
        if colision:
            if self.dy < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        if self.rect.bottom > self.limite_abajo or self.rect.top < self.limite_arriba:
            self.dy *= -1

        pos_actual = self.rect.x - self.nivel.sumatoria_de_cambio
        if pos_actual < self.limite_izq or pos_actual > self.limite_der:
            self.dx *= -1
