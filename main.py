import pygame as pg
from grid import Grid
import sys

pg.init()

#constants
SCREEN = WIDTH, HEIGHT = 900, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def main():
    #setup
    win = pg.display.set_mode(SCREEN)
    pg.display.set_caption('Grid')

    clock = pg.time.Clock()
    clicked = False
    grid = Grid(WIDTH//50, HEIGHT//50, WIDTH, HEIGHT)
    
    while True:
        clock.tick(60)

        grid.draw(win)

        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                clicked = True
            elif event.type == pg.MOUSEBUTTONUP:
                clicked = False

        if clicked:
            pos = pg.mouse.get_pos()
            grid.cell_clicked(pos)

        pg.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()

