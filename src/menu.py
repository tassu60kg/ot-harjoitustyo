import pygame
from game import main

def loadmap(map,tile_size):
     main(map,tile_size)

running = True
map = [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [1,0,1,0,1,2,1,0,1],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]

tile_size = 100
pygame.init()
pygame.font.init()
print(pygame.display.Info().current_h)
display = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h)) 
font = pygame.font.SysFont('Comic Sans MS', 40)
font2 = pygame.font.SysFont('Comic Sans MS', 25)
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    loadmap([[1,1,1,1,0,0,1,1,1,1],
                    [1,1,0,0,0,0,0,0,1,1],
                    [1,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,1],
                    [0,0,0,0,1,1,0,0,0,0],
                    [0,0,0,0,1,1,0,0,0,0],
                    [1,0,0,0,0,0,2,0,0,1],
                    [1,0,0,0,0,0,0,0,0,1],
                    [1,1,0,0,0,0,0,0,1,1],
                    [1,1,1,1,0,0,1,1,1,1]],
                    100)
                if event.key == pygame.K_2:
                    loadmap([[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [1,0,1,0,1,2,1,0,1],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0], 
                    [0,0,0,0,0,0,0,0,0]],
                    100)
                if event.key == pygame.K_3:
                    loadmap([[0,0,0,2,0,0,0,0,0,0,0,0,0],
                    [0,1,0,1,0,1,0,1,0,1,0,1,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,1,0,1,0,1,0,1,0,1,0,1,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,1,0,1,0,1,0,1,0,1,0,1,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,1,0,1,0,1,0,1,0,1,0,1,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0]],
                    90)
                if event.key == pygame.K_4:
                    loadmap([[2]],1000)
                if event.key == pygame.K_5:
                    loadmap([[2]],100)

    display.blit(font.render(f"video peli", True, (100, 100, 100)), (150,0))        
    display.blit(font2.render(f"texti tbd, valitse numeroilla", True, (100, 100, 100)), (150,pygame.display.Info().current_h//10))
    display.blit(font2.render(f"1: liikenneympyrä", True, (100, 100, 100)), (150,2*(pygame.display.Info().current_h//10)))
    display.blit(font2.render(f"2: suojatie", True, (100, 100, 100)), (150,3*(pygame.display.Info().current_h//10)))
    display.blit(font2.render(f"3: pilarit", True, (100, 100, 100)), (150,4*(pygame.display.Info().current_h//10)))
    display.blit(font2.render(f"4: hyvä, älä pelaa", True, (100, 100, 100)), (150,5*(pygame.display.Info().current_h//10)))
    display.blit(font2.render(f"5: huono, älä pelaa", True, (100, 100, 100)), (150,6*(pygame.display.Info().current_h//10)))

    pygame.display.update()
    pygame.time.wait(25)
pygame.quit()

