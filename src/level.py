import pygame
from player import Player


class Wall(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Floor(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.Surface((100, 100))
        self.image.fill((25, 25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Level:
    def __init__(self, map, tile_size):
        self.tile_size = tile_size
        self.map = map
        self.player = None
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self._mapmaker(self.map)

    def _mapmaker(self, map):

        height = len(map)
        width = len(map[0])

        for x in range(width):  # make less bad
            for y in range(height):
                tile = map[y][x]
                real_x = x*self.tile_size
                real_y = y*self.tile_size

                if tile == 0:
                    self.floors.add(Floor(real_x, real_y))

                elif tile == 1:
                    self.walls.add(Wall(real_x, real_y))

                elif tile == 2:
                    self.player = Player(real_x, real_y)
                    self.walls.add(Floor(real_x, real_y))

        self.sprites.add(self.floors, self.walls, self.player)
