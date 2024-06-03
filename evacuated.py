import pygame
pygame.init()
def evac():
    scX = 1920
    scY = 1080
    sc = pygame.display.set_mode([scX, scY])
    menu = pygame.image.load(r'game_spr/evac_v2.png')
    sc.blit(menu, [0, 0])
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False