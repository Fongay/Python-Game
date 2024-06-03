import pygame
pygame.init()
def settings():
    scX, scY = 1920, 1080
    sc = pygame.display.set_mode([scX,scY])





    
    run = True
    while run:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False