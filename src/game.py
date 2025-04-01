import pygame
import os

#will be split into multiple files

class Player(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0):
        super().__init__()
        
        self.image = pygame.Surface((30,30))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Wall(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0):
        super().__init__()
        
        self.image = pygame.Surface((200,200))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Floor(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0):
        super().__init__()
        
        self.image = pygame.Surface((200,200))
        self.image.fill((25,25,25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Level:
    def __init__(self,map,tile_size):
        self.tile_size = tile_size
        self.map = map
        self.player = Player(50,50)
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


        self.sprites.add(self.floors,self.walls)
    
    def player_controller(self,dx=0,dy=0):
        self.player.rect.move_ip(dx,dy)




map = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
tile_size = 200

def main():
    height = len(map)
    width = len(map[0])    
    realheight = height*tile_size
    realwidth = width*tile_size

    display = pygame.display.set_mode((realwidth, realheight))

    pygame.display.set_caption("ts pmo")

    level = Level(map,tile_size)


    pygame.init()

    level.sprites.draw(display)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    
    pygame.quit()




if __name__ == "__main__":
    main()

