#Version 0.5
from tkinter import Tk
from time import sleep
from sys import exit as forcequit
from tkinter import messagebox
from webbrowser import open as web
try:
    from log55 import log
except:
    Tk().withdraw()
    messagebox.showerror('Game','Please download the library "log55". Press ok to to be prompted for download')
    Tk().withdraw()
    l = messagebox.askyesno('Game','Do you want to download it?')
    if l == True:
        web('https://github.com/Enderbyte-Programs/Avoiders/raw/main/log55.cpython-39.pyc')
    sleep(30)
    forcequit()
x = 'gamelog.log'
try:
    log(x,'Game started')
except:
    Tk().withdraw()
    messagebox.showerror('Error','Could not create log file')
    forcequit()
from tkinter.constants import LEFT,BOTTOM,RIGHT
try:
    import pygame


    from pygame.locals import (K_UP,

        K_DOWN,

        K_LEFT,

        K_RIGHT,

        K_ESCAPE,
        RLEACCEL,
        )
except:
    Tk().withdraw()
    messagebox.showerror('Error','Could not find library "pygame"')
    log(x,'Could not find library "pygame"')
    haspygame = False
else:
    haspygame = True
import platform

from tkinter import Tk, Label, Button, filedialog

import os
import random
try:
    from requests import get
except:
    Tk().withdraw()
    messagebox.showerror('Error','Could not find library "requests"')
    log(x,'could not find library "requests"')
    hasreq = False
else:
    hasreq = True
from packaging import version

cwd = os.getcwd()
if platform.system() == 'Windows':
    slash = '\\'
else:
    slash = '/'


def cfu():
    
    data = get('https://pastebin.com/raw/cg0knwqc').text
    SYSVERSION = version.parse("0.5.0")
    LATVERSION = version.parse(data[0:6].replace(' ',''))
    if LATVERSION > SYSVERSION:
        Tk().withdraw()
        l = messagebox.askyesno('Update','A new update is available('+data[0:6]+'). Do you want to download it?')
        if l == True:
            web(data[6:len(data)])
    else:
        Tk().withdraw()
        messagebox.showinfo('Update','No new versions are available')
