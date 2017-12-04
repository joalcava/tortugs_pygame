import pygame
import constants

from platforms import MovingPlatform


class Player(pygame.sprite.Sprite):
    """El jugador"""

    dx = 0
    dy = 0

    imgs_caminando = {}
    imgs_quieto = {}
    imgs_atacando_der = []
    imgs_atacando_izq = []
    imgs_muerto_der = []
    imgs_muerto_izq = []

    muerto = False
    perdio = False
    atacando = False
    inmune = 0
    temporizador = 0
    cont_ataque_frame = -1
    cont_dead_frame = -1
    direccion = "R"
    nivel_actual = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sonido_ataque = pygame.mixer.Sound('audio/throw.wav')

        # Quieto
        image = pygame.image.load("imagen/parado1.png").convert_alpha()
        self.imgs_quieto['R1'] = image
        image = pygame.transform.flip(image, True, False)
        self.imgs_quieto['L1'] = image
        image = pygame.image.load("imagen/saltar1.png").convert_alpha()
        self.imgs_quieto['R2'] = image
        image = pygame.transform.flip(image, True, False)
        self.imgs_quieto['L2'] = image

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

        # Caminando
        image = pygame.image.load("imagen/caminar1.png").convert_alpha()
        self.imgs_caminando['R' + '0'] = image
        image = pygame.transform.flip(image, True, False)
        self.imgs_caminando['L' + '0'] = image
        image = pygame.image.load("imagen/caminar2.png").convert_alpha()
        self.imgs_caminando['R' + '1'] = image
        image = pygame.transform.flip(image, True, False)
        self.imgs_caminando['L' + '1'] = image
        image = pygame.image.load("imagen/caminar3.png").convert_alpha()
        self.imgs_caminando['R' + '2'] = image
        image = pygame.transform.flip(image, True, False)
        self.imgs_caminando['L' + '2'] = image

        self.image = self.imgs_quieto['R1']
        self.rect = self.image.get_rect()
        self.vida = 10
        self.shurikens = 20
        self.puntos = 0

    def gravedad(self):
        if self.dy == 0:
            self.dy = 1
        else:
            self.dy += .35

    def saltar(self):
        if not self.muerto:
            self.rect.y += 2  # Hacer colisionar con el suelo
            colision = pygame.sprite.spritecollide(self, self.nivel_actual.plataformas, False)
            self.rect.y -= 2  # Deshacer la colision

            # Si hubo colision, hay suelo, entonces saltar
            if len(colision) > 0 or self.rect.bottom >= constants.ALTO_PANTALLA:
                self.dy = -10

    def atacar(self):
        if not self.muerto:
            self.atacando = True
            self.cont_ataque_frame = 0
            self.sonido_ataque.play()

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
        self.rect.x += self.dx  # Caminar
        pos = self.rect.x + self.nivel_actual.sumatoria_de_cambio
        self.inmune -= 1

        if self.muerto is False and self.perdio is False:
            if self.atacando:
                if self.direccion == "R":
                    self.image = self.imgs_atacando_der[self.cont_ataque_frame]
                else:
                    self.image = self.imgs_atacando_izq[self.cont_ataque_frame]
                self.temporizador += 1
                if (self.temporizador % 8) == 0:
                    self.cont_ataque_frame += 1
                if self.cont_ataque_frame == len(self.imgs_atacando_der):
                    self.cont_ataque_frame = -1
                    self.atacando = False
                    self.temporizador = 0

            else:
                if self.dx == 0:
                    if self.dy < 0:
                        # Saltando
                        self.image = self.imgs_quieto[self.direccion + '2']
                    else:
                        # Quieto
                        self.image = self.imgs_quieto[self.direccion + '1']
                else:
                    if self.dy < 0:
                        # Saltando en movimiento
                        self.image = self.imgs_quieto[self.direccion + '2']
                    else:
                        # Caminando
                        frame = (pos // 40) % 3  # pos // temporizador % numero de frames
                        self.image = self.imgs_caminando[self.direccion + str(frame)]
        # Muerto
        else:
            if self.direccion == "R":
                self.image = self.imgs_muerto_der[self.cont_dead_frame]
            else:
                self.image = self.imgs_muerto_izq[self.cont_dead_frame]
            self.temporizador += 1
            if (self.temporizador % 6) == 0:
                self.cont_dead_frame += 1
            if self.cont_dead_frame == len(self.imgs_muerto_der):
                self.cont_dead_frame = -1
                self.muerto = False
                self.perdio = True
                self.temporizador = 0

        # Colisiones
        colisiones_l = pygame.sprite.spritecollide(self, self.nivel_actual.plataformas, False)
        for block in colisiones_l:
            if self.muerto is False and self.perdio is False:
                if self.dx > 0:
                    self.rect.right = block.rect.left  # Reestablecer la posicion
                elif self.dx < 0:
                    self.rect.left = block.rect.right  # Reestablecer la posicion

        # Movimiento y colision vertical
        self.rect.y += self.dy
        colisiones_l = pygame.sprite.spritecollide(self, self.nivel_actual.plataformas, False)
        for block in colisiones_l:
            if self.muerto is False and self.perdio is False:
                if self.dy > 0:
                    self.rect.bottom = block.rect.top
                elif self.dy < 0:
                    self.rect.top = block.rect.bottom
            self.dy = 0  # Detener el movimiento vertical
            if isinstance(block, MovingPlatform):  # Si colisiono con una plataforma en movimiento
                self.rect.x += block.change_x  # mover al jugador con la plataforma
