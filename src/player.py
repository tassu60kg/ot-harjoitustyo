"player functions"
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = pygame.math.Vector2(0, 0)
        self.cubes_terminated = 0

    def move_player(self, movespeed, walls):
        if not (self.dir.x == 0 and self.dir.y == 0):
            self.dir.normalize_ip()
            self.dir *= movespeed
            self.rect.x += self.dir.x
            self.rect.y += self.dir.y
            for i in walls:
                if self.rect.colliderect(i):
                    self.rect.x -= self.dir.x
                    self.rect.y -= self.dir.y
                    break
            self.dir.x = 0
            self.dir.y = 0

    def moveplayerx(self, x=0):
        self.dir.x = x

    def moveplayery(self, y=0):
        self.dir.y = y

    def shooter(self, mouse, display, enemy):
        pygame.draw.line(display, (255, 0, 0), (self.rect.x+15,
                         self.rect.y+15), (mouse[0], mouse[1]))
        for i in enemy:
            if i.rect.clipline((self.rect.x+15, self.rect.y+15), (mouse[0], mouse[1])) != ():
                enemy.remove(i)
                self.cubes_terminated += 1
        pygame.display.flip()

    def die(self, enemy):
        for i in enemy:
            if self.rect.colliderect(i):
                return True
        return False
