from Classes.GameLib import PyPrimitiveShapeSprites as PGSSprite
from Classes.GameLib.GameObject import GameObject

import pygame
vec2 = pygame.math.Vector2


class Planet(GameObject):
    AU = 149.6e6 * 1000
    G = 6.67428e-11

    SCALE = 250 / AU  # 1AU = 100px
    TIMESTEP = 3600*24

    def __init__(self, position, radius, mass, color):
        super().__init__() 
        self.position = position
        self.radius = radius
        self.mass = mass
        self.color = color
        
        self.velX = 0
        self.velY = 0

        self.orbitTail= []
        
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius ,self.radius), self.radius)
        self.rect = self.image.get_rect()

    def draw(self, win, delta):
        pass