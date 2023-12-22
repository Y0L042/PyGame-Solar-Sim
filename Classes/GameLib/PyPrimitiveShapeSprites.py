

import pygame
vec = pygame.math.Vector2


class CircleSprite(pygame.sprite.Sprite):
    def __init__(self, position, radius, color, ):
        super().__init__()
        
        self.radius = radius
        self.color = color
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        # self.rect.center = (self.image.get_width() // 2, self.image.get_height() // 2)