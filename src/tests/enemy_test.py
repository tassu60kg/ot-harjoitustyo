import unittest
import pygame
import enemy
from player import Player
from game import main


class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.srceen = pygame.display.set_mode((500, 500))
        self.enemy = enemy.Spawncontroller()
        self.enemy1 = enemy.Enemy1()

    def test_down_movement(self):
        player = Player(100, 100)
        self.enemy.enemy.add(enemy.Enemy1(100, 0))
        for _ in range(10):
            self.enemy.move_enemy(player.rect)
        for i in self.enemy.enemy:
            n = i.rect.y
        self.assertAlmostEqual(n, 20)

    def test_up_movement(self):
        player = Player(100, 0)
        self.enemy.enemy.add(enemy.Enemy1(100, 100))
        for _ in range(10):
            self.enemy.move_enemy(player.rect)
        for i in self.enemy.enemy:
            n = i.rect.y
        self.assertAlmostEqual(n, 80)

    def test_left_movement(self):
        player = Player(0, 100)
        self.enemy.enemy.add(enemy.Enemy1(100, 100))
        for _ in range(10):
            self.enemy.move_enemy(player.rect)
        for i in self.enemy.enemy:
            n = i.rect.x
        self.assertAlmostEqual(n, 80)

    def test_right_movement(self):
        player = Player(100, 100)
        self.enemy.enemy.add(enemy.Enemy1(0, 100))
        for _ in range(10):
            self.enemy.move_enemy(player.rect)
        for i in self.enemy.enemy:
            n = i.rect.x
        self.assertAlmostEqual(n, 20)

    def test_no_movement(self):
        player = Player(100, 100)
        self.enemy.enemy.add(enemy.Enemy1(100, 100))
        for _ in range(10):
            self.enemy.move_enemy(player.rect)
        for i in self.enemy.enemy:
            n = i.rect.x
            m = i.rect.y
        self.assertAlmostEqual(n+m, 200)

    def test_summoning(self):
        self.enemy.summon(1, self.srceen, True, (100, 100))
        self.assertEqual(len(self.enemy.enemy), 1)
    
    def test_summoning2(self):
        self.enemy.summon(2, self.srceen, True, (100, 100))
        self.assertEqual(len(self.enemy.enemy), 1)
