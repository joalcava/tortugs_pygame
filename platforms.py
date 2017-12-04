"""
Module for managing platforms.
"""
import pygame
import random

from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

GRASS1 = (448, 193, 64, 64)
GRASS2 = (384, 257, 128, 64)
GRASS3 = (0, 65, 192, 64)  # NO SIRVE
TIERRA1 = (0, 138, 64, 64)
TIERRA2 = (0, 138, 128, 64)
TIERRA3 = (0, 138, 192, 64)
ARBOL = (0, 256, 192, 192)
ROCA = (0, 453, 192, 60)
FLORES = (192, 29, 64, 35)
PLANTA = (141, 0, 42, 64)
SNOWMAN = (448, 512, 64, 134)
SNOWPLANT = (65, 0, 63, 64)
SNOWBAL = (193, 449, 65, 62)
SNOWARBOL = (188, 512, 134, 63)
PLANTANIGHT = (64, 2, 66, 62)
ROCANIGHT = (192, 513, 130, 126)
COFREVERT = (0, 510, 64, 129)
COFREHORI = (64, 514, 128, 64)
FUEGO = (0, 259, 129, 125)
TRAJE = (133, 257, 56, 127)
PUERTA = (0, 405, 129, 172)
HERRAMIENTAS = (320, 512, 189, 127)
LAMPARA = (130, 383, 225, 183)


class Shuriken(pygame.sprite.Sprite):

    def __init__(self, direccion, de_jugador):
        pygame.sprite.Sprite.__init__(self)
        self.frames = [
            pygame.image.load('imagen/shuriken/shuriken1.png').convert_alpha(),
            pygame.image.load('imagen/shuriken/shuriken2.png').convert_alpha(),
            pygame.image.load('imagen/shuriken/shuriken3.png').convert_alpha(),
            pygame.image.load('imagen/shuriken/shuriken4.png').convert_alpha()
        ]
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.direccion = direccion
        self.jugador = de_jugador
        self.frame_actual = 0
        self.temporizador = 0

    def update(self):
        if self.direccion == "R":
            self.rect.x += 5
        else:
            self.rect.x -= 5
        self.image = self.frames[self.frame_actual]
        self.temporizador += 1
        if (self.temporizador % 4) == 0:
            self.frame_actual += 1
        if self.frame_actual == len(self.frames):
            self.frame_actual = 0
            self.temporizador = 0


