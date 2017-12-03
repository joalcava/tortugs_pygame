import pygame
import constants

from platforms import MovingPlatform


class Player(pygame.sprite.Sprite):
    """El jugador"""

    dx = 0
    dy = 0

    imgs_caminando_izq = []
    imgs_caminando_der = []
    imgs_quieto = []
    imgs_atacando_der = []
    imgs_atacando_izq = []
    imgs_muerto_der = []
    imgs_muerto_izq = []

    muerto = False
    perdio = False

    atacando = False
    cont_ataque = -1
    temporizador = 0
    cont_dead = -1
    inmune = 0

    direccion = "R"

    # List of sprites we can bump against
    level = None


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Quieto
        image = pygame.image.load("imagen/parado1.png").convert_alpha()
        self.imgs_quieto.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_quieto.append(image)
        image = pygame.image.load("imagen/saltar1.png").convert_alpha()
        self.imgs_quieto.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_quieto.append(image)

        # Muerto
        image = pygame.image.load("imagen/morir1.png").convert_alpha()
        self.imgs_muerto_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_muerto_izq.append(image)
        image = pygame.image.load("imagen/morir2.png").convert_alpha()
        self.imgs_muerto_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_muerto_izq.append(image)
        image = pygame.image.load("imagen/morir3.png").convert_alpha()
        self.imgs_muerto_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_muerto_izq.append(image)
        image = pygame.image.load("imagen/morir4.png").convert_alpha()
        self.imgs_muerto_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_muerto_izq.append(image)
        image = pygame.image.load("imagen/morir5.png").convert_alpha()
        self.imgs_muerto_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_muerto_izq.append(image)


        # Atacando
        image = pygame.image.load("imagen/atacar1.png").convert_alpha()
        self.imgs_atacando_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_atacando_izq.append(image)
        image = pygame.image.load("imagen/atacar2.png").convert_alpha()
        self.imgs_atacando_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_atacando_izq.append(image)
        image = pygame.image.load("imagen/atacar3.png").convert_alpha()
        self.imgs_atacando_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_atacando_izq.append(image)
        image = pygame.image.load("imagen/atacar4.png").convert_alpha()
        self.imgs_atacando_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_atacando_izq.append(image)

        # Atacando
        image = pygame.image.load("imagen/caminar1.png").convert_alpha()
        self.imgs_caminando_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_caminando_izq.append(image)
        image = pygame.image.load("imagen/caminar2.png").convert_alpha()
        self.imgs_caminando_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_caminando_izq.append(image)
        image = pygame.image.load("imagen/caminar3.png").convert_alpha()
        self.imgs_caminando_der.append(image)
        image = pygame.transform.flip(image, True, False)
        self.imgs_caminando_izq.append(image)

        self.image = self.imgs_quieto[0]
        self.rect = self.image.get_rect()
        self.vida = 10
        self.piedra = 500
        self.puntos = 0

    def gravedad(self):
        if self.dy == 0:
            self.dy = 1
        else:
            self.dy += .35

    def saltar(self):
        if not self.muerto:
            self.rect.y += 2 # Hacer colisionar con el suelo
            colision = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y -= 2 # Deshacer la colision

            # Si hubo colision, hay suelo, entonces saltar
            if len(colision) > 0 or self.rect.bottom >= constants.ALTO_PANTALLA:
                self.dy = -10

    def atacar(self):
        if not self.muerto:
            self.atacando = True
            self.cont_ataque = 0

    def mover_izquierda(self):
        if not self.muerto:
            self.dx = -4
            self.direccion = "L"

    def mover_derecha(self):
        if not self.muerto:
            self.dx = 4
            self.direccion = "R"

    def parar(self):
        self.dx = 0

    def update(self):
        self.gravedad()

        self.rect.x += self.dx
        pos = self.rect.x + self.level.world_shift

        self.inmune -= 1

        if (self.muerto == False and self.perdio == False):
            if self.atacando:
                if self.direccion == "R":
                    self.image = self.imgs_atacando_der[self.cont_ataque]
                else:
                    self.image = self.imgs_atacando_izq[self.cont_ataque]
                self.temporizador += 1
                if (self.temporizador % 8) == 0:
                    self.cont_ataque += 1
                if (self.cont_ataque == len(self.imgs_atacando_der)):
                    self.cont_ataque = -1
                    self.atacando = False
                    self.temporizador = 0

            else:
                if self.direccion == "R":
                    if self.dx == 0:
                        if self.dy < 0:
                            # Saltando
                            self.image = self.imgs_quieto[2]
                        else:
                            # Quieto
                            self.image = self.imgs_quieto[0]
                    else:
                        if self.dy < 0:
                            # Saltando
                            self.image = self.imgs_quieto[2]
                        else:
                            # Caminando
                            frame = (pos // 40) % len(self.imgs_caminando_der)
                            self.image = self.imgs_caminando_der[frame]
                else:
                    if self.dx == 0:
                        if self.dy < 0:
                            self.image = self.imgs_quieto[3]
                        else:
                            self.image = self.imgs_quieto[1]
                    else:
                        if self.dy < 0:
                            self.image = self.imgs_quieto[3]
                        else:
                            frame = (pos // 40) % len(self.imgs_caminando_izq)
                            self.image = self.imgs_caminando_izq[frame]
        else:
            if self.direccion == "R":
                self.image = self.imgs_muerto_der[self.cont_dead]
            else:
                self.image = self.imgs_muerto_izq[self.cont_dead]
            self.temporizador += 1
            if (self.temporizador % 6) == 0:
                self.cont_dead += 1
            if (self.cont_dead == len(self.imgs_muerto_der)):
                self.cont_dead = -1
                self.muerto = False
                self.perdio = True
                self.temporizador = 0



        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if (self.muerto == False and self.perdio == False):
                if self.dx > 0:
                    self.rect.right = block.rect.left
                elif self.dx < 0:
                    # Otherwise if we are moving left, do the opposite.
                    self.rect.left = block.rect.right

        # Move up/down
        # if(self.dead == False):
        self.rect.y += self.dy

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if (self.muerto == False and self.perdio == False):
                if self.dy > 0:
                    self.rect.bottom = block.rect.top
                elif self.dy < 0:
                    self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.dy = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
