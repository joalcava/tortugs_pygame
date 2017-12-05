import pygame
import constants
import platforms

from platforms import\
    Enemigo,\
    Enemigo1,\
    Enemigo2,\
    EnemigoEstatico,\
    PlataformaEnMovimiento,\
    Plataforma,\
    Objeto


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
        for enemigo in self.enemigos:
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
        # self.enemigos.draw(pantalla)

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
        #self.limite = -100
        self.limite = -3300

        level = [
            [platforms.PASTO2, 200, 536],
            [platforms.PASTO2, 320, 536],
            [platforms.PASTO3, 550, 500],
            [platforms.TIERRA3, 550, 564],
            [platforms.TIERRA3, 737, 564],
            [platforms.PASTO3, 737, 500],
            [platforms.PASTO1, 1000, 450],
            [platforms.PASTO1, 1070, 400],
            [platforms.PASTO1, 1190, 280],
            [platforms.PASTO3, 1850, 450],
            [platforms.TIERRA3, 1850, 514],
            [platforms.TIERRA3, 1850, 578],
            [platforms.PASTO3, 2037, 450],
            [platforms.TIERRA3, 2037, 514],
            [platforms.TIERRA3, 2037, 578],
            [platforms.PASTO3, 2224, 450],
            [platforms.TIERRA3, 2224, 514],
            [platforms.TIERRA3, 2224, 578],
            [platforms.PASTO1, 2566, 430],
            [platforms.PASTO3, 2965, 300],
            [platforms.TIERRA3, 2965, 360],
            [platforms.TIERRA3, 2965, 424],
            [platforms.TIERRA3, 2965, 488],
            [platforms.TIERRA3, 2965, 552],
            [platforms.TIERRA3, 2965, 616],
            [platforms.PASTO3, 3620, 300],
            [platforms.TIERRA3, 3620, 360],
            [platforms.TIERRA3, 3620, 424],
            [platforms.TIERRA3, 3620, 488],
            [platforms.TIERRA3, 3620, 552],
            [platforms.TIERRA3, 3620, 616],
            [platforms.PASTO3, 3807, 300],
            [platforms.TIERRA3, 3807, 360],
            [platforms.TIERRA3, 3807, 424],
            [platforms.TIERRA3, 3807, 488],
            [platforms.TIERRA3, 3807, 552],
            [platforms.TIERRA3, 3807, 616],
            [platforms.PASTO3, 3994, 300],
            [platforms.TIERRA3, 3994, 360],
            [platforms.TIERRA3, 3994, 424],
            [platforms.TIERRA3, 3994, 488],
            [platforms.TIERRA3, 3994, 552],
            [platforms.TIERRA3, 3994, 616],
            [platforms.PASTO3, 4186, 300],
            [platforms.TIERRA3, 4186, 360],
            [platforms.TIERRA3, 4186, 424],
            [platforms.TIERRA3, 4186, 488],
            [platforms.TIERRA3, 4186, 552],
            [platforms.TIERRA3, 4186, 616],
            [platforms.PASTO3, 4373, 300],
            [platforms.TIERRA3, 4373, 360],
            [platforms.TIERRA3, 4373, 424],
            [platforms.TIERRA3, 4373, 488],
            [platforms.TIERRA3, 4373, 552],
            [platforms.TIERRA3, 4373, 616],
        ]

        objetos = [
            [platforms.ARBOL, 270, 344],
            [platforms.FLORES, 600, 465],
            [platforms.FLORES, 670, 465],
            [platforms.FLORES, 740, 465],
            [platforms.FLORES, 810, 465],
            [platforms.ARBOL, 1925, 258],
            [platforms.ROCA, 2117, 391],
            [platforms.FLORES, 3000, 265],
            [platforms.ARBOL, 3750, 108],
            [platforms.ROCA, 3950, 241],
            [platforms.FLORES, 4136, 265],
            [platforms.FLORES, 4250, 265],
            [platforms.ARBOL, 4300, 108],
        ]

        enemigos = [
            [1, (895, 450)],
            [1, (1900, 400)],
            [2, (2200, 410)],
            [1, (2300, 400)],
            [1, (3050, 250)],
            [1, (3700, 250)],
            [1, (3900, 250)],
            [1, (4100, 250)],
        ]

        for enemigo in enemigos:
            if enemigo[0] == 1:
                self.enemigos.add(
                    platforms.Enemigo(enemigo[1]))
            elif enemigo[0] == 2:
                self.enemigos.add(
                    platforms.EnemigoEstatico(enemigo[1], enemigo[0]))

        for objeto in objetos:
            obj = platforms.Objeto(objeto[0], 1)
            obj.rect.x = objeto[1]
            obj.rect.y = objeto[2]
            self.objetos.add(obj)

        for platform in level:
            block = platforms.Plataforma(platform[0], 1)
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.plataformas.add(block)

        block = PlataformaEnMovimiento(platforms.PASTO1, 1)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.plataformas.add(block)

        block = PlataformaEnMovimiento(platforms.PASTO1, 1)
        block.rect.x = 2666
        block.rect.y = 300
        block.boundary_left = 2666
        block.boundary_right = 2850
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.plataformas.add(block)

        block = PlataformaEnMovimiento(platforms.PASTO1, 1)
        block.rect.x = 3320
        block.rect.y = 400
        block.boundary_left = 3320
        block.boundary_right = 3550
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.plataformas.add(block)

        block = PlataformaEnMovimiento(platforms.PASTO1, 1)
        block.rect.x = 1690
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.plataformas.add(block)


