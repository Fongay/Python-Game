import pygame, About, GAME, help_file
pygame.init()
scX = 1920
scY = 1080
sc = pygame.display.set_mode([scX,scY])
top = [400,550,700,850]
x, xp = 0, -20
y, yp = 0, 540
col = 0
nig1, nig2 = -230, 1080
bp = 1320
time = 100
play = pygame.image.load(r'menu spr/play3.png').convert_alpha()
help = pygame.image.load(r'menu spr/help2.png').convert_alpha()
about = pygame.image.load(r'menu spr/about2.png').convert_alpha()
exit = pygame.image.load(r'menu spr/exit1.png').convert_alpha()
sprite = pygame.image.load(r'game_spr/player/player1.png').convert_alpha()
sprite = pygame.transform.scale(sprite, (256, 320))
menuButton = [play, help, about, exit]
run = True
clock = pygame.time.Clock()
fps = 60
local = 12

def player_anim(w1, h1, k, sprite):
    frame = []
    weidth, heidth = sprite.get_size()
    w, h = weidth // w1, heidth // h1
    cout = 0
    for i in range(int(heidth / h)):
        for j in range(int(weidth / w)):
            x = sprite.subsurface(pygame.rect.Rect(j * w, cout, w, h))
            frame.append(x)
        cout += int(h)
    cout2 = 0
    return frame
local_l = 0
def menu_func(local,xp,col, local_l, nig1, nig2):
    if col < 254:
        col += 1
    if col > 245 and xp < 960:
        if local < 16:
            local_l += 1
            if local_l >6:
                local += 1
                local_l = 0
        if local > 15:
            local = 12
        xp += 2
        sc.fill([col, col, col])
        sc.blit(frame[local], [xp, yp])

    elif col > 245:
        if local < 16:
            local_l += 1
            if local_l >6:
                local += 1
                local_l = 0
            if local > 15:
                local = 12
        sc.fill([col, col, col])

        sc.blit(frame[local], [xp, yp])
    pygame.draw.rect(sc, [0, 0, 0], (0, nig1, 1920, 230))
    pygame.draw.rect(sc, [0, 0, 0], (0, nig2, 1920, 1080))

    return local,xp,col, local_l

frame = player_anim(4, 5, 20, sprite)

while run:
    if nig1 < -2:
        nig1 += 3
    if nig2 > 850:
        nig2 -= 3
    if bp > 1920:
        bp = 1320
    sc.fill([col, col, col])
    local,xp,col, local_l = menu_func(local, xp, col, local_l, nig1, nig2)

    for i in range(4):
        sc.blit(menuButton[i], [1320, top[i]])
    clock.tick(fps)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            for u in range(4):
                if (x > 1320) and (y > top[u]) and y < (top[u] + 80):
                    break
                else:
                    u = 10

            if u == 0:
                print('game')
                for j in range(time):
                    sc.fill([col, col, col])
                    local,xp,col, local_l = menu_func(local, xp, col, local_l, nig1, nig2)
                    for i in range(4):
                        if i != 0:
                            sc.blit(menuButton[i], [1320, top[i]])
                        else:
                            bp +=10
                            sc.blit(menuButton[i], [bp, top[i]])
                    clock.tick(fps)
                    pygame.display.update()
                GAME.game()

            elif u == 1:
                print('help')
                for j in range(time):
                    sc.fill([col, col, col])
                    local,xp,col, local_l = menu_func(local, xp, col, local_l, nig1, nig2)
                    for i in range(4):
                        if i != 1:
                            sc.blit(menuButton[i], [1320, top[i]])
                        else:
                            bp +=10
                            sc.blit(menuButton[i], [bp, top[i]])
                    clock.tick(fps)
                    pygame.display.update()
                help_file.help()

            elif u == 2:
                print('About')
                for j in range(time):
                    sc.fill([col, col, col])
                    local,xp,col, local_l = menu_func(local, xp, col, local_l, nig1, nig2)
                    for i in range(4):
                        if i != 2:
                            sc.blit(menuButton[i], [1320, top[i]])
                        else:
                            bp +=10
                            sc.blit(menuButton[i], [bp, top[i]])
                    clock.tick(fps)
                    pygame.display.update()
                About.about()

            elif u == 3:
                for j in range(time):
                    sc.fill([col, col, col])
                    local, xp, col, local_l = menu_func(local, xp, col, local_l, nig1, nig2)
                    for i in range(4):
                        if i != 3:
                            sc.blit(menuButton[i], [1320, top[i]])
                        else:
                            bp +=10
                            sc.blit(menuButton[i], [bp, top[i]])
                    clock.tick(fps)
                    pygame.display.update()
                run = False

pygame.quit()