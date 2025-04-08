import os
import math
import random
import pygame

#will be split into multiple files

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.image = pygame.Surface((30,30),pygame.SRCALPHA)
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def moveplayerx(self,x=0):
        self.rect.x += x
    def moveplayery(self,y=0):
        self.rect.y += y
    
    def shooter(self,mouse,display):
        pygame.draw.line(display,(255,0,0),(self.rect.x+15,self.rect.y+15),(mouse[0],mouse[1]))
        pygame.display.flip()


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.Surface((30,30),pygame.SRCALPHA)
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = pygame.math.Vector2(1,1)


class Spawncontroller():
    def __init__(self):
        self.enemy = pygame.sprite.Group()
        

    def summon(self,enemy,playerlocation):
        if enemy == 1: 
            x = playerlocation[0]+random.choice([5,-5])*math.ceil(math.sin(random.randint(15,157)/100)*85)
            y = playerlocation[1]+random.choice([5,-5])*math.ceil(math.sin(random.randint(15,157)/100)*85)
            self.enemy.add(Enemy1(x,y))
            
    def move_enemy(self,player):
        for i in self.enemy:
            if player[0] > i.rect.x:
                i.dir.x = 1
            if player[0] < i.rect.x:
                i.dir.x = -1
            if player[0] == i.rect.x:
                i.dir.x = 0
            if player[1] > i.rect.y:
                i.dir.y = 1
            if player[1] < i.rect.y:
                i.dir.y = -1
            if player[1] == i.rect.y:
                i.dir.y = 0.1
            i.dir.normalize_ip()
            i.rect.x += i.dir.x
            i.rect.y += i.dir.y
                
                
        

class Wall(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0):
        super().__init__()
        
        self.image = pygame.Surface((100,100))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Floor(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0):
        super().__init__()
        
        self.image = pygame.Surface((100,100))
        self.image.fill((25,25,25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Level:
    def __init__(self,map,tile_size):
        self.tile_size = tile_size
        self.map = map
        self.player = None
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self._mapmaker(self.map)
    

    def _mapmaker(self,map):
        
        height = len(map)
        width = len(map[0]) 
        
        for x in range(width): #make less bad
            for y in range(height):
                tile = map[y][x]
                real_x = x*self.tile_size
                real_y = y*self.tile_size

                if tile == 0:
                    self.floors.add(Floor(real_x,real_y))

                elif tile == 1:
                    self.walls.add(Wall(real_x,real_y))
                
                elif tile == 2:
                    self.player = Player(real_x,real_y)
                    self.walls.add(Floor(real_x,real_y))
                    

        self.sprites.add(self.floors,self.walls,self.player)
    
    





map = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,2,0,0,1,0,0],
        [0,0,1,0,0,0,1,1,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],]
tile_size = 100

def main():
    height = len(map)
    width = len(map[0])    
    realheight = height*tile_size
    realwidth = width*tile_size

    display = pygame.display.set_mode((realwidth, realheight))


    pygame.display.set_caption("ts pmo")

    movespeed = 5

    level = Level(map,tile_size)

    spawncontroller = Spawncontroller()

    pygame.init()

    level.sprites.draw(display)

    running = True

    n=0
    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                level.player.shooter(pygame.mouse.get_pos(),display)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            level.player.moveplayerx(movespeed)
        if keys[pygame.K_q]:
            level.player.moveplayerx(-movespeed)
        if keys[pygame.K_w]:
            level.player.moveplayery(-movespeed)
        if keys[pygame.K_s]:
            level.player.moveplayery(movespeed)
        
           
        if n%10 == 0: spawncontroller.summon(1,(level.player.rect.x,level.player.rect.y))
        
        level.sprites.draw(display)
        spawncontroller.enemy.draw(display)
        pygame.display.update()
        n+=1
        spawncontroller.move_enemy((level.player.rect.x,level.player.rect.y))
        pygame.time.wait(30)

    pygame.quit()




if __name__ == "__main__":
    main()