if haspygame == True:
    pygame.mixer.init()
    if os.path.isfile("music.ogg"):
        pygame.mixer.music.load('music.ogg')
        pygame.mixer.music.play(loops=-1)
    else:
        log(x,'could not find file "music.ogg"')
    if os.path.isfile("win.ogg"):
        win_sound = pygame.mixer.Sound("win.ogg")
    else:
        log(x,'could not find file "win.ogg"')
    if os.path.isfile("lose.ogg"):
        lose_sound = pygame.mixer.Sound("lose.ogg")
    else:
        log(x,'could not find file "lose.ogg"')
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
        f = open('default.dat','w+')
        f.write('girl.png')
        f.close()
    def boy():
        global charpic
        charpic = 'boy.png'
        log('gamelog.log','Changed to boy character')
        f = open('default.dat','w+')
        f.write('boy.png')
        f.close()

    def importchar():
        x = filedialog.askopenfilename()
        if os.path.isfile(x)== True:
            global charpic
            charpic = x
            f = open('default.dat','w+')
            f.write(x)
            f.close()
    
    

    if os.path.isfile('default.dat') == True:
        f = open('default.dat')
        charpic = f.read()
        if os.path.isfile(charpic):
            f.close()
        else:
            f.close()
            f = open('default.dat','w+')
            f.write('boy.png')
            f.close()
    else:
        f = open('default.dat','x')
        f.write('boy.png')
        f.close()
        charpic = 'boy.png'
    if os.path.isfile('boy.png') == False or os.path.isfile('ep.ico') == False:
        log(x,"Could not find files boy.png and/or ep.ico")
        Tk().withdraw()
        messagebox.showerror('Game','Please reinstall me.')
        forcequit()
    root = Tk()
    root.title('Game Menu')
    root.geometry('600x200')
    def disable_event():
        pass
    lbl = Label(root,text='Welcome to Avoiders. Please select the level that you want to play. If you are unsure, press HOW TO PLAY.')
    lbl.pack()
    btn = Button(root,text='Level 1',bg='lime green',command=lambda: lvlassig(1))
    btn.pack(side=LEFT)
    if haspygame == False:
        btn['state'] = 'disabled'
    btn4 = Button(root,text='Level 2',bg='lime green',command=lambda: lvlassig(2))
    btn4.pack(side=LEFT)
    if haspygame == False:
        btn4['state'] = 'disabled'
    btn8 = Button(root,text='Level 3',bg='lime green',command=lambda: lvlassig(3))
    btn8.pack(side=LEFT)
    if haspygame == False:
        btn8['state'] = 'disabled'
    btn9 = Button(root,text='Level 4',bg='lime green',command=lambda: lvlassig(4))
    btn9.pack(side=LEFT)
    if haspygame == False:
        btn9['state'] = 'disabled'
    btn10 = Button(root,text='Level 5',bg='lime green',command=lambda: lvlassig(5))
    btn10.pack(side=LEFT)
    if haspygame == False:
        btn10['state'] = 'disabled'
    btn11 = Button(root,text='Level 6',bg='lime green',command=lambda: lvlassig(6))
    btn11.pack(side=LEFT)
    if haspygame == False:
        btn11['state'] = 'disabled'
    btn3 = Button(root,text='Check for updates',bg='skyblue',command=cfu)
    btn3.pack(side=RIGHT)
    if hasreq == False:
        btn3['state'] = 'disabled'
    btn5 = Button(root,text='Switch to girl character',bg='pink',command=girl)
    btn5.pack()
    if not os.path.isfile('girl.png'):
        btn5['state'] = 'disabled'
    btn6 = Button(root,text='Switch to boy character',bg='sky blue',command=boy)
    btn6.pack()
    btn7 = Button(root,text='Import character',bg='black',fg='white',command=importchar)
    btn7.pack()

    
    
    btn1 = Button(root,text='Exit',bg='Red',command=die)
    btn1.pack(side=BOTTOM)
    
    btn2 = Button(root,text='How To Play',bg='yellow',command=lambda: os.startfile('how_to_play.txt'))
    btn2.pack(side=BOTTOM)
    if os.path.isfile('how_to_play.txt') == False:
        log(x,'Could not find file "how_to_play.txt"')
        btn2['state'] = 'disabled'
    lbl1 = Label(root,text='Avoiders Build 0.5.0 (c) 2021 Enderbyte Programs')
    lbl1.place(x=0,y=root.winfo_height()+25)
    
    root.protocol("WM_DELETE_WINDOW", disable_event)
    root.mainloop()
    root.quit()
    
    if os.path.isfile('default.dat') == True:
        f = open('default.dat')
        charpic = f.read()
        if os.path.isfile(charpic):
            f.close()
        else:
            f.close()
            f = open('default.dat','w+')
            f.write('boy.png')
            f.close()
    else:
        f = open('default.dat','x')
        f.write('boy.png')
        f.close()
    if lvl == 1:
        log(x,'Level 1: Preparing')
        class Player(pygame.sprite.Sprite):
            
            def __init__(self):
                global charpic
                
                super(Player,self).__init__()
                global ivif
                try:
                    self.surf = pygame.image.load(charpic).convert()
                except:
                    log(x,'Loaded invalid image file')
                    Tk().withdraw()
                    messagebox.showwarning('Game','Please use a valid image file')
                    charpic = 'boy.png'
                    
                    f = open('default.dat','w+')
                    f.write('boy.png')
                    f.close()
                    
                    ivif = True
                else:
                    ivif = False
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
            if ivif == True:
                break
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
            
            m = messagebox.askyesno('Game','You win level 1! Do you want to play Level 2?')
            if m == True:
                lvl = 2
        elif win == False:
            Tk().withdraw()
            messagebox.showwarning('Game','You died.')

    if lvl == 2:
        log(x,'Level 2: Preparing')
        class Player(pygame.sprite.Sprite):
            def __init__(self):
                global charpic
                super(Player,self).__init__()
                global ivif
                try:
                    self.surf = pygame.image.load(charpic).convert()
                except:
                    log(x,'Loaded invalid image file')
                    Tk().withdraw()
                    messagebox.showwarning('Game','Please use a valid image file')
                    charpic = 'boy.png'
                    
                    f = open('default.dat','w+')
                    f.write('boy.png')
                    f.close()
                    
                    ivif = True
                else:
                    ivif = False
                
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
            if ivif == True:
                break
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
            
            m = messagebox.askyesno('Game','You win level 2! Do you want to play level 3?')
            if m == True:
                lvl = 3
        elif win == False:
            Tk().withdraw()
            messagebox.showwarning('Game','You died.')
        
    if lvl == 3:
        log(x,'Level 3: Preparing')
        class Player(pygame.sprite.Sprite):
            def __init__(self):
                global charpic
                super(Player,self).__init__()
                global ivif
                try:
                    self.surf = pygame.image.load(charpic).convert()
                except:
                    log(x,'Loaded invalid image file')
                    Tk().withdraw()
                    messagebox.showwarning('Game','Please use a valid image file')
                    charpic = 'boy.png'
                    
                    f = open('default.dat','w+')
                    f.write('boy.png')
                    f.close()
                    
                    ivif = True
                else:
                    ivif = False
                
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
        class Obs3(pygame.sprite.Sprite):
            def __init__(self):
                super(Obs3,self).__init__()
                self.surf = pygame.Surface((50,400))
                self.surf.fill((255,255,255))
                self.rect = self.surf.get_rect(center=(200,325))
        clock = pygame.time.Clock()
        pygame.init()
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        a = pygame.image.load('ep.ico')
        screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        pygame.display.set_caption('Game Level 3')
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
        obs3 = Obs3()
        obstacles.add(obs3)
        all_sprites.add(obs3)
        obstacles.add(obs2)
        obstacles.add(obstacle)
        all_sprites.add(obstacle)
        all_sprites.add(obs2)
        running = True
        log(x,'level 3: Started')
        while running:
            if ivif == True:
                break
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
            
            m = messagebox.askyesno('Game','You win level 3! Do you want to play level 4?')
            if m == True:
                lvl = 4
        elif win == False:
            Tk().withdraw()
            messagebox.showwarning('Game','You died.')



    if lvl == 4:
        log(x,'Level 4: Preparing')
        class Player(pygame.sprite.Sprite):
            def __init__(self):
                global charpic
                super(Player,self).__init__()
                global ivif
                try:
                    self.surf = pygame.image.load(charpic).convert()
                except:
                    log(x,'Loaded invalid image file')
                    Tk().withdraw()
                    messagebox.showwarning('Game','Please use a valid image file')
                    charpic = 'boy.png'
                    
                    f = open('default.dat','w+')
                    f.write('boy.png')
                    f.close()
                    
                    ivif = True
                else:
                    ivif = False
                
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
        class Obs3(pygame.sprite.Sprite):
            def __init__(self):
                super(Obs3,self).__init__()
                self.surf = pygame.Surface((50,400))
                self.surf.fill((255,255,255))
                self.rect = self.surf.get_rect(center=(200,300))
        class Obs4(pygame.sprite.Sprite):
            def __init__(self):
                super(Obs4,self).__init__()
                self.surf = pygame.Surface((350,50))
                self.surf.fill((255,255,255))
                self.rect = self.surf.get_rect(center=(275,300))
        clock = pygame.time.Clock()
        pygame.init()
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        a = pygame.image.load('ep.ico')
        screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        pygame.display.set_caption('Game Level 4')
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
        obs3 = Obs3()
        obs4 = Obs4()
        obstacles.add(obs4)
        obstacles.add(obs3)
        
        obstacles.add(obs2)
        obstacles.add(obstacle)
        for obstac in obstacles:
            all_sprites.add(obstac)
        
        running = True
        log(x,'level 4: Started')
        while running:
            if ivif == True:
                break
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
            
            m = messagebox.askyesno('Game','You win level 4! Do you want to play level 5?')
            if m == True:
                lvl = 5
        elif win == False:
            Tk().withdraw()
            messagebox.showwarning('Game','You died.')

    if lvl == 5:

        log(x,'Level 5: Preparing')
        class Player(pygame.sprite.Sprite):
            def __init__(self):
                global charpic
                super(Player,self).__init__()
                global ivif
                try:
                    self.surf = pygame.image.load(charpic).convert()
                except:
                    log(x,'Loaded invalid image file')
                    
                    charpic = 'boy.png'
                    
                    f = open('default.dat','w+')
                    f.write('boy.png')
                    f.close()
                    
                    ivif = True
                else:
                    ivif = False
                
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
                self.surf = pygame.Surface((20,10))
                self.surf.fill((255,255,255))
                self.rect = self.surf.get_rect(center=(random.randint(0,SCREEN_WIDTH),0))
            def update(self):
                self.rect.move_ip(0,5)
                if self.rect.bottom >= SCREEN_HEIGHT:
                    self.kill()

        clock = pygame.time.Clock()
        pygame.init()
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        a = pygame.image.load('ep.ico')
        screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        ADDOBS = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDOBS,1000)
        pygame.display.set_caption('Game Level 5')
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
        log(x,'Level 5 Started')
        while running:
            if ivif == True:
                for entities in obstacles:
                    entities.kill()
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == ADDOBS:
                    newobs = Obstacle()
                    obstacles.add(newobs)
                    all_sprites.add(newobs)
                        
            pressed_keys = pygame.key.get_pressed()
            player.update(pressed_keys)
            screen.fill((0,0,0))
            obstacles.update()
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
        if ivif == True:
            Tk().withdraw()
            messagebox.showwarning('Game','Please use a valid image file')
        if win == True:
            Tk().withdraw()
            
            m = messagebox.askyesno('Game','You win level 5! Do you want to play level 6?')
            if m == True:
                lvl = 5
        elif win == False:
            Tk().withdraw()
            messagebox.showwarning('Game','You died.')

    if lvl == 6:

        log(x,'Level 6: Preparing')
        class Player(pygame.sprite.Sprite):
            def __init__(self):
                global charpic
                super(Player,self).__init__()
                global ivif
                try:
                    self.surf = pygame.image.load(charpic).convert()
                except:
                    log(x,'Loaded invalid image file')
                    
                    charpic = 'boy.png'
                    
                    f = open('default.dat','w+')
                    f.write('boy.png')
                    f.close()
                    
                    ivif = True
                else:
                    ivif = False
                
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
                self.surf = pygame.Surface((20,10))
                self.surf.fill((255,255,255))
                self.rect = self.surf.get_rect(center=(random.randint(0,SCREEN_WIDTH),0))
                self.speed = random.randint(5,20)
            def update(self):
                self.rect.move_ip(0,self.speed)
                if self.rect.bottom >= SCREEN_HEIGHT:
                    self.kill()

        

        clock = pygame.time.Clock()
        pygame.init()
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        a = pygame.image.load('ep.ico')
        screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        ADDOBS = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDOBS,500)
        pygame.display.set_caption('Game Level 6')
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
        log(x,'Level 6 Started')
        while running:
            if ivif == True:
                for entities in obstacles:
                    entities.kill()
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == ADDOBS:
                    newobs = Obstacle()
                    obstacles.add(newobs)
                    all_sprites.add(newobs)
                        
            pressed_keys = pygame.key.get_pressed()
            player.update(pressed_keys)
            screen.fill((0,0,0))
            obstacles.update()
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
        if ivif == True:
            Tk().withdraw()
            messagebox.showwarning('Game','Please use a valid image file')
        if win == True:
            Tk().withdraw()
            
            m = messagebox.askyesno('Game','You win level 6! Do you want to play level 7?')
            if m == True:
                lvl = 7
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
