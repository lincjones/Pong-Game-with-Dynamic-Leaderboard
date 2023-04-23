import os
import random
import pygame

from player import Player
from ball import Ball
from settings import *
from store_score import update_score

all_sprites = pygame.sprite.Group()
font = pygame.font.Font('freesansbold.ttf', 32)
go_text = font.render('GAME OVER', True, (255, 0, 0), (0, 0, 255))
score = 0

def get_game_id():
    x = input("Do you want a custom name(y/n):")
    if x == "n":
        return ""
    else:
        id = input("Enter id:")
    return id

class Game:
    def __init__(self, screen):
        self.screen = screen

        self.player = Player(PLAYER_COLOR, SCREEN_WIDTH/25, SCREEN_HEIGHT*0.2)
        self.player.rect.x += PLAYER_DISPLACE
        self.ball = Ball((0, 255, 0), 20, 20)

        all_sprites.add(self.ball)
        all_sprites.add(self.player)

        self.game_id = get_game_id()

        if (self.game_id == ""):
            f = open(os.path.dirname(os.path.abspath(__file__)) + "/back/scores.txt", 'r')
            t = True
            while t:
                def find():
                    n = random.randint(100000, 999999)
                    for line in f.readlines():
                        print(line)
                        data = line.rsplit(',')
                        if n == data[0]:
                            find()
                        else:
                            self.game_id = n
                            t = False
                            break
                find()
                t=False
                f.close()

        print('YOUR GAME ID:',self.game_id)
    
    def run(self):
        global score
        all_sprites.update()
        self.ball.check_wall()

        if pygame.sprite.collide_rect(self.player, self.ball):
            self.ball.velocity[0] = -self.ball.velocity[0]
            score += 1
            update_score(self.game_id, score)

        self.update_screen()


    def update_screen(self):
        self.screen.fill((0, 0, 0))
        all_sprites.draw(self.screen)

        text=font.render(str(score), True, (255, 0, 0), (0, 0, 0))
        self.screen.blit(text, text.get_rect())

        if self.ball.rect.x <= 0:
            self.screen.blit(go_text, ((SCREEN_WIDTH/2)-(go_text.get_width()/2), (SCREEN_HEIGHT/2)-(go_text.get_height()/2) - 30))

        pygame.display.update()

