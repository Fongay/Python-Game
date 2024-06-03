import pygame
pygame.init()
def help():
    scX, scY = 1920, 1080
    sc = pygame.display.set_mode([scX,scY])
    menu = pygame.image.load(r"menu spr/help_menu.png").convert_alpha()
    at = pygame.image.load(r"menu spr/tap_to_ex.png").convert_alpha()
    alpha = 0
    alpha_1 = 0
    run = True
    while run:
        alpha_1 += 1
        alpha +=1
        menu.set_alpha(alpha)
        at.set_alpha(alpha_1)
        sc.blit(menu, [0,0])
        if alpha_1 <255:
            sc.blit(at, [1580, 940])
        pygame.display.flip()
        if alpha_1 == 254:
            for i in range(250):
                alpha_1 -= 1
                at.set_alpha(alpha_1)
                sc.blit(menu, [0, 0])
                sc.blit(at, [1580, 940])
                pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.QUIT:
                run = False