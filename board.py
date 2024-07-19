import pygame, sys
from pygame.locals import *

class Board:

    def draw():
        pygame.init()

        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        pos = []
        mouse_position = (0, 0)
        drawing = False
        screen = pygame.display.set_mode((600, 600), 0, 32)
        screen.fill(WHITE)
        pygame.display.set_caption("Board")

        last_pos = None

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return pos


                elif event.type == MOUSEMOTION:
                    if (drawing):
                        mouse_position = pygame.mouse.get_pos()
                        pos.append(mouse_position)

                        if last_pos is not None:
                            pygame.draw.line(screen, BLACK, last_pos, mouse_position, 5)
                        last_pos = mouse_position

                elif event.type == MOUSEBUTTONUP:
                    mouse_position = (0, 0)
                    drawing = False
                    last_pos = None

                elif event.type == MOUSEBUTTONDOWN:
                    drawing = True

            pygame.display.update()
