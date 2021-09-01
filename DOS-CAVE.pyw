#Parkour Game Build 0.1
from tkinter.constants import LEFT,BOTTOM
import pygame
from pygame.locals import (K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,
    RLEACCEL,
    KEYDOWN,

    QUIT,)
import platform
from tkinter import Tk, Label, Button
from tkinter import messagebox
import os
cwd = os.getcwd()
if platform.system() == 'Windows':
    slash = '\\'
else:
    slash = '/'
pygame.mixer.init()
pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(loops=-1)
win_sound = pygame.mixer.Sound("win.ogg")
lose_sound = pygame.mixer.Sound("lose.ogg")
#music init here
#Game menu here
while True:
    lvl = 0
    def lvlassig(level):
        global root
        global lvl
        lvl = level
        root.quit()
        root.destroy()
    def die():
        global root
        root.quit()
        root.destroy()
    root = Tk()
    root.title('Game Menu')
    root.geometry('600x100')
    lbl = Label(root,text='Welcome to Dos cave. Please select the level that you want to play. If you are unsure, press HOW TO PLAY.')
    lbl.pack()
    btn = Button(root,text='Level 1',bg='lime green',command=lambda: lvlassig(1))
    btn.pack(side=LEFT)
    btn1 = Button(root,text='Exit',bg='Red',command=die)
    btn1.pack(side=BOTTOM)
    btn2 = Button(root,text='How To Play',bg='yellow',command=lambda: os.startfile('how_to_play.txt'))
    btn2.pack(side=BOTTOM)
    root.mainloop()
    
    if lvl == 1:
       
        class Player(pygame.sprite.Sprite):
            def __init__(self):
                super(Player,self).__init__()
                self.surf = pygame.image.load("default.png").convert()
                self.surf.set_colorkey((255,255,255),RLEACCEL)
                
                self.rect = self.surf.get_rect(center=(50,400))
            def update(self,pressed_keys):
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5,0)
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5,0)
                if pressed_keys[K_UP]:
                    self.rect.move_ip(0,-5)
                if pressed_keys[K_DOWN]:    
                    self.rect.move_ip(0,5)
                if self.rect.left < 0:

                    self.rect.left = 0

                if self.rect.right > SCREEN_WIDTH:

                    self.rect.right = SCREEN_WIDTH

                if self.rect.top <= 0:

                    self.rect.top = 0

                if self.rect.bottom >= SCREEN_HEIGHT:

                    self.rect.bottom = SCREEN_HEIGHT
        class Win(pygame.sprite.Sprite):
            def __init__(self):
                super(Win,self).__init__()
                self.surf = pygame.Surface((50,50))
                self.surf.fill((0,255,0))
                self.rect = self.surf.get_rect(center=(700,500))

        class Obstacle(pygame.sprite.Sprite):
            def __init__(self):
                super(Obstacle,self).__init__()
                self.surf = pygame.Surface((800,50))
                self.surf.fill((255,255,255))
                self.rect = self.surf.get_rect(center=(400,525))
        clock = pygame.time.Clock()
        pygame.init()
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        a = pygame.image.load('ep.ico')
        screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        pygame.display.set_caption('Game Level 1')
        pygame.display.set_icon(a)
        player = Player()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        win = Win()
        wins = pygame.sprite.Group()
        wins.add(win)
        all_sprites.add(win)
        obstacle = Obstacle()
        obstacles = pygame.sprite.Group()
        obstacles.add(obstacle)
        all_sprites.add(obstacle)
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

            for entity in all_sprites:
                screen.blit(entity.surf,entity.rect)
            if pygame.sprite.spritecollideany(player,wins):
                win = True
                player.kill()
                win_sound.play()
                running = False
            if pygame.sprite.spritecollideany(player,obstacles):
                win = False
                player.kill()
                lose_sound.play()
                running = False
            
            pygame.display.flip()
            clock.tick(30)
        pygame.display.quit()
        if win == True:
            Tk().withdraw()
            
            messagebox.showinfo('Game','You win')
        elif win == False:
            Tk().withdraw()
            messagebox.showwarning('Game','You died.')
    elif lvl == 0:

        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
        break

