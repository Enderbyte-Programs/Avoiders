#Parkour Game Build 0.0.2
import pygame
from pygame.locals import (K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,)
import platform
from tkinter import Tk
from tkinter import messagebox
import os
import sys
from time import sleep
cwd = os.getcwd()
if platform.system() == 'Windows':
    slash = '\\'
else:
    slash = '/'

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((0,0,255))
        self.rect = self.surf.get_rect()
    def update(self,pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1,0)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-2)
            
        self.rect.move_ip(0,1)
        if self.rect.left < 0:

            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:

            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:

            self.rect.top = 0

        if self.rect.bottom >= 500:

            self.rect.bottom = 500
class Win(pygame.sprite.Sprite):
    def __init__(self):
        super(Win,self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(center=(700,500))
        

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
a = pygame.image.load('ep.ico')
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('Game')
pygame.display.set_icon(a)
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
win = Win()
wins = pygame.sprite.Group()
wins.add(win)
all_sprites.add(win)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    screen.fill((0,0,0))
    surf = pygame.Surface((800,50))
    
    surf.fill((255,255,255))
    rect = surf.get_rect()
    screen.blit(surf,(0,500))
    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect)
    if pygame.sprite.spritecollideany(player,wins):
        win = True
        player.kill()
        running = False
    
    pygame.display.flip()
pygame.quit()
if win == True:
    Tk().withdraw()
    messagebox.showinfo('Game','You win Level 1!')