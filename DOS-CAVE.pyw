#Parkour Game Build 0.2.0
from log55 import log
x = 'gamelog.log'
log(x,'Game started')
from tkinter.constants import LEFT,BOTTOM,RIGHT
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
SYSVERSION = '0.2.0'
from tkinter import Tk, Label, Button
from tkinter import messagebox
import os
from requests import get
from packaging import version
from webbrowser import open as web
cwd = os.getcwd()
if platform.system() == 'Windows':
    slash = '\\'
else:
    slash = '/'


def cfu():
    
    data = get('https://pastebin.com/raw/cg0knwqc').text
    SYSVERSION = version.parse("0.2.1")
    LATVERSION = version.parse(data[0:6].replace(' ',''))
    if LATVERSION > SYSVERSION:
        Tk().withdraw()
        l = messagebox.askyesno('Update','A new update is available('+data[0:6]+'). Do you want to download it?')
        if l == True:
            web(data[6:len(data)])
    else:
        Tk().withdraw()
        messagebox.showinfo('Update','No new versions are available')
pygame.mixer.init()
pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(loops=-1)
win_sound = pygame.mixer.Sound("win.ogg")
lose_sound = pygame.mixer.Sound("lose.ogg")
log(x,'sound system initialised')
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
    def girl():
        global charpic
        charpic = 'girl.png'
        log('gamelog.log','Changed to girl character')
    def boy():
        global charpic
        charpic = 'boy.png'
        log('gamelog.log','Changed to boy character')
    charpic = 'boy.png'
    root = Tk()
    root.title('Game Menu')
    root.geometry('600x150')
    lbl = Label(root,text='Welcome to Dos cave. Please select the level that you want to play. If you are unsure, press HOW TO PLAY.')
    lbl.pack()
    btn = Button(root,text='Level 1',bg='lime green',command=lambda: lvlassig(1))
    btn.pack(side=LEFT)
    btn4 = Button(root,text='Level 2',bg='lime green',command=lambda: lvlassig(2))
    btn4.pack(side=LEFT)
    btn5 = Button(root,text='Switch to girl character',bg='pink',command=girl)
    btn5.pack()
    
    btn6 = Button(root,text='Switch to boy character',bg='sky blue',command=boy)
    btn6.pack()
    
    btn1 = Button(root,text='Exit',bg='Red',command=die)
    btn1.pack(side=BOTTOM)
    btn2 = Button(root,text='How To Play',bg='yellow',command=lambda: os.startfile('how_to_play.txt'))
    btn2.pack(side=BOTTOM)
    btn3 = Button(root,text='Check for updates',bg='skyblue',command=cfu)
    btn3.pack(side=RIGHT)
    
    
    root.mainloop()
    
    if lvl == 1:
        log(x,'Level 1: Preparing')
        class Player(pygame.sprite.Sprite):
            
            def __init__(self):
                global charpic
                super(Player,self).__init__()
                self.surf = pygame.image.load(charpic).convert()
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
        log(x,'level 1: Started')
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
            
            messagebox.showinfo('Game','You win level 1!')
        elif win == False:
            Tk().withdraw()
            messagebox.showwarning('Game','You died.')

    if lvl == 2:
        log(x,'Level 2: Preparing')
        class Player(pygame.sprite.Sprite):
            def __init__(self):
                global charpic
                super(Player,self).__init__()
                self.surf = pygame.image.load(charpic).convert()
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
        class Obs2(pygame.sprite.Sprite):
            def __init__(self):
                super(Obs2,self).__init__()
                self.surf = pygame.Surface((50,300))
                self.surf.fill((255,255,255))
                self.rect = self.surf.get_rect(center=(600,200))
        clock = pygame.time.Clock()
        pygame.init()
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        a = pygame.image.load('ep.ico')
        screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        pygame.display.set_caption('Game Level 2')
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
        obs2 = Obs2()
        obstacles.add(obs2)
        obstacles.add(obstacle)
        all_sprites.add(obstacle)
        all_sprites.add(obs2)
        running = True
        log(x,'level 2: Started')
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
            
            messagebox.showinfo('Game','You win level 2!')
        elif win == False:
            Tk().withdraw()
            messagebox.showwarning('Game','You died.')
        

    elif lvl == 0:
        log(x,'shutting down sound system')
        
        break
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
log(x,'Process quit with exit code 0')
