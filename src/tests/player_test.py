import unittest
import pygame
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(100, 100)
        self.srceen = pygame.display.set_mode((500, 500))

    def test_move_down(self):
        self.player.moveplayery(1)
        self.player.move_player(10,pygame.sprite.Group())
        self.assertEqual(self.player.rect.y, 110)

    def test_move_up(self):
        self.player.moveplayery(-1)
        self.player.move_player(10,pygame.sprite.Group())
        self.assertEqual(self.player.rect.y, 90)

    def test_move_right(self):
        self.player.moveplayerx(1)
        self.player.move_player(10,pygame.sprite.Group())
        self.assertEqual(self.player.rect.x, 110)

    def test_move_left(self):
        self.player.moveplayerx(-1)
        self.player.move_player(10,pygame.sprite.Group())
        self.assertEqual(self.player.rect.x, 90)
