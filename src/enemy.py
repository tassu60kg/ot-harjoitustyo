import pygame
import math
import random

class Enemy1(pygame.sprite.Sprite): #basic red square enemy
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.Surface((30,30),pygame.SRCALPHA)
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = pygame.math.Vector2(1,1)
        self.move_speed = 1

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.Surface((30,30),pygame.SRCALPHA)
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = pygame.math.Vector2(1,1)
        self.move_speed = 1.5

class Spawncontroller():
    def __init__(self):
        self.enemy = pygame.sprite.Group()
        
    def summon(self,enemy,screen,forcepos=False, pos=(0,0)):
        if enemy == 1: 
            if forcepos == True:
                x = pos[0]
                y = pos[1]
                self.enemy.add(Enemy1(x,y))
            else: 
                angle = random.randint(0,157)/100
                x = screen[0]+random.choice([1,-1])*math.cos(angle)*600
                y = screen[1]+random.choice([1,-1])*math.sin(angle)*600
                self.enemy.add(Enemy1(x,y))
        elif enemy == 2:
            if forcepos == True:
                x = pos[0]
                y = pos[1]
                self.enemy.add(Enemy2(x,y))
            else: 
                angle = random.randint(0,157)/100
                x = screen[0]+random.choice([1,-1])*math.cos(angle)*600
                y = screen[1]+random.choice([1,-1])*math.sin(angle)*600
                self.enemy.add(Enemy2(x,y))

                
    def move_enemy(self,player):
        for i in self.enemy:
            i.dir.x = player[0] - i.rect.x 
            i.dir.y = player[1] - i.rect.y
            if not (i.dir.x == 0 and i.dir.y == 0):
                i.dir.normalize_ip()   
                i.dir*=2
                i.rect.x += i.dir.x * i.move_speed
                i.rect.y += i.dir.y* i.move_speed