class Bala(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagen/balas.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.direccion = "L"
        self.jugador = 0

    def update(self):
        if self.direccion == "R":
            self.rect.x += 5
        else:
            self.rect.x -= 5


class Enemigo(pygame.sprite.Sprite):
    def __init__(self, imagen, dispararNum):
        self.stay_frame = []
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(imagen).convert_alpha()
        self.stay_frame.append(image)
        image = pygame.transform.flip(image, True, False)
        self.stay_frame.append(image)
        self.image = self.stay_frame[0]
        self.rect = self.image.get_rect()
        self.direccion = 0
        self.ene = 0
        self.disparar = random.randrange(dispararNum)
        self.dispararN = dispararNum
        self.vida = 1
        self.des = random.randrange(dispararNum - 50)
        self.cont = 0

    def update(self):
        if self.cont > 6:
            self.cont = 0

        if self.direccion == 0:
            self.image = self.stay_frame[0]
        else:
            self.image = self.stay_frame[1]
        self.disparar -= 1
        self.des -= 1
        if self.des < 0:
            self.des = random.randrange(self.dispararN - 50)

        if self.disparar < 0:
            self.disparar = random.randrange(self.dispararN)

        if self.ene == 5 and self.des == 0:
            if self.cont == 0:
                self.rect.x += 500
            if self.cont == 1:
                self.rect.x -= 500
            if self.cont == 2:
                self.rect.y -= 100
            if self.cont == 4:
                self.rect.y -= 100
            if self.cont == 5:
                self.rect.y -= 100
            if self.cont == 6:
                self.rect.y = 414

            self.cont += 1

    def chocar(self):
        self.vida -= 1


class Enemigo2(pygame.sprite.Sprite):

    def __init__(self, dispararNum):

        self.change_x = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.attack_frames_l = []
        self.attack_frames_r = []
        self.direction = "L"
        level = None

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("imagen/skeleton.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(39, 6, 30, 64)
        self.walking_frames_l.append(image)
        self.attack_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        self.attack_frames_r.append(image)

        image = sprite_sheet.get_image(71, 6, 33, 64)
        self.walking_frames_l.append(image)
        self.attack_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        self.attack_frames_r.append(image)
        image = sprite_sheet.get_image(110, 6, 30, 64)
        self.walking_frames_l.append(image)
        self.attack_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        self.attack_frames_r.append(image)
        image = sprite_sheet.get_image(146, 5, 31, 66)
        self.walking_frames_l.append(image)
        self.attack_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        self.attack_frames_r.append(image)

        self.image = self.walking_frames_l[0]
        self.rect = self.image.get_rect()

        self.attack = False
        self.cont_attack = -1
        self.cont_even = 0

        self.boundary_left = 0
        self.boundary_right = 0

        self.direccion = 0

        self.ene = 1

        self.disparar = random.randrange(dispararNum)
        self.atacar = random.randrange(dispararNum - 50)

        self.dispararN = dispararNum

        self.vida = 1

    def update(self):
        pos = self.rect.x + self.level.sumatoria_de_cambio

        cur_pos = self.rect.x - self.level.sumatoria_de_cambio
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
            if (self.change_x < 0):
                self.direction = "L"
                self.direccion = 0
            else:
                self.direction = "R"
                self.direccion = 1

        if self.attack:
            if self.direction == "R":
                self.image = self.attack_frames_r[self.cont_attack]
                self.cont_even += 1
                if (self.cont_even % 22) == 0:
                    self.cont_attack += 1
                if (self.cont_attack == 4):
                    self.cont_attack = -1
                    self.attack = False
                    self.cont_even = 0
            else:
                self.image = self.attack_frames_l[self.cont_attack]
                self.cont_even += 1
                if (self.cont_even % 22) == 0:
                    self.cont_attack += 1
                if (self.cont_attack == 4):
                    self.cont_attack = -1
                    self.attack = False
                    self.cont_even = 0


        else:
            if self.direction == "R":
                if self.change_x == 0:
                    self.image = self.attack_frames_r[0]
                else:
                    frame = (pos // 30) % len(self.walking_frames_r)
                    self.image = self.walking_frames_r[frame]
            else:
                if self.change_x == 0:
                    self.image = self.attack_frames_l[0]
                else:
                    frame = (pos // 30) % len(self.walking_frames_l)
                    self.image = self.walking_frames_l[frame]

        self.rect.x += self.change_x

        self.disparar -= 1
        if self.disparar < 0:
            self.disparar = random.randrange(self.dispararN)
        self.atacar -= 1
        if self.atacar < 0:
            self.atacar = random.randrange(self.dispararN - 50)

    def chocar(self):
        self.vida -= 1

    def Attack(self):
        self.attack = True
        self.cont_attack = 1


class Enemigo1(pygame.sprite.Sprite):

    def __init__(self, dispararNum):

        self.change_x = 0

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.attack_frames_l = []
        self.attack_frames_r = []
        self.direction = "L"
        level = None

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("imagen/knight.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(11, 102, 43, 77)
        self.walking_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(81, 100, 44, 79)
        self.walking_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(150, 102, 45, 77)
        self.walking_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(226, 100, 42, 79)
        self.walking_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(294, 100, 43, 79)
        self.walking_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(363, 101, 44, 78)
        self.walking_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(432, 100, 43, 79)
        self.walking_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(504, 100, 43, 79)
        self.walking_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(229, 280, 43, 79)
        self.attack_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_r.append(image)
        image = sprite_sheet.get_image(145, 282, 55, 77)
        self.attack_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_r.append(image)
        image = sprite_sheet.get_image(77, 281, 55, 78)
        self.attack_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_r.append(image)
        image = sprite_sheet.get_image(12, 283, 43, 76)
        self.attack_frames_l.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_r.append(image)

        self.image = self.walking_frames_l[0]
        self.rect = self.image.get_rect()

        self.attack = False
        self.cont_attack = -1
        self.cont_even = 0

        self.boundary_left = 0
        self.boundary_right = 0

        self.direccion = 0

        self.ene = 1

        self.disparar = random.randrange(dispararNum)
        self.atacar = random.randrange(dispararNum - 50)

        self.dispararN = dispararNum

        self.vida = 1

    def update(self):
        pos = self.rect.x + self.level.sumatoria_de_cambio

        cur_pos = self.rect.x - self.level.sumatoria_de_cambio
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
            if (self.change_x < 0):
                self.direction = "L"
                self.direccion = 0
            else:
                self.direction = "R"
                self.direccion = 1

        if self.attack:
            if self.direction == "R":
                self.image = self.attack_frames_r[self.cont_attack]
                self.cont_even += 1
                if (self.cont_even % 22) == 0:
                    self.cont_attack += 1
                if (self.cont_attack == 4):
                    self.cont_attack = -1
                    self.attack = False
                    self.cont_even = 0
            else:
                self.image = self.attack_frames_l[self.cont_attack]
                self.cont_even += 1
                if (self.cont_even % 22) == 0:
                    self.cont_attack += 1
                if (self.cont_attack == 4):
                    self.cont_attack = -1
                    self.attack = False
                    self.cont_even = 0


        else:
            if self.direction == "R":
                if self.change_x == 0:
                    self.image = self.attack_frames_r[0]
                else:
                    frame = (pos // 30) % len(self.walking_frames_r)
                    self.image = self.walking_frames_r[frame]
            else:
                if self.change_x == 0:
                    self.image = self.attack_frames_l[0]
                else:
                    frame = (pos // 30) % len(self.walking_frames_l)
                    self.image = self.walking_frames_l[frame]

        self.rect.x += self.change_x

        self.disparar -= 1
        if self.disparar < 0:
            self.disparar = random.randrange(self.dispararN)
        self.atacar -= 1
        if self.atacar < 0:
            self.atacar = random.randrange(self.dispararN - 50)

    def chocar(self):
        self.vida -= 1

    def Attack(self):
        self.attack = True
        self.cont_attack = 1


class Objeto(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data, nivel):

        pygame.sprite.Sprite.__init__(self)
        if nivel == 1:
            sprite_sheet = SpriteSheet("imagen/grass.png")
        if nivel == 2:
            sprite_sheet = SpriteSheet("imagen/snow.png")
        if nivel == 3:
            sprite_sheet = SpriteSheet("imagen/night.png")
        if nivel == 4:
            sprite_sheet = SpriteSheet("imagen/castle.png")

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()


class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data, nivel):
        pygame.sprite.Sprite.__init__(self)
        if nivel == 1:
            sprite_sheet = SpriteSheet("imagen/grass.png")
        if nivel == 2:
            sprite_sheet = SpriteSheet("imagen/snow.png")
        if nivel == 3:
            sprite_sheet = SpriteSheet("imagen/night.png")
        if nivel == 4:
            sprite_sheet = SpriteSheet("imagen/castle.png")

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.sumatoria_de_cambio
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