class Nivel2(Nivel):

    def __init__(self, player):
        Nivel.__init__(self, player)
        self.id = 1
        self.fondo = pygame.image.load("imagen/night1.png").convert_alpha()
        self.fondo.set_colorkey(constants.Color.BLANCO)
        #limite = 100
        self.limite = -5670

        level = [
            [platforms.PASTO2, 200, 536],
            [platforms.PASTO2, 320, 536],
            [platforms.PASTO3, 550, 500],
            [platforms.TIERRA3, 550, 564],
            [platforms.TIERRA3, 737, 564],
            [platforms.PASTO3, 737, 500],
            [platforms.PASTO1, 500, 320],
            [platforms.PASTO1, 390, 410],
            [platforms.PASTO1, 690, 310],
            [platforms.PASTO1, 960, 320],
            [platforms.PASTO2, 1200, 400],
            [platforms.PASTO3, 1850, 450],
            [platforms.TIERRA3, 1850, 514],
            [platforms.TIERRA3, 1850, 578],
            [platforms.PASTO3, 2037, 450],
            [platforms.TIERRA3, 2037, 514],
            [platforms.TIERRA3, 2037, 578],
            [platforms.PASTO3, 2224, 450],
            [platforms.TIERRA3, 2224, 514],
            [platforms.TIERRA3, 2224, 578],
            [platforms.PASTO1, 2800, 400],
            [platforms.PASTO3, 3100, 200],
            [platforms.PASTO3, 3830, 200],
            [platforms.PASTO3, 5000, 400],
            [platforms.PASTO3, 5187, 400],
            [platforms.PASTO3, 6100, 400],
        ]

        objetos = [
            [platforms.COFREVERT, 300, 407],
            [platforms.COFREHORI, 600, 436],
            [platforms.COFREHORI, 1860, 386],
            [platforms.COFREVERT, 2030, 321],
            [platforms.COFREHORI, 6130, 336],
        ]

        enemigos = [
            ["skull", (1250, 345)],
            ["skull", (2000, 395)],
            ["skull", (2300, 395)],
            ["skull", (3180, 145)],
            ["skull", (3840, 145)],
            ["skull", (3950, 145)],
            ["skull", (5050, 345)],
            ["skull", (5250, 345)],
            ["skull", (5310, 345)]
        ]

        enemigos1 = [
            [200, 560, 434, -1, 550, 910],
            [200, 2100, 384, -1, 2010, 2400],
            [200, 3200, 136, -1, 3110, 3240],
            [200, 5110, 336, -1, 5010, 5300],
            [200, 5210, 336, -1, 5110, 5350],
        ]

        for enemigo in enemigos:
            self.enemigos.add(EnemigoEstatico(enemigo[1], enemigo[0]))

        for enem in enemigos1:
            ene = Enemigo2(enem[0])
            ene.rect.x = enem[1]
            ene.rect.y = enem[2]
            ene.dx = enem[3]
            ene.boundary_left = enem[4]
            ene.boundary_right = enem[5]
            ene.nivel = self
            self.enemigos.add(ene)

        # Go through the array above and add platforms
        for platform in level:
            block = Plataforma(platform[0], 3)
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.plataformas.add(block)

        for obj in objetos:
            three_ob = Objeto(obj[0], 3)
            three_ob.rect.x = obj[1]
            three_ob.rect.y = obj[2]
            self.objetos.add(three_ob)

        movimiento = [
            [platforms.PASTO1, 1350, 400, "Y", 100, 500, -1],
            [platforms.PASTO1, 1470, 450, "Y", 100, 500, -1],
            [platforms.PASTO1, 1590, 300, "Y", 100, 500, -1],
            [platforms.PASTO1, 2520, 380, "X", 2520, 2700, 1],
            [platforms.PASTO1, 2920, 300, "Y", 100, 500, -1],
            [platforms.PASTO1, 3300, 200, "X", 3300, 3750, 2],
            [platforms.PASTO1, 4100, 200, "X", 4100, 4530, 2],
            [platforms.PASTO1, 4600, 450, "Y", 100, 500, -1],
            [platforms.PASTO1, 4750, 300, "Y", 100, 500, -1],
            [platforms.PASTO1, 5390, 400, "X", 5390, 6000, 2],
            [platforms.PASTO2, 6320, 400, "X", 6320, 6800, 3],
        ]

        for mov in movimiento:
            block = PlataformaEnMovimiento(mov[0], 3)
            block.rect.x = mov[1]
            block.rect.y = mov[2]
            if mov[3] == "X":
                block.boundary_left = mov[4]
                block.boundary_right = mov[5]
                block.change_x = mov[6]
            else:
                block.boundary_top = mov[4]
                block.boundary_bottom = mov[5]
                block.change_y = mov[6]
            block.player = self.player
            block.level = self
            self.plataformas.add(block)

        block = PlataformaEnMovimiento(platforms.PASTO1, 3)
        block.rect.x = 1690
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.plataformas.add(block)


