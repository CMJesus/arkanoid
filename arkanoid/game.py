import pygame as pg
from arkanoid import ALTO, ANCHO
# from . import ALTO, ANCHO
# "punto" refiere al módulo arkanoid, en el cual estamos

pg.init()

class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((ANCHO, ALTO))

    def launch(self):
        game_over = False
        while not game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_over = True

            # Pantalla
            self.screen.fill((123, 123, 255))

            pg.display.flip()

        pg.quit()
        sys.exit()

