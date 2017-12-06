import pygame
import random
from spritesheet_functions import SpriteSheet


pygame.mixer.init(44100, -16, 2, 2048)
pygame.display.set_mode((800, 600))

_sonidos = {
    "disparo_laser": pygame.mixer.Sound('audio/laser.wav')
}

_imagenes = {
    "skull1": pygame.image.load("imagen/skull/1.png").convert_alpha(),
    "skull2": pygame.image.load("imagen/skull/2.png").convert_alpha(),
    "skull3": pygame.image.load("imagen/skull/3.png").convert_alpha(),
    "skull4": pygame.image.load("imagen/skull/4.png").convert_alpha(),
    "skull5": pygame.image.load("imagen/skull/5.png").convert_alpha(),
    "flame1": pygame.image.load("imagen/flame/1.png").convert_alpha(),
    "flame2": pygame.image.load("imagen/flame/2.png").convert_alpha(),
    "flame3": pygame.image.load("imagen/flame/3.png").convert_alpha(),
    "flame4": pygame.image.load("imagen/flame/4.png").convert_alpha(),
    "fireball1": pygame.image.load("imagen/fireball/1.png").convert_alpha(),
    "fireball2": pygame.image.load("imagen/fireball/2.png").convert_alpha(),
    "fireball3": pygame.image.load("imagen/fireball/3.png").convert_alpha(),
    "shuriken1": pygame.image.load('imagen/shuriken/shuriken1.png').convert_alpha(),
    "shuriken2": pygame.image.load('imagen/shuriken/shuriken2.png').convert_alpha(),
    "shuriken3": pygame.image.load('imagen/shuriken/shuriken3.png').convert_alpha(),
    "shuriken4": pygame.image.load('imagen/shuriken/shuriken4.png').convert_alpha(),
    "bala": pygame.image.load('imagen/balas.png').convert_alpha(),
    "enemigoestacionario": pygame.image.load("imagen/enemigo1.png").convert_alpha(),
    "brain1": pygame.image.load("imagen/brain/1.png").convert_alpha(),
    "brain2": pygame.image.load("imagen/brain/2.png").convert_alpha(),
    "brain3": pygame.image.load("imagen/brain/3.png").convert_alpha(),
    "roller1": pygame.image.load("imagen/roller/1.png").convert_alpha(),
    "roller2": pygame.image.load("imagen/roller/2.png").convert_alpha(),
    "roller3": pygame.image.load("imagen/roller/3.png").convert_alpha(),
    "roller4": pygame.image.load("imagen/roller/4.png").convert_alpha()
}


class Shuriken(pygame.sprite.Sprite):

    def __init__(self, direccion, de_jugador):
        pygame.sprite.Sprite.__init__(self)
        self.frames = [
            _imagenes["shuriken1"], _imagenes["shuriken2"],
            _imagenes["shuriken3"], _imagenes["shuriken4"]
        ]
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.direccion = direccion
        self.jugador = de_jugador
        self.frame_actual = 0
        self.temporizador = 0

    def update(self):
        if self.direccion == "R":
            self.rect.x += 6
        else:
            self.rect.x -= 6
        self.image = self.frames[self.frame_actual]
        self.temporizador += 1
        if (self.temporizador % 4) == 0:
            self.frame_actual += 1
        if self.frame_actual == len(self.frames):
            self.frame_actual = 0
            self.temporizador = 0


class FireBall(pygame.sprite.Sprite):

    def __init__(self, direccion):
        pygame.sprite.Sprite.__init__(self)
        self.frames = {
            "L0": _imagenes["fireball1"],
            "L1": _imagenes["fireball2"],
            "L2": _imagenes["fireball3"],
            "R0": pygame.transform.flip(_imagenes["fireball1"], True, False),
            "R1": pygame.transform.flip(_imagenes["fireball2"], True, False),
            "R2": pygame.transform.flip(_imagenes["fireball3"], True, False)
        }

        self.frame_actual = 0
        self.direccion = direccion
        self.image = self.frames[self.direccion + str(self.frame_actual)]
        self.rect = self.image.get_rect()
        self.jugador = False
        self.temporizador = 0

    def update(self):
        if self.direccion == "R":
            self.rect.x += 6
        else:
            self.rect.x -= 6
        self.temporizador += 1
        if (self.temporizador % 3) == 0:
            self.image = self.frames[self.direccion + str(self.frame_actual)]
            self.frame_actual += 1
            if self.frame_actual == (len(self.frames)/2):
                self.frame_actual = 0
                self.temporizador = 0


