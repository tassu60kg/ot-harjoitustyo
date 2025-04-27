import pygame   


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
    
    def shooter(self,mouse,display,enemy):
        pygame.draw.line(display,(255,0,0),(self.rect.x+15,self.rect.y+15),(mouse[0],mouse[1]))
        for i in enemy:
            if i.rect.clipline((self.rect.x+15,self.rect.y+15),(mouse[0],mouse[1])) != ():
                enemy.remove(i)
        pygame.display.flip()

    def die(self,enemy):
        for i in enemy:
            if self.rect.colliderect(i):
                return True
        return False