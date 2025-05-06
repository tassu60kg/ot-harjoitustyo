import pygame
from level import Level
from enemy import Spawncontroller
from math import floor


def main(map,tile_size): 
    height = len(map)
    width = len(map[0])
    realheight = height*tile_size
    realwidth = width*tile_size
    display = pygame.display.set_mode((realwidth, realheight))
    pygame.display.set_caption("qwsd to move, mouse to shoot")
    movespeed = 5
    level = Level(map, tile_size)
    spawncontroller = Spawncontroller()
    pygame.init()
    level.sprites.draw(display)
    pygame.font.init() 
    font = pygame.font.SysFont('Comic Sans MS', 30)
    
    time_alive = 1
    enemy1_delay = 150
    enemy2_delay = 250

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                level.player.shooter(pygame.mouse.get_pos(),
                                     display, spawncontroller.enemy)
                xd = pygame.mouse.get_pos()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and level.player.rect.x < realwidth - 30:
            level.player.moveplayerx(1)
        if keys[pygame.K_q] and level.player.rect.x > 0:
            level.player.moveplayerx(-1)
        if keys[pygame.K_w] and level.player.rect.y > 0:
            level.player.moveplayery(-1)
        if keys[pygame.K_s] and level.player.rect.y < realheight - 30:
            level.player.moveplayery(1)
        
        level.player.move_player(movespeed,level.walls)

        if time_alive % enemy1_delay == 0:
            spawncontroller.summon(1, (realwidth//2, realheight//2))
        if time_alive % enemy2_delay == 0:
            spawncontroller.summon(2, (realwidth//2, realheight//2))
        if time_alive % 500 == 0:
            spawncontroller.difficulty *= 1.1
            enemy1_delay = floor(enemy1_delay * 0.9)
            enemy2_delay = floor(enemy2_delay * 0.95)
        

        level.sprites.draw(display)
        spawncontroller.enemy.draw(display)
        display.blit(font.render(f"{time_alive//40}", True, (100, 100, 100)), (10,10))
        pygame.display.update()
        time_alive += 1
        spawncontroller.move_enemy((level.player.rect.x, level.player.rect.y))

        if level.player.die(spawncontroller.enemy):
            pygame.display.set_caption("you dead")
        
        pygame.time.wait(25)

    pygame.quit()


