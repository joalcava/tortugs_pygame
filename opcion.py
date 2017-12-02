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


class Opcion:

    def __init__(self, fuente, titulo, pos, funcion):
        fuente.set_underline(False)
        self.imagen_normal = fuente.render(titulo, 1, (255, 255, 255))

        fuente.set_underline(True)
        self.imagen_destacada = fuente.render(titulo, 1, (0, 255, 0))

        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 105
        self.rect.y = pos
        self.funcion = funcion

    def imprimir(self, pantalla):
        pantalla.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion()
