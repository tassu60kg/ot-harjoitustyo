import unittest
import pygame
from level import Level
from player import Player


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.screen = pygame.display.set_mode((500, 500))
        map = [[0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 2]]
        self.level = Level(map, 100)

    def test_wall(self):
        for i in self.level.walls:
            n = i
        self.assertEqual(n.rect, (400, 400, 100, 100))