class Nivel3(Nivel):

    def __init__(self, jugador):
        Nivel.__init__(self, jugador)
        self.id = 2
        self.fondo = pygame.image.load("imagen/castle1.png").convert_alpha()
        self.fondo.set_colorkey(constants.Color.BLANCO)
        self.limite = -3100

        level = [
            (platforms.PASTO2, 200, 536),
            (platforms.PASTO2, 320, 536),
            (platforms.PASTO3, 550, 500),
            (platforms.TIERRA3, 550, 564),
            (platforms.TIERRA3, 737, 564),
            (platforms.PASTO3, 737, 500),
            (platforms.PASTO3, 924, 500),
            (platforms.TIERRA3, 924, 564),
            (platforms.PASTO3, 1111, 500),
            (platforms.TIERRA3, 1111, 564),
            (platforms.PASTO3, 1111, 500),
            (platforms.TIERRA3, 1111, 564),
            (platforms.PASTO3, 1298, 500),
            (platforms.TIERRA3, 1298, 564),
            (platforms.PASTO3, 1485, 500),
            (platforms.TIERRA3, 1485, 564),
            (platforms.PASTO3, 1672, 500),
            (platforms.TIERRA3, 1672, 564),
            (platforms.PASTO3, 1859, 500),
            (platforms.TIERRA3, 1859, 564),
            (platforms.PASTO3, 2051, 500),
            (platforms.TIERRA3, 2051, 564),
            (platforms.PASTO3, 2230, 500),
            (platforms.TIERRA3, 2230, 564),
            (platforms.PASTO3, 2425, 500),
            (platforms.TIERRA3, 2425, 564),
            (platforms.PASTO3, 2612, 500),
            (platforms.TIERRA3, 2612, 564),
            (platforms.PASTO3, 2799, 500),
            (platforms.TIERRA3, 2799, 564),
            (platforms.PASTO3, 2986, 500),
            (platforms.TIERRA3, 2986, 564),
            (platforms.PASTO3, 3173, 500),
            (platforms.TIERRA3, 3173, 564),
            (platforms.PASTO3, 3360, 500),
            (platforms.TIERRA3, 3360, 564),
            (platforms.PASTO3, 3547, 500),
            (platforms.TIERRA3, 3547, 564),
            (platforms.PASTO3, 3734, 500),
            (platforms.TIERRA3, 3734, 564),
            (platforms.PASTO3, 3921, 500),
            (platforms.TIERRA3, 3921, 564),
            (platforms.PASTO3, 4108, 500),
            (platforms.TIERRA3, 4108, 564),
        ]

        objetos = [
            (platforms.PUERTA, 4050, 329),
            (platforms.FUEGO, 750, 375),
            (platforms.FUEGO, 2250, 375),
            (platforms.FUEGO, 3750, 375),
            (platforms.TRAJE, 200, 373),
            (platforms.TRAJE, 1200, 373),
            (platforms.TRAJE, 1900, 373),
            (platforms.TRAJE, 2500, 373),
            (platforms.TRAJE, 3500, 373),
            (platforms.HERRAMIENTAS, 260, 373),
            (platforms.HERRAMIENTAS, 1300, 373),
            (platforms.HERRAMIENTAS, 2000, 373),
            (platforms.HERRAMIENTAS, 2600, 373),
            (platforms.HERRAMIENTAS, 3300, 373),
        ]

        enemigos = [
            ("skull", (550, 445)),
            ("skull", (800, 445)),
            ("skull", (1000, 445)),
            ("skull", (1100, 445)),
            ("skull", (1500, 445)),
            ("skull", (1800, 445)),
            ("skull", (2000, 445)),
            ("skull", (2200, 445)),
            ("skull", (2500, 445)),
            ("skull", (2800, 445)),
        ]

        enemigos1 = [
            (200, 560, 434, -1, 550, 910),
            (200, 1050, 434, -1, 1000, 1500),
            (200, 1550, 434, -1, 1500, 1800),
            (200, 1850, 434, -1, 1800, 2000),
            (200, 2150, 434, -1, 2100, 2300),
            (200, 2350, 434, -1, 2300, 2500),
            (200, 2550, 434, -1, 2500, 2700),
        ]

        enemigos2 = [
            (200, 660, 424, -1, 650, 910),
            (200, 1150, 424, -1, 1100, 1600),
            (200, 1650, 424, -1, 1600, 1900),
            (200, 1950, 424, -1, 1700, 2100),
            (200, 2250, 424, -1, 2200, 2400),
            (200, 2450, 424, -1, 2400, 2600),
            (200, 2650, 424, -1, 2600, 2800),
        ]

        # ene = Enemigo("boss.png", 150)
        # ene.rect.x = 3400
        # ene.rect.y = 414
        # ene.ene = 5
        # self.enemigos.add(ene)

        for enemigo in enemigos:
            self.enemigos.add(EnemigoEstatico(enemigo[1], enemigo[0]))

        for enem in enemigos1:
            ene = Enemigo2(enem[0])
            ene.rect.x = enem[1]
            ene.rect.y = enem[2]
            ene.dx = enem[3]
            ene.boundary_left = enem[4]
            ene.boundary_right = enem[5]
            ene.level = self
            self.enemigos.add(ene)

        for enem in enemigos2:
            ene = Enemigo1(enem[0])
            ene.rect.x = enem[1]
            ene.rect.y = enem[2]
            ene.change_x = enem[3]
            ene.boundary_left = enem[4]
            ene.boundary_right = enem[5]
            ene.level = self
            self.enemigos.add(ene)

        for platform in level:
            block = Plataforma(platform[0], 4)
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.plataformas.add(block)

        for obj in objetos:
            three_ob = Objeto(obj[0], 4)
            three_ob.rect.x = obj[1]
            three_ob.rect.y = obj[2]
            self.objetos.add(three_ob)

        movimiento = []

        for mov in movimiento:
            block = PlataformaEnMovimiento(mov[0], 3)
            block.rect.x = mov[1]
            block.rect.y = mov[2]
            if mov[3] == "X":
                block.boundary_left = mov[4]
                block.boundary_right = mov[5]
                block.change_x = mov[6]
            else:
                block.boundary_top = mov[4]
                block.boundary_bottom = mov[5]
                block.change_y = mov[6]
            block.player = self.player
            block.level = self
            self.plataformas.add(block)
