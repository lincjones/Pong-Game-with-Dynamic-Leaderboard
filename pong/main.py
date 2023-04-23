import pygame
pygame.init()
import sys

from settings import *
import game


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = game.Game(screen)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    clock.tick(FPS)
    game.run()
    