class Bala(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = _imagenes["bala"]
        self.rect = self.image.get_rect()
        self.direccion = "L"
        self.jugador = False

    def update(self):
        if self.direccion == "R":
            self.rect.x += 4
        else:
            self.rect.x -= 4


# Estacionario que dispara balas
class EnemigoEstacionario(pygame.sprite.Sprite):
    sonido_laser = pygame.mixer.Sound('audio/laser.wav')
    def __init__(self, pos):
        self.con_movimiento = False
        pygame.sprite.Sprite.__init__(self)
        image = _imagenes["enemigoestacionario"]
        self.stay_frame = []
        self.stay_frame.append(image)
        self.stay_frame.append(pygame.transform.flip(image, True, False))
        self.image = self.stay_frame[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.direccion = "L"
        self.cadencia = random.randrange(40, 100)
        self.temporizador = 0

    def atacar(self):
        pass

    def disparar(self):
        self.temporizador += 1
        if (self.temporizador % self.cadencia) == 0:
            EnemigoEstacionario.sonido_laser.play()
            self.cadencia = random.randrange(40, 100)
            self.temporizador = 0
            bala = Bala()
            bala.direccion = self.direccion
            bala.rect.x = self.rect.x
            bala.rect.y = self.rect.y
            return bala
        return None

    def update(self):
        if self.direccion == "L":
            self.image = self.stay_frame[0]
        else:
            self.image = self.stay_frame[1]


# Cerebro estacionario
class EnemigoObstaculo(pygame.sprite.Sprite):

    def __init__(self, pos):
        self.con_movimiento = False
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("imagen/enemigo2.png").convert_alpha()
        self.stay_frame = []
        self.stay_frame.append(image)
        self.stay_frame.append(pygame.transform.flip(image, True, False))
        self.image = self.stay_frame[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.direccion = "L"

    def atacar(self):
        pass

    def disparar(self):
        return None

    def update(self):
        if self.direccion == "L":
            self.image = self.stay_frame[0]
        else:
            self.image = self.stay_frame[1]

    def kill(self):
        pass


# Roller en movimiento
class EnemigoConMovimiento(pygame.sprite.Sprite):

    def __init__(self, pos, nivel):
        self.con_movimiento = True
        pygame.sprite.Sprite.__init__(self)
        self.dx = 0
        self.dy = 0
        self.frames_caminando = {
            "L0": _imagenes["roller1"],
            "L1": _imagenes["roller2"],
            "R0": pygame.transform.flip(_imagenes["roller1"], True, False),
            "R1": pygame.transform.flip(_imagenes["roller2"], True, False)
        }
        self.frames_atacando = {
            "L0": _imagenes["roller3"],
            "L1": _imagenes["roller4"],
            "R0": pygame.transform.flip(_imagenes["roller3"], True, False),
            "R1": pygame.transform.flip(_imagenes["roller4"], True, False)
        }
        self.direccion = "L"
        self.frame_actual = 0
        self.atacando = False
        self.temporizador_caminando = 0
        self.temporizador_atacando = 0
        self.vida = 2
        self.image = self.frames_caminando[self.direccion + str(self.frame_actual)]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.nivel = nivel
        self.cayendo = False

    def gravedad(self):
        if self.dy == 0:
            self.dy = 1
        else:
            self.dy += .35

    def update(self):
        self.gravedad()
        self.rect.x += self.dx

        if self.atacando:
            if self.direccion == "R":
                self.dx = 3
            else:
                self.dx = -3
            self.temporizador_atacando += 1
            if (self.temporizador_atacando % 10) == 0:
                self.temporizador_atacando = 0
                self.frame_actual += 1
                if self.frame_actual == (len(self.frames_atacando) / 2):
                    self.frame_actual = 0
                self.image = self.frames_atacando[self.direccion + str(self.frame_actual)]

        self.rect.y += self.dy
        if self.cayendo is False:
            colisiones_l = pygame.sprite.spritecollide(self, self.nivel.plataformas, False)
            if colisiones_l:
                if self.dy > 0:
                    self.rect.bottom = colisiones_l[0].rect.top
                elif self.dy < 0:
                    self.rect.top = colisiones_l[0].rect.bottom
                self.dy = 0  # No caer
            else:
                self.cayendo = True

        #for block in colisiones_l:
        #    if self.dy > 0:
        #        self.rect.bottom = block.rect.top
        #    elif self.dy < 0:
        #        self.rect.top = block.rect.bottom

        if self.rect.y > 800:
            pygame.sprite.Sprite.kill(self)
            print('Enemigo cayendo al vacio')

    def kill(self):
        self.vida -= 1
        if self.vida == 0:
            pygame.sprite.Sprite.kill(self)

    def disparar(self):
        pass

    def atacar(self):
        self.atacando = True

# Brain en movimiento
class EnemigoConMovimiento2(pygame.sprite.Sprite):

    def __init__(self, pos, limites, nivel):
        self.con_movimiento = True
        pygame.sprite.Sprite.__init__(self)
        self.dx = -1
        self.frames_caminando = {
            "L0": _imagenes["brain1"],
            "L1": _imagenes["brain2"],
            "R0": pygame.transform.flip(_imagenes["brain1"], True, False),
            "R1": pygame.transform.flip(_imagenes["brain2"], True, False)
        }
        self.frames_atacando = {
            "L0": _imagenes["brain3"],
            "R0": pygame.transform.flip(_imagenes["brain3"], True, False)
        }

        self.direccion = "L"
        self.frame_actual_caminando = 0
        self.atacando = False
        self.temporizador_caminando = 0
        self.temporizador_atacando = 0
        self.limite_izq = limites[0]
        self.limite_der = limites[1]
        self.nivel = nivel
        self.vida = 2
        self.image = self.frames_caminando[self.direccion + str(self.frame_actual_caminando)]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        # Cambiar de direccion cuando se llegue al limite
        posicion_actual = self.rect.x - self.nivel.sumatoria_de_cambio
        if posicion_actual < self.limite_izq or posicion_actual > self.limite_der:
            self.dx *= -1
            if self.dx < 0:
                self.direccion = "L"
            else:
                self.direccion = "R"

        # Atacar
        if self.atacando:
            if self.direccion == "R":
                self.dx = 3
            else:
                self.dx = -3

            self.temporizador_atacando += 1
            if (self.temporizador_atacando % 40) == 0:
                self.temporizador_atacando = 0
                self.atacando = False
                if self.dx > 0:
                    self.dx = 1
                else:
                    self.dx = -1
                self.image = self.frames_caminando[self.direccion + '0']
        # Caminar
        else:
            self.temporizador_caminando += 1
            if (self.temporizador_caminando % 40) == 0:
                self.frame_actual_caminando += 1
                if self.frame_actual_caminando == (len(self.frames_caminando)/2):
                    self.frame_actual_caminando = 0
                    self.temporizador_caminando = 0
                self.image = self.frames_caminando[self.direccion + str(self.frame_actual_caminando)]
        self.rect.x += self.dx

    def kill(self):
        self.vida -= 1
        if self.vida == 0:
            pygame.sprite.Sprite.kill(self)

    def disparar(self):
        pass

    def atacar(self):
        self.atacando = True
        self.image = self.frames_atacando[self.direccion + '0']


# Dragon que dispara fuego estacionario
class EnemigoEstacionario2(pygame.sprite.Sprite):

    def __init__(self, pos):
        self.con_movimiento = False
        pygame.sprite.Sprite.__init__(self)
        self.frames = {
            "L0": _imagenes["skull1"],
            "L1": _imagenes["skull2"],
            "L2": _imagenes["skull3"],
            "L3": _imagenes["skull4"],
            "L4": _imagenes["skull5"],
            "R0": pygame.transform.flip(_imagenes["skull1"], True, False),
            "R1": pygame.transform.flip(_imagenes["skull2"], True, False),
            "R2": pygame.transform.flip(_imagenes["skull3"], True, False),
            "R3": pygame.transform.flip(_imagenes["skull4"], True, False),
            "R4": pygame.transform.flip(_imagenes["skull5"], True, False)
        }
        self.frame_actual = 0
        self.direccion = "L"
        self.image = self.frames[self.direccion + str(self.frame_actual)]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.cadencia = random.randrange(60, 150)
        self.temporizador_disparo = 0
        self.temporizador_animacion = 0
        self.animando = False

    def atacar(self):
        pass

    def disparar(self):
        self.temporizador_disparo += 1
        if (self.temporizador_disparo % self.cadencia) == 0:
            self.animar()
            if self.animando:
                self.temporizador_disparo -= 2
            else:
                print('Dragon disparando')
                self.cadencia = random.randrange(40, 100)
                self.temporizador_disparo = 0
                self.animando = False
                bala = FireBall(self.direccion)
                bala.rect.x = self.rect.x
                bala.rect.y = self.rect.y + 10
                return bala
        return None

    def animar(self):
        self.animando = True
        self.temporizador_animacion += 1
        if (self.temporizador_animacion % 3) == 0:
            print('Animando dragon')
            self.frame_actual += 1
            if self.frame_actual == (len(self.frames)/2):
                self.animando = False
                self.frame_actual = 0
                self.temporizador_animacion = 0
            self.image = self.frames[self.direccion + str(self.frame_actual)]

    def update(self):
        self.image = self.frames[self.direccion + str(self.frame_actual)]


# Fuego estacionario
class EnemigoObstaculo2(pygame.sprite.Sprite):

    def __init__(self, pos):
        self.con_movimiento = False
        pygame.sprite.Sprite.__init__(self)

        self.frames = [
            _imagenes["flame1"], _imagenes["flame2"],
            _imagenes["flame3"], _imagenes["flame4"]
        ]
        self.frame_actual = 0
        self.image = self.frames[self.frame_actual]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.temporizador = 0

    def atacar(self):
        pass

    def disparar(self):
        return None

    def update(self):
        self.temporizador += 1
        if (self.temporizador % 10) == 0:
            self.temporizador = 0
            self.frame_actual += 1
            if self.frame_actual == len(self.frames):
                self.frame_actual = 0
            self.image = self.frames[self.frame_actual]

    def kill(self):
        pass


class Jefe(pygame.sprite.Sprite):
    pass
