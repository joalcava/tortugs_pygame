import pygame
import constants
import plataformas

from enemigos import\
    EnemigoEstacionario, EnemigoConMovimiento,\
    EnemigoConMovimiento2, EnemigoObstaculo,\
    EnemigoObstaculo2, EnemigoEstacionario2

from plataformas import PlataformaEnMovimiento, Plataforma, Objeto


class Nivel:
    plataformas = None
    enemigos = None
    objetos = None
    fondo = None
    sumatoria_de_cambio = 0
    limite = -1000

    def __init__(self, player):
        self.plataformas = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.objetos = pygame.sprite.Group()
        self.balas = pygame.sprite.Group()
        self.player = player

    def update(self):
        enemigos1 = [i for i in self.enemigos if not i.con_movimiento]
        enemigos2 = [i for i in self.enemigos if i.con_movimiento]
        for enemigo in enemigos1:
            # Mantener la direccion del jugador
            if enemigo.rect.x < self.player.rect.x:
                enemigo.direccion = "R"
            else:
                enemigo.direccion = "L"
            # Disparar y atacar
            if abs(enemigo.rect.x - self.player.rect.x) < 280:
                enemigo.atacar()
                bala = enemigo.disparar()
                if bala:
                    self.balas.add(bala)

        for enemigo in enemigos2:
            if abs(enemigo.rect.x - self.player.rect.x) < 240\
                    and abs(enemigo.rect.y - self.player.rect.y) < 50:
                enemigo.atacar()

        # Colisiones
        # Balas chocan con plataforma
        pygame.sprite.groupcollide(self.balas, self.plataformas, True, False)

        # Balas de jugador chocan con enemigo
        balas_player = pygame.sprite.Group([i for i in self.balas if i.jugador is True])
        impactos = pygame.sprite.groupcollide(balas_player, self.enemigos, True, True)
        self.player.puntos += len(impactos) * 5

        # Balas chocan con jugador
        balas_enemigos = pygame.sprite.Group([i for i in self.balas if i.jugador is False])
        impactos = pygame.sprite.spritecollide(self.player, balas_enemigos, True)
        if impactos:
            if self.player.atacando is False:
                self.player.vida -= 1
            else:
                self.player.puntos += 10

        # Jugador choca con enemigos
        impactos = pygame.sprite.spritecollide(self.player, self.enemigos, self.player.atacando)
        if impactos:
            if self.player.atacando:
                self.player.puntos += len(impactos) * 10
            else:
                if self.player.inmune < 0:
                    self.player.vida -= 1
                self.player.inmune = 15
                self.player.retroceder()

        self.balas.update()
        self.plataformas.update()
        self.enemigos.update()
        self.enemigos.update()

    def draw(self, pantalla):
        pantalla.fill(constants.Color.AZUL)
        pantalla.blit(self.fondo, (self.sumatoria_de_cambio // 3, 0))
        self.objetos.draw(pantalla)
        self.balas.draw(pantalla)
        self.plataformas.draw(pantalla)
        self.enemigos.draw(pantalla)

    def mover_mundo(self, dx):
        self.sumatoria_de_cambio += dx

        for bala in self.balas:
            bala.rect.x += dx

        for three in self.objetos:
            three.rect.x += dx

        for platform in self.plataformas:
            platform.rect.x += dx

        for enemy in self.enemigos:
            enemy.rect.x += dx


class Nivel1(Nivel):

    def __init__(self, player):
        Nivel.__init__(self, player)
        self.id = 0
        self.fondo = pygame.image.load("imagen/nivel1.jpg").convert_alpha()
        self.fondo.set_colorkey(constants.Color.BLANCO)
        self.limite = -1
        self.limite = -3300

        level = [
            [plataformas.PASTO2, 200, 536],
            [plataformas.PASTO2, 320, 536],
            [plataformas.PASTO3, 550, 500],
            [plataformas.TIERRA3, 550, 564],
            [plataformas.TIERRA3, 737, 564],
            [plataformas.PASTO3, 737, 500],
            [plataformas.PASTO1, 1000, 450],
            [plataformas.PASTO1, 1070, 400],
            [plataformas.PASTO1, 1190, 280],
            [plataformas.PASTO3, 1850, 450],
            [plataformas.TIERRA3, 1850, 514],
            [plataformas.TIERRA3, 1850, 578],
            [plataformas.PASTO3, 2037, 450],
            [plataformas.TIERRA3, 2037, 514],
            [plataformas.TIERRA3, 2037, 578],
            [plataformas.PASTO3, 2224, 450],
            [plataformas.TIERRA3, 2224, 514],
            [plataformas.TIERRA3, 2224, 578],
            [plataformas.PASTO1, 2566, 430],
            [plataformas.PASTO3, 2965, 300],
            [plataformas.TIERRA3, 2965, 360],
            [plataformas.TIERRA3, 2965, 424],
            [plataformas.TIERRA3, 2965, 488],
            [plataformas.TIERRA3, 2965, 552],
            [plataformas.TIERRA3, 2965, 616],
            [plataformas.PASTO3, 3620, 300],
            [plataformas.TIERRA3, 3620, 360],
            [plataformas.TIERRA3, 3620, 424],
            [plataformas.TIERRA3, 3620, 488],
            [plataformas.TIERRA3, 3620, 552],
            [plataformas.TIERRA3, 3620, 616],
            [plataformas.PASTO3, 3807, 300],
            [plataformas.TIERRA3, 3807, 360],
            [plataformas.TIERRA3, 3807, 424],
            [plataformas.TIERRA3, 3807, 488],
            [plataformas.TIERRA3, 3807, 552],
            [plataformas.TIERRA3, 3807, 616],
            [plataformas.PASTO3, 3994, 300],
            [plataformas.TIERRA3, 3994, 360],
            [plataformas.TIERRA3, 3994, 424],
            [plataformas.TIERRA3, 3994, 488],
            [plataformas.TIERRA3, 3994, 552],
            [plataformas.TIERRA3, 3994, 616],
            [plataformas.PASTO3, 4186, 300],
            [plataformas.TIERRA3, 4186, 360],
            [plataformas.TIERRA3, 4186, 424],
            [plataformas.TIERRA3, 4186, 488],
            [plataformas.TIERRA3, 4186, 552],
            [plataformas.TIERRA3, 4186, 616],
            [plataformas.PASTO3, 4373, 300],
            [plataformas.TIERRA3, 4373, 360],
            [plataformas.TIERRA3, 4373, 424],
            [plataformas.TIERRA3, 4373, 488],
            [plataformas.TIERRA3, 4373, 552],
            [plataformas.TIERRA3, 4373, 616],
        ]

        objetos = [
            [plataformas.ARBOL, 270, 344],
            [plataformas.FLORES, 600, 465],
            [plataformas.FLORES, 670, 465],
            [plataformas.FLORES, 740, 465],
            [plataformas.FLORES, 810, 465],
            [plataformas.ARBOL, 1925, 258],
            [plataformas.ROCA, 2117, 391],
            [plataformas.FLORES, 3000, 265],
            [plataformas.ARBOL, 3750, 108],
            [plataformas.ROCA, 3950, 241],
            [plataformas.FLORES, 4136, 265],
            [plataformas.FLORES, 4250, 265],
            [plataformas.ARBOL, 4300, 108],
        ]

        # Enemigos
        self.enemigos.add(EnemigoConMovimiento((895, 460), self))
        self.enemigos.add(EnemigoEstacionario((1900, 400)))
        self.enemigos.add(EnemigoObstaculo((2200, 415)))
        self.enemigos.add(EnemigoConMovimiento((2300, 400), self))
        self.enemigos.add(EnemigoObstaculo((3050, 263)))
        self.enemigos.add(EnemigoEstacionario((3700, 250)))
        self.enemigos.add(EnemigoObstaculo((3900, 265)))
        self.enemigos.add(EnemigoEstacionario((4100, 250)))
        self.enemigos.add(EnemigoConMovimiento((4300, 250), self))

        for objeto in objetos:
            obj = Objeto(objeto[0], self.id)
            obj.rect.x = objeto[1]
            obj.rect.y = objeto[2]
            self.objetos.add(obj)

        for platform in level:
            block = Plataforma(platform[0], self.id)
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.plataformas.add(block)

        block = PlataformaEnMovimiento(plataformas.PASTO1, self.id)
        block.rect.x = 1350
        block.rect.y = 280
        block.limite_izq = 1350
        block.limite_der = 1600
        block.dx = 1
        block.player = self.player
        block.nivel = self
        self.plataformas.add(block)

        block = PlataformaEnMovimiento(plataformas.PASTO1, self.id)
        block.rect.x = 2666
        block.rect.y = 300
        block.limite_izq = 2666
        block.limite_der = 2850
        block.dx = 1
        block.player = self.player
        block.nivel = self
        self.plataformas.add(block)

        block = PlataformaEnMovimiento(plataformas.PASTO1, self.id)
        block.rect.x = 3320
        block.rect.y = 400
        block.limite_izq = 3320
        block.limite_der = 3550
        block.dx = 1
        block.player = self.player
        block.nivel = self
        self.plataformas.add(block)

        block = PlataformaEnMovimiento(plataformas.PASTO1, self.id)
        block.rect.x = 1690
        block.rect.y = 300
        block.limite_arriba = 100
        block.limite_abajo = 550
        block.dy = -1
        block.player = self.player
        block.nivel = self
        self.plataformas.add(block)


class Nivel2(Nivel):

    def __init__(self, player):
        Nivel.__init__(self, player)
        self.id = 1
        self.fondo = pygame.image.load("imagen/night1.png").convert_alpha()
        self.fondo.set_colorkey(constants.Color.BLANCO)
        self.limite = -1
        self.limite = -5670

        level = [
            [plataformas.PASTO2, 200, 536],
            [plataformas.PASTO2, 320, 536],
            [plataformas.PASTO3, 550, 500],
            [plataformas.TIERRA3, 550, 564],
            [plataformas.TIERRA3, 737, 564],
            [plataformas.PASTO3, 737, 500],
            [plataformas.PASTO1, 500, 320],
            [plataformas.PASTO1, 390, 410],
            [plataformas.PASTO1, 690, 310],
            [plataformas.PASTO1, 960, 320],
            [plataformas.PASTO2, 1200, 400],
            [plataformas.PASTO3, 1850, 450],
            [plataformas.TIERRA3, 1850, 514],
            [plataformas.TIERRA3, 1850, 578],
            [plataformas.PASTO3, 2037, 450],
            [plataformas.TIERRA3, 2037, 514],
            [plataformas.TIERRA3, 2037, 578],
            [plataformas.PASTO3, 2224, 450],
            [plataformas.TIERRA3, 2224, 514],
            [plataformas.TIERRA3, 2224, 578],
            [plataformas.PASTO1, 2800, 400],
            [plataformas.PASTO3, 3100, 200],
            [plataformas.PASTO3, 3830, 200],
            [plataformas.PASTO3, 5000, 400],
            [plataformas.PASTO3, 5187, 400],
            [plataformas.PASTO3, 6100, 400],
        ]

        objetos = [
            [plataformas.COFREVERT, 300, 407],
            [plataformas.COFREHORI, 600, 436],
            [plataformas.COFREHORI, 1860, 386],
            [plataformas.COFREVERT, 2030, 321],
            [plataformas.COFREHORI, 6130, 336],
        ]

        # Enemigos obstaculo estacionario o fuego
        self.enemigos.add(EnemigoObstaculo2((1250, 350)))
        self.enemigos.add(EnemigoObstaculo2((2000, 400)))
        self.enemigos.add(EnemigoObstaculo2((3180, 150)))
        self.enemigos.add(EnemigoObstaculo2((5050, 350)))
        self.enemigos.add(EnemigoObstaculo2((5310, 350)))

        # Enemigos estacionarios que disparan o dragon
        self.enemigos.add(EnemigoEstacionario2((2100, 389)))
        self.enemigos.add(EnemigoEstacionario2((3840, 150)))
        self.enemigos.add(EnemigoEstacionario2((5110, 341)))

        # Enemigos en movimiento
        self.enemigos.add(EnemigoConMovimiento2(pos=(560, 434), limites=(550, 910), nivel=self))
        self.enemigos.add(EnemigoConMovimiento2(pos=(3200, 136), limites=(3110, 3240), nivel=self))
        self.enemigos.add(EnemigoConMovimiento2(pos=(5210, 336), limites=(5110, 5350), nivel=self))

        for plataforma in level:
            block = Plataforma(plataforma[0], self.id)
            block.rect.x = plataforma[1]
            block.rect.y = plataforma[2]
            block.player = self.player
            self.plataformas.add(block)

        for objeto in objetos:
            three_ob = Objeto(objeto[0], self.id)
            three_ob.rect.x = objeto[1]
            three_ob.rect.y = objeto[2]
            self.objetos.add(three_ob)

        movimiento = [
            [plataformas.PASTO1, 1350, 400, "Y", 100, 500, -1],
            [plataformas.PASTO1, 1470, 450, "Y", 100, 500, -1],
            [plataformas.PASTO1, 1590, 300, "Y", 100, 500, -1],
            [plataformas.PASTO1, 2520, 380, "X", 2520, 2700, 1],
            [plataformas.PASTO1, 2920, 300, "Y", 100, 500, -1],
            [plataformas.PASTO1, 3300, 200, "X", 3300, 3750, 2],
            [plataformas.PASTO1, 4100, 200, "X", 4100, 4530, 2],
            [plataformas.PASTO1, 4600, 450, "Y", 100, 500, -1],
            [plataformas.PASTO1, 4750, 300, "Y", 100, 500, -1],
            [plataformas.PASTO1, 5390, 400, "X", 5390, 6000, 2],
            [plataformas.PASTO2, 6320, 400, "X", 6320, 6800, 3],
        ]

        for mov in movimiento:
            block = PlataformaEnMovimiento(mov[0], self.id)
            block.rect.x = mov[1]
            block.rect.y = mov[2]
            if mov[3] == "X":
                block.limite_izq = mov[4]
                block.limite_der = mov[5]
                block.dx = mov[6]
            else:
                block.limite_arriba = mov[4]
                block.limite_abajo = mov[5]
                block.dy = mov[6]
            block.player = self.player
            block.nivel = self
            self.plataformas.add(block)

        block = PlataformaEnMovimiento(plataformas.PASTO1, self.id)
        block.rect.x = 1690
        block.rect.y = 300
        block.limite_arriba = 100
        block.limite_abajo = 550
        block.dy = 1
        block.player = self.player
        block.nivel = self
        self.plataformas.add(block)


class Nivel3(Nivel):

    def __init__(self, jugador):
        Nivel.__init__(self, jugador)
        self.id = 2
        self.fondo = pygame.image.load("imagen/castle1.png").convert_alpha()
        self.fondo.set_colorkey(constants.Color.BLANCO)
        self.limite = -3100

        level = [
            (plataformas.PASTO2, 200, 536),
            (plataformas.PASTO2, 320, 536),
            (plataformas.PASTO3, 550, 500),
            (plataformas.TIERRA3, 550, 564),
            (plataformas.TIERRA3, 737, 564),
            (plataformas.PASTO3, 737, 500),
            (plataformas.PASTO3, 924, 500),
            (plataformas.TIERRA3, 924, 564),
            (plataformas.PASTO3, 1111, 500),
            (plataformas.TIERRA3, 1111, 564),
            (plataformas.PASTO3, 1111, 500),
            (plataformas.TIERRA3, 1111, 564),
            (plataformas.PASTO3, 1298, 500),
            (plataformas.TIERRA3, 1298, 564),
            (plataformas.PASTO3, 1485, 500),
            (plataformas.TIERRA3, 1485, 564),
            (plataformas.PASTO3, 1672, 500),
            (plataformas.TIERRA3, 1672, 564),
            (plataformas.PASTO3, 1859, 500),
            (plataformas.TIERRA3, 1859, 564),
            (plataformas.PASTO3, 2051, 500),
            (plataformas.TIERRA3, 2051, 564),
            (plataformas.PASTO3, 2230, 500),
            (plataformas.TIERRA3, 2230, 564),
            (plataformas.PASTO3, 2425, 500),
            (plataformas.TIERRA3, 2425, 564),
            (plataformas.PASTO3, 2612, 500),
            (plataformas.TIERRA3, 2612, 564),
            (plataformas.PASTO3, 2799, 500),
            (plataformas.TIERRA3, 2799, 564),
            (plataformas.PASTO3, 2986, 500),
            (plataformas.TIERRA3, 2986, 564),
            (plataformas.PASTO3, 3173, 500),
            (plataformas.TIERRA3, 3173, 564),
            (plataformas.PASTO3, 3360, 500),
            (plataformas.TIERRA3, 3360, 564),
            (plataformas.PASTO3, 3547, 500),
            (plataformas.TIERRA3, 3547, 564),
            (plataformas.PASTO3, 3734, 500),
            (plataformas.TIERRA3, 3734, 564),
            (plataformas.PASTO3, 3921, 500),
            (plataformas.TIERRA3, 3921, 564),
            (plataformas.PASTO3, 4108, 500),
            (plataformas.TIERRA3, 4108, 564),
        ]

        objetos = [
            (plataformas.PUERTA, 4050, 329),
            (plataformas.FUEGO, 750, 375),
            (plataformas.FUEGO, 2250, 375),
            (plataformas.FUEGO, 3750, 375),
            (plataformas.TRAJE, 200, 373),
            (plataformas.TRAJE, 1200, 373),
            (plataformas.TRAJE, 1900, 373),
            (plataformas.TRAJE, 2500, 373),
            (plataformas.TRAJE, 3500, 373),
            (plataformas.HERRAMIENTAS, 260, 373),
            (plataformas.HERRAMIENTAS, 1300, 373),
            (plataformas.HERRAMIENTAS, 2000, 373),
            (plataformas.HERRAMIENTAS, 2600, 373),
            (plataformas.HERRAMIENTAS, 3300, 373),
        ]

        self.enemigos.add(EnemigoObstaculo2((550, 450)))
        self.enemigos.add(EnemigoObstaculo((1000, 455)))
        self.enemigos.add(EnemigoObstaculo2((1400, 450)))
        self.enemigos.add(EnemigoObstaculo((2000, 455)))
        self.enemigos.add(EnemigoObstaculo2((2500, 450)))
        self.enemigos.add(EnemigoObstaculo((2800, 455)))

        self.enemigos.add(EnemigoEstacionario2((650, 434)))
        self.enemigos.add(EnemigoEstacionario((1350, 445)))
        self.enemigos.add(EnemigoEstacionario2((1550, 434)))
        self.enemigos.add(EnemigoEstacionario((1850, 445)))
        self.enemigos.add(EnemigoEstacionario2((2150, 434)))
        self.enemigos.add(EnemigoEstacionario((2350, 445)))

        self.enemigos.add(EnemigoConMovimiento((850, 430), nivel=self))
        self.enemigos.add(EnemigoConMovimiento2((1150, 424), (1100, 1600), nivel=self))
        self.enemigos.add(EnemigoConMovimiento((1650, 430), nivel=self))
        self.enemigos.add(EnemigoConMovimiento2((2250, 424), (2200, 2400), nivel=self))
        self.enemigos.add(EnemigoConMovimiento((2450, 430), nivel=self))
        self.enemigos.add(EnemigoConMovimiento2((2650, 430), (2600, 2800), nivel=self))

        for platform in level:
            block = Plataforma(platform[0], self.id)
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.plataformas.add(block)

        for obj in objetos:
            three_ob = Objeto(obj[0], self.id)
            three_ob.rect.x = obj[1]
            three_ob.rect.y = obj[2]
            self.objetos.add(three_ob)

        movimiento = []

        for mov in movimiento:
            block = PlataformaEnMovimiento(mov[0], self.id)
            block.rect.x = mov[1]
            block.rect.y = mov[2]
            if mov[3] == "X":
                block.limite_izq = mov[4]
                block.limite_der = mov[5]
                block.dx = mov[6]
            else:
                block.limite_arriba = mov[4]
                block.limite_abajo = mov[5]
                block.dy = mov[6]
            block.player = self.player
            block.nivel = self
            self.plataformas.add(block)
