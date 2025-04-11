import pygame
from level import Level
from enemy import Spawncontroller



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
                level.player.shooter(pygame.mouse.get_pos(),display,spawncontroller.enemy)
                xd = pygame.mouse.get_pos()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            level.player.moveplayerx(movespeed)
        if keys[pygame.K_q]:
            level.player.moveplayerx(-movespeed)
        if keys[pygame.K_w]:
            level.player.moveplayery(-movespeed)
        if keys[pygame.K_s]:
            level.player.moveplayery(movespeed)
        
           
        if n%20 == 0: spawncontroller.summon(1,(realwidth//2,realheight//2))
        


        level.sprites.draw(display)
        spawncontroller.enemy.draw(display)
        pygame.display.update()
        n+=1
        spawncontroller.move_enemy((level.player.rect.x,level.player.rect.y))
        pygame.time.wait(30)

    pygame.quit()




if __name__ == "__main__":
    main()

