import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        # self.rect = pygame.Rect(
        #     (50, 50),(int(width), int(height))
        #                         )
        self.vel = 10
        self.image = pygame.surface.Surface((int(width), int(height)))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = (SCREEN_HEIGHT/2) - (self.image.get_height()/2)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.vel
        elif keys[pygame.K_s] and self.rect.y < SCREEN_HEIGHT - self.image.get_height():
            self.rect.y += self.vel
