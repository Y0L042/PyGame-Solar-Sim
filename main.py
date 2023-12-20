from __future__ import annotations

import math
import pygame

from Classes.GameObject import GameObject
# from Classes.Planet import Planet


pygame.init()



#region Display Config
WIDTH, HEIGHT = 800, 800
MAX_FRAMERATE = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")
#endregion Display Config



#region Color Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
#endregion Color Constants



#region Global Variables
GameObjects = []
#endregion Global Variables



#region Loop
def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(MAX_FRAMERATE)

        process()
        draw()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
#endregion Loop



#region Main Functions
def process():
    sun = instantiate(Planet(0, 0, 30, 1.98892 * 10**30, YELLOW))

def draw():
    for Object in GameObjects:
        Object.draw(WIN)

#endregion Main Functions



#region Utility Functions
def instantiate(i_new_game_object):
    GameObjects.append(i_new_game_object)
    return i_new_game_object
#endregion Utility Functions







class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11

    SCALE = 250 / AU  # 1AU = 100px
    TIMESTEP = 3600*24

    def __init__(self, posX, posY, radius, mass, color):
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.mass = mass
        self.color = color

        self.velX = 0
        self.velY = 0

        self.orbitTail= []

    def draw(self, win):
        x = self.posX * self.SCALE + WIDTH / 2
        y = self.posY * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)



























#region Main()
if __name__ == '__main__':
    main()
#endregion Main()