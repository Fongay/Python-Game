import pygame, random, math, evacuated
pygame.init()
def game():
    # переменные, и легаси переменные #
    wh, hh = 128, 128
    cout2, stay = 0, 0
    ammo_het, med_het = 0, 0
    N, a_tic = 0, 0
    ZX, ZY = [], []
    AX, AY, MX, MY = [], [], [], []
    rplX, rplY = 0, 0
    plX, plY = 960, 540
    vector = [0, 0]
    scX, scY = 1920, 1080
    sc = pygame.display.set_mode([scX, scY])
    w1, h1, k = 4, 6, 20
    x_b, y_b = 0, 0
    reload, dead_v = 0, 0
    score = 0
    lolololoo = 0
    player_dead = False
    debug_mod = False
    zom_dead = -1
    zombi_colich = 4
    sbros_last_vec = 0
    ammo = 12
    HP = 300
    ras = 7
    boss_HP = 100
    boss_active = False
    my_font = pygame.font.SysFont('impact', 32, bold=False, italic=False)
    # загрузка спрайтов и тайлов #
    med = pygame.image.load(r"game_spr/player/med.png").convert_alpha()
    open_ammobox = pygame.image.load(r"game_spr/player/ammobox2.png").convert_alpha()
    close_ammobox = pygame.image.load(r"game_spr/player/ammobox1.png").convert_alpha()
    road = pygame.image.load(r"game_spr/ground_asf.png").convert_alpha()
    grass = pygame.image.load(r"game_spr/grown.png").convert_alpha()
    sprite = pygame.image.load(r'game_spr/player/player_1.png').convert_alpha()
    bpla = pygame.image.load(r"game_spr/ee_bpla-sheet0.png").convert_alpha()
    home1 = pygame.image.load(r"game_spr/home 1/house_1.png").convert_alpha()
    home1_int = pygame.image.load(r"game_spr/home 1/house_1_int.png").convert_alpha()
    home2 = pygame.image.load(r"game_spr/home 1/house_2.png").convert_alpha()
    home2_int = pygame.image.load(r"game_spr/home 1/house_2_int.png").convert_alpha()
    home1_door = pygame.image.load(r"game_spr/home 1/door.png").convert_alpha()
    home4 = pygame.image.load(r"game_spr/home 1/house_4.png").convert_alpha()
    home4_int = pygame.image.load(r"game_spr/home 1/house_4_int.png").convert_alpha()
    dead_tabl = pygame.image.load(r"game_spr/player/dead_tabl.png").convert_alpha()
    dead_tabl2 = pygame.image.load(r"game_spr/player/dead_tabl2.png").convert_alpha()
    reload_spine = pygame.image.load(r"game_spr/player/reloading_spinner-sheet0.png").convert_alpha()
    reload_sprite = pygame.image.load(r"game_spr/player/reloading_icon-sheet0.png").convert_alpha()
    life_1 = pygame.image.load(r"game_spr/player/life_1.png").convert_alpha()
    life_2 = pygame.image.load(r"game_spr/player/life_2.png").convert_alpha()
    car_1_v = pygame.image.load(r"game_spr/cars/car_regular_gray_vert-sheet0.png").convert_alpha()
    car_2_v = pygame.image.load(r"game_spr/cars/car_regular_green_vert-sheet0.png").convert_alpha()
    car_3_v = pygame.image.load(r"game_spr/cars/car_police_vert-sheet0.png").convert_alpha()
    hamer_v = pygame.image.load(r"game_spr/cars/hammer_crash-sheet0.png").convert_alpha()
    car_1_g = pygame.image.load(r"game_spr/cars/car_regular_gray-sheet0.png").convert_alpha()
    car_2_g = pygame.image.load(r"game_spr/cars/car_van_black-sheet0.png").convert_alpha()
    car_3_g = pygame.image.load(r"game_spr/cars/ee_car_destroyed-sheet0.png").convert_alpha()
    hamer_g = pygame.image.load(r"game_spr/cars/hammer_crash-sheet1.png").convert_alpha()
    car_4_g = pygame.image.load(r"game_spr/cars/ee_fallcar-sheet0.png").convert_alpha()
    btr = pygame.image.load(r"game_spr/cars/car_btr-sheet0.png").convert_alpha()
    road_up = pygame.image.load(r"game_spr/ground_asf_up.png").convert_alpha()
    road_down = pygame.image.load(r"game_spr/ground_asf_down.png").convert_alpha()
    road_rigth = pygame.image.load(r"game_spr/ground_asf_right.png").convert_alpha()
    road_left = pygame.image.load(r"game_spr/ground_asf_left.png").convert_alpha()
    exit_zone = pygame.image.load(r"game_spr/exit_zone.png").convert_alpha()
    atent_press = pygame.image.load(r"game_spr/atent_press.png").convert_alpha()

    med = pygame.transform.scale(med, (40, 52))
    close_ammobox = pygame.transform.scale(close_ammobox, (63, 40))
    open_ammobox = pygame.transform.scale(open_ammobox, (63, 40))
    road = pygame.transform.scale(road, (128, 128))
    grass = pygame.transform.scale(grass, (128, 128))
    home1 = pygame.transform.scale(home1, (650, 775))
    home1_int = pygame.transform.scale(home1_int, (645, 485))
    home2 = pygame.transform.scale(home2, (650, 775))
    home2_int = pygame.transform.scale(home2_int, (645, 485))
    home4 = pygame.transform.scale(home4, (650, 775))
    home4_int = pygame.transform.scale(home4_int, (645, 485))
    dead_tabl = pygame.transform.scale(dead_tabl, (512, 128))
    car_1_v = pygame.transform.scale(car_1_v, (90, 170))
    car_2_v = pygame.transform.scale(car_2_v, (90, 170))
    car_3_v = pygame.transform.scale(car_3_v, (90, 170))
    hamer_v = pygame.transform.scale(hamer_v, (170, 180))
    hamer_g = pygame.transform.scale(hamer_g, (240, 150))
    car_1_g = pygame.transform.scale(car_1_g, (170, 90))
    car_2_g = pygame.transform.scale(car_2_g, (200, 150))
    car_3_g = pygame.transform.scale(car_3_g, (170, 90))
    car_4_g = pygame.transform.scale(car_4_g, (200, 140))
    btr = pygame.transform.scale(btr, (350, 200))
    road_up = pygame.transform.scale(road_up, (128, 128))
    road_down = pygame.transform.scale(road_down, (128, 128))
    road_rigth = pygame.transform.scale(road_rigth, (128, 128))
    road_left = pygame.transform.scale(road_left, (128, 128))

    # тотальный распил тайла на спрайты для игрока и не только #
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
        return frame

    # класс камеры (свеерический конь в вакууме) #
    class cam:
        def __init__(self, plX, plY):
            self.rect = pygame.Rect(plX, plY, 1920, 1080)

        def move(self, vector):
            self.rect[0] += vector[0]
            self.rect[1] += vector[1]

    # отрисовка игрока функ #
    def player(cout2):
        frame_scale = pygame.transform.scale(frame[cout2], (96, 96))
        frame_scale_rect_norRe = pygame.transform.scale(frame[cout2], (70, 72))
        frame_scale_rect = frame_scale_rect_norRe.get_rect()
        frame_scale_rect.topleft = [plX - 54, plY - 50]

        player_triger = pygame.transform.scale(frame[0], (1750,996))
        player_triger_rect = player_triger.get_rect()
        player_triger_rect.topleft = [plX - 880, plY - 500]
        if debug_mod == True:
            pygame.draw.rect(sc, [250, 0, 0] ,frame_scale_rect, 2)
        if vector[0] != 0 or vector[1] != 0:
            sc.blit(frame_scale, [plX-64, plY-64])
        else:
            frame_scale = pygame.transform.scale(frame[stay], (96, 96))
            sc.blit(frame_scale, [plX - 64, plY - 64])
        return frame_scale_rect, player_triger_rect

    # класс игрока (свеерический конь в вакууме) #
    class Player:
        def __init__(self, x, y):
            self.rect = pygame.Rect(x, y, 10, 10)

        def move(self, vector):
            self.rect[0] += vector[0]
            self.rect[1] += vector[1]

        def draw(self): ##  Игрок на самом окне не двигается, двигается мир вокруг него
            frame_scale_rect, player_triger_rect = player(cout2)

    # класс всех объектов кроме игрока (свеерический конь в вакууме, но только частично) #
    class object:
        ##  Это какой-нибудь объект, отличный игрока (к примеру враг или дерево)
        def __init__(self, x, y, width, height):
            self.rect = pygame.Rect(x, y, width, height)

        def draw(self, ZX, ZY, x_b, y_b, buo, zomby_frame_scale_rect, reload, dead_v, lolololoo, score, ammo, ammo_het, med_het, MX, MY, AX, AY, boss_HP, HP):
            pygame.draw.rect(sc, (255, 0, 0),(self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1], self.rect[2], self.rect[3]),2)
            N, M, map_list, count = readFile(map_path)
            map_list = drawGROWN(map_list)
            N1, M1, map_list1, coun = readFile1(map_OBJ)
            map_list2 = map_list1
            bpla_rect, vector, n, ZX, ZY, home_1_len, home_rect, car_1_v_rect, car_1_v_len, lolololoo, car_2_v_len, \
            car_2_v_rect, car_3_v_rect, car_3_v_len, hamer_v_rect, hamer_v_len, hamer_g_rect, hamer_g_len, btr_rect, \
            car_1_g_len, car_1_g_rect, car_2_g_len, car_2_g_rect, car_3_g_len, car_3_g_rect, car_4_g_len, car_4_g_rect,\
            exit_zone_rect, ammobox_rect, ammobox_len, med_rect, med_len, ammo_het, med_het, MX, MY, AX, \
            AY = drawOBJ(map_list1, ZX, ZY, lolololoo, ammo_het, med_het, MX, MY, AX, AY, ras)
            zomby_frame_scale_rect = zombi.zomby_draw(ZX, ZY, zomby_frame_scale_rect)
            buo, reload, ammo = bullet.bullet_cord(x_b, y_b, buo, reload, ammo)
            zomby_frame_scale_rect, zom_dead, score, boss_HP = bullet.bullet_draw(zomby_frame_scale_rect, score, boss_HP)
            MX, MY, AX, AY, med_rect = ammomed_draw(MX, MY, AX, AY, vector_end)
            boss.boss_draw()
            HP = boss.boss_shot(HP)

            return buo, zomby_frame_scale_rect, zom_dead, reload, dead_v, score, ammo, ammo_het, med_het, MX, MY, AX, AY, boss_HP, HP

    # класс зомби #
    class zomby:
        def __init__(self):
            self.zomby_tile = pygame.image.load(r"game_spr/zomby/zed_base.png").convert_alpha()
            self.frame_zomby = []
            self.w1, self.h1 = 4, 4
            self.cout, self.dead_count = 0, 0
            self.zomby_vector_x, self.zomby_vector_y = 0, 0
            self.num_zomby = 0
            self.zomby_frame_scale = []
            self.zomby_frame_scale_rect = []
            self.triger_rect = []
            self.dead_zom, self.dead_x, self.dead_y = [], [], []
            self.ZX_p = [0,0,0,0]
            self.frame_num = [0,0,0,0]
            self.timer = [0,0,0,0]
            self.gorizont = False

        def zomby_draw(self, ZX, ZY, zomby_frame_scale_rect):
            self.frame_zomby = player_anim(4, 5, 20, self.zomby_tile)
            self.zomby_vector_x, self.zomby_vector_y = 0, 0
            self.zomby_frame_scale_rect = []
            self.triger_rect = []
            if zom_dead > -1:
                self.zom_dead = pygame.image.load(r"game_spr/zomby/dead_zomb.png")
                self.zom_dead = pygame.transform.scale(self.zom_dead, (96, 96))
                self.dead_x.append(ZX[zom_dead])
                self.dead_y.append(ZY[zom_dead])
                ZX[zom_dead] = -10000
                ZY[zom_dead] = -10000
                self.dead_count += 1
            for i in range(zombi_colich):

                self.zomby_frame_scale = pygame.transform.scale(self.frame_zomby[self.frame_num[i]], (96, 96))
                zomby_frame_scale_rect_t = self.zomby_frame_scale.get_rect()
                zomby_frame_scale_rect_t.topleft = [ZX[i] + 90 + vector_end[0], ZY[i] + vector_end[1]]
                self.zomby_frame_scale_rect.append(zomby_frame_scale_rect_t)
                sc.blit(self.zomby_frame_scale, [ZX[i] + 90 + vector_end[0], ZY[i] + vector_end[1]])

                if debug_mod == True:
                    pygame.draw.rect(sc, [250, 0, 0], self.zomby_frame_scale_rect[i], 2)
            if self.dead_count > 0:
                for j in range(self.dead_count):
                        sc.blit(self.zom_dead, [self.dead_x[j] + 90 + vector_end[0], self.dead_y[j] + vector_end[1]])

            return self.zomby_frame_scale_rect

        def zomby_triger(self, rplX, rplY, ZX, ZY, dead_v, HP):
            if player_dead == False:
                for i in range(zombi_colich):
                    if pygame.Rect.colliderect(player_triger_rect, self.zomby_frame_scale_rect[i]):
                        self.ZX_p[i] = ZX[i]
                        if (ZX[i] - rplX) > 5:
                            ZX[i] -= 5
                            self.timer[i] += 1
                            if self.frame_num[i] < 16 or self.frame_num[i] > 18:
                                self.frame_num[i] = 16
                            elif self.frame_num[i] < 19 and self.timer[i] >= 6:
                                self.frame_num[i] += 1
                                self.timer[i] = 0
                            self.gorizont = True

                        elif (ZX[i] - rplX) < -5:
                            ZX[i] += 5
                            self.timer[i] += 1
                            if self.frame_num[i] < 12 or self.frame_num[i] >= 15:
                                self.frame_num[i] = 12
                            elif self.frame_num[i] < 15 and self.timer[i] >= 6:
                                self.frame_num[i] += 1
                                self.timer[i] = 0
                            self.gorizont = True

                        if (ZY[i] - rplY) > 5:
                            ZY[i] -= 5
                            if self.gorizont == False:
                                self.timer[i] += 1
                            if self.frame_num[i] < 8 or self.frame_num[i] >= 11 and self.gorizont == False:
                                self.frame_num[i] = 8
                            elif self.frame_num[i] < 11 and self.timer[i] >= 6 and self.gorizont == False:
                                self.frame_num[i] += 1
                                self.timer[i] = 0

                        elif (ZY[i] - rplY) < -5:
                            ZY[i] += 5
                            if self.gorizont == False:
                                self.timer[i] += 1
                            if self.frame_num[i] < 4 or self.frame_num[i] >= 7 and self.gorizont == False:
                                self.frame_num[i] = 4
                            elif self.frame_num[i] < 7 and self.timer[i] >= 6 and self.gorizont == False:
                                self.frame_num[i] += 1
                                self.timer[i] = 0

                        #     тут я буду пытаться сделать анимку зомбу при помощи сравнения старых координат и новых, это можно записать
                        #     в переменную типо изм или неизм и при помощи этого менять спрайт зомбу
                        #     ! решил реализовать через то в какой части экрана зомби и от токо качается ли тригер игрока, от этого и задаем спрайт
                        #     пока решал вопрос с анимками смог починить колебания зомби, теперь остались только проблемы колизии
                    else:
                        self.frame_num[i] = 0
                        self.timer[i] = 0
                    if debug_mod:
                        print(ZX, self.ZX_p, self.frame_num, self.timer, self.gorizont) #отладка



            else:
                if dead_v < 15:
                    for i in range(zombi_colich):
                        if pygame.Rect.colliderect(player_triger_rect, self.zomby_frame_scale_rect[i]):
                            if ZX[i] > rplX:
                                ZX[i] -= 5
                            elif ZX[i] < rplX:
                                ZX[i] += 5

                            if ZY[i] > rplY:
                                ZY[i] -= 5
                            elif ZY[i] < rplY:
                                ZY[i] += 5
                            dead_v += 1
            for k in range(zombi_colich):
                if pygame.Rect.colliderect(self.zomby_frame_scale_rect[k], frame_scale_rect):
                    if HP > 0:
                        HP -= 3
            self.gorizont = False
            return ZX, ZY, dead_v, HP

    class bullet:
        def __init__(self):
            self.im = pygame.image.load(r"game_spr/Bullet.png").convert_alpha()
            self.gipo, self.sin_bull, self.cos_bull, self.x, self.y = 0, [], [], 0, 0
            self.speed = 20
            self.center = [960, 540]
            self.bull_cord_x, self.bull_cord_y = [], []
            self.count = 0
            self.time = 0
            self.i1, self.i2 = -2, -1
            self.bull_rect = []

        def bullet_cord(self, x_b, y_b, buo, reload, ammo):
            if player_dead == False:
                if debug_mod == True:
                    pygame.draw.circle(sc, [0, 0, 0], [x_b, y_b], 2)
                    pygame.draw.circle(sc, [250, 0, 0], [x_b1,y_b1], 2)

                if buo != 0:
                    if reload == 0 and ammo > 0:

                        self.center = [x_b1, y_b1]

                        x_b = x_b - self.center[0]
                        y_b = y_b - self.center[1]
                        self.gipo = math.sqrt(x_b ** 2 + y_b ** 2)
                        sin_bull_t = y_b / self.gipo
                        cos_bull_t = x_b / self.gipo
                        self.sin_bull.append(sin_bull_t)
                        self.cos_bull.append(cos_bull_t)
                        self.count += 1
                        self.i1, self.i2 = self.i1 + 2, self.i2 + 2
                        reload = 100
                        ammo -= 1
                    buo = 0

            return buo, reload, ammo
        def bullet_draw(self, zomby_frame_scale_rect, score, boss_HP):
            zom_dead = -1
            for i in range(self.count):
                self.bull_cord_x.append(960)
                self.bull_cord_y.append(540)
                if debug_mod == True:
                    pygame.draw.circle(sc, [0,0,0], [self.center[0], self.center[1]], 2)
                if self.cos_bull[i] != 0 and self.sin_bull[i] != 0:
                    self.bull_cord_x[i] += self.speed * self.cos_bull[i] - vector[0]
                    self.bull_cord_y[i] += self.speed * self.sin_bull[i] - vector[1]
                elif self.cos_bull != 0 and self.sin_bull == 0:
                    self.bull_cord_y[i] += self.speed * self.sin_bull[i] - vector[1]
                elif self.cos_bull == 0 and self.sin_bull != 0:
                    self.bull_cord_x[i] += self.speed * self.cos_bull[i] - vector[0]

                self.bull_rect = self.im.get_rect()
                self.bull_rect.topleft = [self.bull_cord_x[i]-3, self.bull_cord_y[i]-3]

                pygame.draw.rect(sc, [255, 255, 0], self.bull_rect)
                for j in range(zombi_colich):
                    if pygame.Rect.colliderect(zomby_frame_scale_rect[j], self.bull_rect):
                        zom_dead = j
                        score += 1
                        self.bull_cord_x[self.count-1] = -1000000
                for k in range(n):
                    if pygame.Rect.colliderect(home_rect[k], self.bull_rect):
                        self.bull_cord_x[self.count - 1] = -1000000
                if pygame.Rect.colliderect(boss_rect, self.bull_rect):
                    self.bull_cord_x[self.count - 1] = -1000000
                    if boss_HP > 0:
                        boss_HP -= 25
            return zomby_frame_scale_rect, zom_dead, score, boss_HP

    class boss:
        def __init__(self):
            self.X, self.Y = 5670, 3030
            #self.X, self.Y = 100, 200
            self.im = pygame.image.load(r"game_spr/Bullet.png").convert_alpha()
            self.gipo, self.sin_bull, self.cos_bull, self.x, self.y = 0, [], [], 0, 0
            self.reload = 0
            self.speed = 20
            self.center = [rplX, rplY]
            self.bull_cord_x, self.bull_cord_y = [], []
            self.count = 0
            self.time = 0
            self.i1, self.i2 = -2, -1
            self.bull_rect = []
            self.boss_sprite = []
            self.boss_rect = []
            self.boss_frame = []
            self.boss_tile = pygame.image.load(r"game_spr/boss.png").convert_alpha()
            self.boss_dead = pygame.image.load(r"game_spr/boss_dead.png").convert_alpha()
            self.timer = 0
            self.boss_frame_num = 0
            self.gorizont = False

        def boss_draw(self):
            self.boss_sprite = player_anim(4, 7, 28, self.boss_tile)
            self.boss_frame = pygame.transform.scale(self.boss_sprite[self.boss_frame_num], (96, 96))
            self.boss_rect = self.boss_frame.get_rect()
            self.boss_rect.topleft = [self.X + 90 + vector_end[0], self.Y + 90 + vector_end[1]]
            if boss_HP > 0:
                sc.blit(self.boss_frame, [self.X + 90 + vector_end[0], self.Y + 90 + vector_end[1]])
            if boss_HP == 0:
                self.boss_dead = pygame.transform.scale(self.boss_dead, (86, 86))
                sc.blit(self.boss_dead, [self.X + 90 + vector_end[0], self.Y + 90 + vector_end[1]])
            pygame.draw.rect(sc, [250, 0, 0], [self.X + 90 + vector_end[0], self.Y + 80 + vector_end[1], boss_HP, 10])

        def boss_move(self, boss_active):
            if pygame.Rect.colliderect(self.boss_rect, player_triger_rect):
                boss_active = True
            if boss_active and boss_HP > 0:
                self.gorizont = False

                if (self.X - 200 - rplX) > 450:
                    self.X -= 5
                    self.timer += 1
                    if self.boss_frame_num < 16 or self.boss_frame_num >= 18:
                        self.boss_frame_num = 16
                    elif self.boss_frame_num < 19 and self.timer >= 6:
                        self.boss_frame_num += 1
                        self.timer = 0
                    self.gorizont = True

                elif (self.X - 450 - rplX) < -200:
                    self.X += 5
                    self.timer += 1
                    if self.boss_frame_num < 19 or self.boss_frame_num >= 21:
                        self.boss_frame_num = 19
                    elif self.boss_frame_num < 21 and self.timer >= 6:
                        self.boss_frame_num += 1
                        self.timer = 0
                    self.gorizont = True

                if (self.Y + 90 - rplY) > 90:
                    self.Y -= 5
                    if self.gorizont == False:
                        self.timer += 1
                    if self.boss_frame_num < 22 or self.boss_frame_num >= 24 and self.gorizont == False:
                        self.boss_frame_num = 22
                    elif self.boss_frame_num < 24 and self.timer >= 6 and self.gorizont == False:
                        self.boss_frame_num += 1
                        self.timer = 0

                elif (self.Y + 90 - rplY) < -90:
                    self.Y += 5
                    if self.gorizont == False:
                        self.timer += 1
                    if self.boss_frame_num < 25 or self.boss_frame_num >= 27 and self.gorizont == False:
                        self.boss_frame_num = 25
                    elif self.boss_frame_num < 27 and self.timer >= 6 and self.gorizont == False:
                        self.boss_frame_num += 1
                        self.timer = 0

            return boss_active, self.boss_rect
        def boss_shot(self, HP):
            self.center = [self.X + 145 + vector_end[0], self.Y + 145 + vector_end[1]]
            self.x_b = (rplX + vector_end[0] + 140) - self.center[0]
            self.y_b = (rplY + vector_end[1] + 45) - self.center[1]
            if boss_active and boss_HP > 0:
                if self.reload == 0:

                    self.gipo = math.sqrt(self.x_b ** 2 + self.y_b ** 2)
                    sin_bull_t = self.y_b / self.gipo
                    cos_bull_t = self.x_b / self.gipo
                    self.sin_bull.append(sin_bull_t)
                    self.cos_bull.append(cos_bull_t)
                    self.count += 1
                    self.i1, self.i2 = self.i1 + 2, self.i2 + 2
                    self.bull_cord_x.append(self.center[0])
                    self.bull_cord_y.append(self.center[1])
                    self.reload = 100
                else:
                    self.reload -= 1

                for i in range(self.count):
                    if self.cos_bull[i] != 0 and self.sin_bull[i] != 0:
                        self.bull_cord_x[i] += self.speed * self.cos_bull[i] - vector[0]
                        self.bull_cord_y[i] += self.speed * self.sin_bull[i] - vector[1]
                    elif self.cos_bull != 0 and self.sin_bull == 0:
                        self.bull_cord_y[i] += self.speed * self.sin_bull[i] - vector[1]
                    elif self.cos_bull == 0 and self.sin_bull != 0:
                        self.bull_cord_x[i] += self.speed * self.cos_bull[i] - vector[0]

                    self.bull_rect = self.im.get_rect()
                    self.bull_rect.topleft = [self.bull_cord_x[i]-3, self.bull_cord_y[i]-3]
                    pygame.draw.rect(sc, [255, 255, 0], self.bull_rect)
                    pygame.draw.rect(sc, [255, 255, 0], [self.center[0], self.center[1], 5, 5])
                    if pygame.Rect.colliderect(frame_scale_rect, self.bull_rect):
                        self.bull_cord_x[self.count - 1] = -1000000
                        HP -= 100

            return HP

    stopkey = 0
    evac = 0
    # первичный вызов класофункций #
    player1 = Player(0, 0)
    camera = cam(0, 0)
    background = pygame.image.load("game_spr/back.png").convert_alpha()

    # загрузка тайлмап #
    map_path = "map.txt"
    map_OBJ = "map_OBJ.txt"

    # чтение и расшифровка тайлмапы земли #
    def readFile(map_path):
        map_file = open(map_path, 'r')
        N, M, count = 0, 0, 0
        s = map_file.readline()
        s = s.split()
        N, M = int(s[0]), int(s[1])
        map_list = [0] * N
        for i in range(N):
            map_list[i] = [0] * M
        for i in range(N):
            s = map_file.readline()
            s = s.split()
            for j in range(M):
                map_list[i][j] = int(s[j])
                if map_list[i][j] == 3:
                    count += 1
        map_file.close()
        return N, M, map_list, count

    # чтение и расшифровка тайлмапы объектов #
    def readFile1(map_OBJ):
        map_file1 = open(map_OBJ, 'r')  # 'w' - перезаписать //// 'a' - дописать в конец
        N1, M1, coun = 0, 0, 0
        s = map_file1.readline()
        s = s.split()
        N1, M1 = int(s[0]), int(s[1])
        map_list1 = [0] * N1
        for i in range(N1):
            map_list1[i] = [0] * M1
        for i in range(N1):
            s = map_file1.readline()
            s = s.split()
            for j in range(M1):
                map_list1[i][j] = int(s[j])
                if map_list1[i][j] == 3:
                    coun += 1
        map_file1.close()
        return N1, M1, map_list1, coun

    # отрисовка земли #
    def drawGROWN(map_list):
        for i in range(N):
            for j in range(N):
                x = wh*j +vector_end[0] - 960
                y = hh*i + vector_end[1] - 540
                if map_list[i][j] == 0:
                    break
                    # sc.blit(wall, [x,y])
                elif map_list[i][j] == 1:
                    sc.blit(grass,[x,y])
                elif map_list[i][j] == 2:
                    sc.blit(road,[x,y])
                elif map_list[i][j] == 3:
                    sc.blit(road_up, [x,y])
                elif map_list[i][j] == 4:
                    sc.blit(road_down, [x,y])
                elif map_list[i][j] == 5:
                    sc.blit(road_rigth, [x,y])
                elif map_list[i][j] == 6:
                    sc.blit(road_left, [x,y])
        return()

    # отрисовка объектов на земле #
    def drawOBJ(map_list1, ZX, ZY, lolololoo, ammo_het, med_het, MX, MY, AX, AY, ras):
        bpla_rect, home_rect, car_1_v_rect, car_2_v_rect, car_3_v_rect, hamer_v_rect, hamer_g_rect, btr_rect, exit_zone_rect, \
        car_1_g_rect, car_2_g_rect, car_3_g_rect, car_4_g_rect, ammobox_rect, med_rect\
        = [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        car_1_v_len, car_2_v_len, car_3_v_len, hamer_v_len, hamer_g_len, car_1_g_len, car_2_g_len, car_3_g_len, car_4_g_len, \
        ammobox_len, med_len, n  = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        for i in range(N):
            for j in range(N):
                x = wh * j + vector_end[0] - 960
                y = hh * i + vector_end[1] - 540
                if map_list1[i][j] == 0:
                    zadsad = 0

                elif map_list1[i][j] == 1:
                    home_rect_t = home1.get_rect()
                    home_rect_t.topleft = [x, y]
                    home_rect.append(home_rect_t)
                    sc.blit(home1_int, [x, y + 292])
                    sc.blit(home1, [x, y])
                    home_1_len = len(home_rect)
                    if debug_mod == True:
                        for i in range(home_1_len):
                            pygame.draw.rect(sc, [250, 0, 0], home_rect[i], 2)

                elif map_list1[i][j] == 2:

                    home_rect_t = home2.get_rect()
                    home_rect_t.topleft = [x,y]
                    home_rect.append(home_rect_t)
                    sc.blit(home2_int, [x,y+292])
                    sc.blit(home2,[x,y])
                    n = len(home_rect)
                    if debug_mod == True:
                        for i in range(n):
                            pygame.draw.rect(sc, [250,0,0], home_rect[i], 2)

                elif map_list1[i][j] == 3:
                    home_rect_t = home4.get_rect()
                    home_rect_t.topleft = [x, y]
                    home_rect.append(home_rect_t)
                    sc.blit(home4_int, [x, y + 292])
                    sc.blit(home4, [x, y])
                    home_4_len = len(home_rect)
                    if debug_mod == True:
                        for i in range(home_4_len):
                            pygame.draw.rect(sc, [250, 0, 0], home_rect[i], 2)

                elif map_list1[i][j] == 4:
                    if lolololoo < zombi_colich:
                        ZX.append(x)
                        ZY.append(y)
                        lolololoo +=1

                elif map_list1[i][j] == 5:
                    car_1_v_t = car_1_v.get_rect()
                    car_1_v_t.topleft = [x, y]
                    car_1_v_rect.append(car_1_v_t)
                    sc.blit(car_1_v, [x, y])
                    car_1_v_len = len(car_1_v_rect)

                elif map_list1[i][j] == 6:
                    car_2_v_t = car_2_v.get_rect()
                    car_2_v_t.topleft = [x, y]
                    car_2_v_rect.append(car_2_v_t)
                    sc.blit(car_2_v, [x, y])
                    car_2_v_len = len(car_2_v_rect)

                elif map_list1[i][j] == 7:
                    car_3_v_t = car_3_v.get_rect()
                    car_3_v_t.topleft = [x, y]
                    car_3_v_rect.append(car_3_v_t)
                    sc.blit(car_3_v, [x, y])
                    car_3_v_len = len(car_3_v_rect)

                elif map_list1[i][j] == 8:
                    hamer_v_t = hamer_v.get_rect()
                    hamer_v_t.topleft = [x, y]
                    hamer_v_rect.append(hamer_v_t)
                    sc.blit(hamer_v, [x, y])
                    hamer_v_len = len(hamer_v_rect)

                elif map_list1[i][j] == 9:
                    hamer_g_t = hamer_g.get_rect()
                    hamer_g_t.topleft = [x, y]
                    hamer_g_rect.append(hamer_g_t)
                    sc.blit(hamer_g, [x, y])
                    hamer_g_len = len(hamer_g_rect)

                elif map_list1[i][j] == 10:
                    btr_rect = btr.get_rect()
                    btr_rect.topleft = [x, y]
                    sc.blit(btr, [x, y])

                elif map_list1[i][j] == 11:
                    car_1_g_t = car_1_g.get_rect()
                    car_1_g_t.topleft = [x, y]
                    car_1_g_rect.append(car_1_g_t)
                    sc.blit(car_1_g, [x, y])
                    car_1_g_len = len(car_1_g_rect)

                elif map_list1[i][j] == 12:
                    car_2_g_t = car_2_g.get_rect()
                    car_2_g_t.topleft = [x, y]
                    car_2_g_rect.append(car_2_g_t)
                    sc.blit(car_2_g, [x, y])
                    car_2_g_len = len(car_2_g_rect)

                elif map_list1[i][j] == 13:
                    car_3_g_t = car_3_g.get_rect()
                    car_3_g_t.topleft = [x, y]
                    car_3_g_rect.append(car_3_g_t)
                    sc.blit(car_3_g, [x, y])
                    car_3_g_len = len(car_3_g_rect)

                elif map_list1[i][j] == 14:
                    car_4_g_t = car_4_g.get_rect()
                    car_4_g_t.topleft = [x, y]
                    car_4_g_rect.append(car_4_g_t)
                    sc.blit(car_4_g, [x, y])
                    car_4_g_len = len(car_4_g_rect)

                elif map_list1[i][j] == 15:
                    exit_zone_rect = btr.get_rect()
                    exit_zone_rect.topleft = [x, y]
                    sc.blit(exit_zone, [x, y])
                elif map_list1[i][j] == 16:
                    if ammo_het < ras:
                        AX.append(x)
                        AY.append(y)
                        ammobox_len = len(ammobox_rect)
                        ammo_het += 1

                elif map_list1[i][j] == 17:
                    if med_het < ras:
                        MX.append(x)
                        MY.append(y)
                        med_len = len(med_rect)
                        med_het += 1

        return bpla_rect, vector, n, ZX, ZY, home_1_len, home_rect, car_1_v_rect, car_1_v_len, lolololoo, car_2_v_len, car_2_v_rect,\
               car_3_v_rect, car_3_v_len, hamer_v_rect, hamer_v_len, hamer_g_rect, hamer_g_len, btr_rect, car_1_g_len, car_1_g_rect, \
               car_2_g_len, car_2_g_rect, car_3_g_len, car_3_g_rect, car_4_g_len, car_4_g_rect, exit_zone_rect, ammobox_rect, ammobox_len, \
               med_rect, med_len, ammo_het, med_het, MX, MY, AX, AY

    def collide(vector, stopkey):
        if kpressed[pygame.K_w]:
            stopkey = "w"
        if kpressed[pygame.K_s]:
            stopkey = "s"
        if kpressed[pygame.K_d]:
            stopkey = "d"
        if kpressed[pygame.K_a]:
            stopkey = "a"
        if kpressed[pygame.K_w] and kpressed[pygame.K_d]:
            stopkey = "wd"
        if kpressed[pygame.K_w] and kpressed[pygame.K_a]:
            stopkey = "wa"
        if kpressed[pygame.K_s] and kpressed[pygame.K_d]:
            stopkey = "sd"
        if kpressed[pygame.K_s] and kpressed[pygame.K_a]:
            stopkey = "sa"
        # обработка коллизии # раньше за место 0 было 8, вызывало баги
        if vector[0] == 6 and vector[1] == 0:
            vector[0] = -0
        if vector[0] == 0 and vector[1] == 6:
            vector[1] = -0
        if vector[0] == -6 and vector[1] == 0:
            vector[0] = 0
        if vector[0] == 0 and vector[1] == -6:
            vector[1] = 0
        if vector[0] == 6 and vector[1] == 6:
            vector[0] = -0
            vector[1] = -0
        if vector[0] == -6 and vector[1] == -6:
            vector[0] = 0
            vector[1] = 0
        if vector[0] == -6 and vector[1] == 6:
            vector[0] = 0
            vector[1] = -0
        if vector[0] == 6 and vector[1] == -6:
            vector[0] = -0
            vector[1] = 0

        if vector[0] == 0 and vector[1] == 0:

            vector[0] = -lastVEC[0]
            vector[1] = -lastVEC[1]
        return vector, stopkey

    def ammomed_draw(MX, MY, AX, AY, vector_end):
        med_rect = []
        for g in range(ras):
            sc.blit(med, [MX[g] + 90 + vector_end[0], MY[g] + vector_end[1]])
            med_rect_t = med.get_rect()
            med_rect_t.topleft = [MX[g] + 90 + vector_end[0], MY[g] + vector_end[1]]
            med_rect.append(med_rect_t)

            sc.blit(close_ammobox, [AX[g] + 90 + vector_end[0], AY[g] + vector_end[1]])
            ammobox_rect_t = close_ammobox.get_rect()
            ammobox_rect_t.topleft = [AX[g] + 90 + vector_end[0], AY[g] + vector_end[1]]
            ammobox_rect.append(ammobox_rect_t)

        return MX, MY, AX, AY, med_rect

    # первичная отрисовка и вызовы функций для их нормального функционирования #
    zomby_frame_scale_rect = []
    buo = 0
    frame = player_anim(w1, h1, k, sprite)
    player(cout2)
    frame_scale_rect, player_triger_rect = player(cout2)
    run = True
    vector_end = [0, 0]
    N, M, map_list, count = readFile(map_path)
    N1, M1, map_list1, coun = readFile1(map_OBJ)

    bpla_rect, vector, n, ZX, ZY, home_1_len, home_rect, car_1_v_rect, car_1_v_len, lolololoo, car_2_v_len, car_2_v_rect, \
    car_3_v_rect, car_3_v_len, hamer_v_rect, hamer_v_len, hamer_g_rect, hamer_g_len, btr_rect, car_1_g_len, car_1_g_rect, \
    car_2_g_len, car_2_g_rect, car_3_g_len, car_3_g_rect, car_4_g_len, car_4_g_rect, exit_zone_rect, ammobox_rect, ammobox_len, \
    med_rect, med_len, ammo_het, med_het, MX, MY, AX, AY = drawOBJ(map_list1, ZX, ZY, lolololoo, ammo_het, med_het, MX, MY, AX, AY, ras)
    frame = player_anim(w1, h1, k, sprite)
    MX, MY, AX, AY, med_rect = ammomed_draw(MX, MY, AX, AY, vector_end)
    reload_frame = player_anim(5, 4,25, reload_spine)
    pygame.key.set_repeat(100, 80)
    sc.blit(frame[stay], [plX, plY])
    clock = pygame.time.Clock()
    fps = 60
    lastVEC = [0,0]
    x_b1 = 0
    y_b1= 0
    n_t_t, n_t = 0, 0
    alpha = 0
    zombi = zomby()
    bullet = bullet()
    boss = boss()
    an_shet = 0
    zomby_pos_tp = 0
    lasttime = 0
    while run:
        if rplY >672 and rplY < 700 and zomby_pos_tp == 0:
            for i in range(zombi_colich):
                ZX[i] = 1806 + random.randint(-30, 30)
                ZY[i] = 1680 + random.randint(-30, 30)
                zom_dead = -1
            zomby_pos_tp += 1

        elif rplX > 1460 and rplX < 1480 and rplY > 1400 and zomby_pos_tp == 1:
            for i in range(zombi_colich):
                ZX[i] = 132 + random.randint(-30, 30)
                ZY[i] = 1716 + random.randint(-30, 30)
                zom_dead = -1
            zomby_pos_tp += 1

        elif rplY >2020 and rplY < 2030 and zomby_pos_tp == 2:
            for i in range(zombi_colich):
                ZX[i] = 42 + random.randint(-30, 30)
                ZY[i] = 3050 + random.randint(-30, 30)
                zom_dead = -1
            zomby_pos_tp += 1

        elif rplX >500 and rplX < 510 and rplY > 2700 and zomby_pos_tp == 3:
            for i in range(zombi_colich):
                ZX[i] = 1782 + random.randint(-30, 30)
                ZY[i] = 3036 + random.randint(-30, 30)
                zom_dead = -1
            zomby_pos_tp += 1

        elif rplY >3350 and rplY < 3360 and zomby_pos_tp == 4:
            for i in range(zombi_colich):
                ZX[i] = 1806 + random.randint(-30, 30)
                ZY[i] = 4234 + random.randint(-30, 30)
                zom_dead = -1
            zomby_pos_tp += 1

        elif rplX >2280 and rplX < 2290 and zomby_pos_tp == 5:
            for i in range(zombi_colich):
                ZX[i] = 2772 + random.randint(-30, 30)
                ZY[i] = 2974 + random.randint(-30, 30)
                zom_dead = -1
            zomby_pos_tp += 1

        elif rplX >2916 and rplX < 2926 and zomby_pos_tp == 6:
            for i in range(zombi_colich):
                ZX[i] = 4410 + random.randint(-30, 30)
                ZY[i] = 3022 + random.randint(-30, 30)
                zom_dead = -1
            zomby_pos_tp += 1
        elif rplX > 4540 and rplX < 4550 and zomby_pos_tp == 7:
            for i in range(zombi_colich):
                ZX[i] = 5490 + random.randint(-30, 30)
                ZY[i] = 2982 + random.randint(-30, 30)
                zom_dead = -1
            zomby_pos_tp += 1


        # предыдущие векторы, чтобы вытаскивать персонажа из коллизии #
        if lastVEC[0] >= 6:
            lastVEC[0] = lastVEC[0] - 6
        if lastVEC[1] >= 6:
            lastVEC[1] = lastVEC[1] - 6
        if lastVEC[1] <= -6:
            lastVEC[1] = lastVEC[1] + 6
        if lastVEC[0] <= -6:
            lastVEC[0] = lastVEC[0] + 6
        # обнуление вектора для правильного перемещения персонажа #
        vector = [0,0]

        # непонятная отрисовка #
        bpla_rect, vector, n, ZX, ZY, home_1_len, home_rect, car_1_v_rect, car_1_v_len, lolololoo, car_2_v_len, car_2_v_rect, \
        car_3_v_rect, car_3_v_len, hamer_v_rect, hamer_v_len, hamer_g_rect, hamer_g_len, btr_rect, car_1_g_len, car_1_g_rect, \
        car_2_g_len, car_2_g_rect, car_3_g_len, car_3_g_rect, car_4_g_len, car_4_g_rect, exit_zone_rect, ammobox_rect, ammobox_len, \
        med_rect, med_len, ammo_het, med_het, MX, MY, AX, AY = drawOBJ(map_list1, ZX, ZY, lolololoo, ammo_het, med_het, MX, MY, AX, AY, ras)
        zombi.zomby_draw(ZX, ZY, zomby_frame_scale_rect)
        ZX, ZY, dead_v, HP = zombi.zomby_triger(rplX, rplY, ZX, ZY, dead_v, HP)
        N, M, map_list, count = readFile(map_path)
        MX, MY, AX, AY, med_rect = ammomed_draw(MX, MY, AX, AY, vector_end)
        boss.boss_draw()
        boss_active, boss_rect = boss.boss_move(boss_active)

        # рассчет движение камеры #
        kpressed = pygame.key.get_pressed()
        if player_dead == False:
            if stopkey != "wa" and kpressed[pygame.K_w] and kpressed[pygame.K_a]:
                stopkey = 0
                vector[1] -= 6
                lastVEC[1] -= 6
                vector[0] -= 6
                lastVEC[0] -= 6
                an_shet += 1
                if an_shet > 6:
                    if cout2 > 14 and cout2 + 1 < 20:
                        cout2 = cout2 + 1
                        an_shet = 0
                    elif cout2 < 15 or cout2 + 1 > 19:
                        cout2 = 16
                        an_shet = 0
                stay = 3

            elif stopkey != "wd" and kpressed[pygame.K_w] and kpressed[pygame.K_d]:
                stopkey = 0
                vector[0] += 6
                lastVEC[0] += 6
                vector[1] -= 6
                lastVEC[1] -= 6
                an_shet += 1
                if an_shet > 6:
                    if cout2 > 11 and cout2 + 1 < 16:
                        cout2 = cout2 + 1
                        an_shet = 0
                    elif cout2 < 12 or cout2 + 1 > 15:
                        cout2 = 12
                        an_shet = 0
                stay = 2

            elif stopkey != "w" and kpressed[pygame.K_w] and not(kpressed[pygame.K_a]) and not(kpressed[pygame.K_d]):
                stopkey = 0
                vector[1] -= 6
                lastVEC[1] -= 6
                an_shet += 1
                if an_shet > 6:
                    if cout2 > 7 and cout2 + 1 < 12:
                        cout2 = cout2 + 1
                        an_shet =0
                    elif cout2 < 8 or cout2 + 1 > 11:
                        cout2 = 8
                        an_shet = 0
                stay = 1

            elif stopkey != "sa" and kpressed[pygame.K_s] and kpressed[pygame.K_a]:
                stopkey = 0
                vector[0] -= 6
                lastVEC[0] -= 6
                vector[1] += 6
                lastVEC[1] += 6
                an_shet += 1
                if an_shet > 6:
                    if cout2 > 14 and cout2 + 1 < 20:
                        cout2 = cout2 + 1
                        an_shet = 0
                    elif cout2 < 15 or cout2 + 1 > 19:
                        cout2 = 16
                        an_shet = 0
                stay = 3

            elif stopkey != "sd" and kpressed[pygame.K_s] and kpressed[pygame.K_d]:
                stopkey = 0
                vector[0] += 6
                lastVEC[0] += 6
                vector[1] += 6
                lastVEC[1] += 6
                an_shet += 1
                if an_shet > 6:
                    if cout2 > 11 and cout2 + 1 < 16:
                        cout2 = cout2 + 1
                        an_shet = 0
                    elif cout2 < 12 or cout2 + 1 > 15:
                        cout2 = 12
                        an_shet = 0
                stay = 2

            elif stopkey != "s" and kpressed[pygame.K_s] and not(kpressed[pygame.K_a]) and not(kpressed[pygame.K_d]):
                stopkey = 0
                vector[1] += 6
                lastVEC[1] += 6
                an_shet += 1
                if an_shet > 6:
                    if cout2 > 3 and cout2 + 1 < 8:
                        cout2 = cout2 + 1
                        an_shet = 0
                    elif cout2 < 3 or cout2 + 1 > 6:
                        cout2 = 4
                        an_shet = 0
                stay = 0

            if stopkey != "a" and kpressed[pygame.K_a] and not(kpressed[pygame.K_w]) and not(kpressed[pygame.K_s]):
                stopkey = 0
                vector[0] -= 6
                lastVEC[0] -= 6
                an_shet += 1
                if an_shet > 6:
                    if cout2 > 14 and cout2 + 1 < 20:
                        cout2 = cout2 + 1
                        an_shet = 0
                    elif cout2 < 15 or cout2 + 1 > 19:
                        cout2 = 16
                        an_shet = 0
                stay = 3

            elif stopkey != "d" and kpressed[pygame.K_d] and not(kpressed[pygame.K_w]) and not(kpressed[pygame.K_s]):
                stopkey = 0
                vector[0] += 6
                lastVEC[0] += 6
                an_shet += 1
                if an_shet > 6:
                    if cout2 > 11 and cout2 + 1 < 16:
                        cout2 = cout2 + 1
                        an_shet = 0
                    elif cout2 < 12 or cout2 + 1 > 15:
                        cout2 = 12
                        an_shet = 0
                stay = 2

            else:
                stay = stay
        if player_dead == True:
            cout2 = 20
            stay = cout2
            lasttime += 1
            if cout2 < 21 and lasttime > 7:
                cout2 += 1
                stay = cout2

        # коллизия #
        for i in range(n):
            # pygame.Rect.colliderect(bpla_rect[i], frame_scale_rect) or
            if pygame.Rect.colliderect(home_rect[i], frame_scale_rect):
                # обработка коллизии #
                vector, stopkey = collide(vector, stopkey)
        for l in range(car_1_v_len):
            if pygame.Rect.colliderect(car_1_v_rect[l], frame_scale_rect):
                vector, stopkey = collide(vector, stopkey)
        for ll in range(car_2_v_len):
            if pygame.Rect.colliderect(car_2_v_rect[ll], frame_scale_rect):
                vector, stopkey = collide(vector, stopkey)
        for lll in range(car_3_v_len):
            if pygame.Rect.colliderect(car_3_v_rect[lll], frame_scale_rect):
                vector, stopkey = collide(vector, stopkey)
        for llll in range(hamer_v_len):
            if pygame.Rect.colliderect(hamer_v_rect[llll], frame_scale_rect):
                vector, stopkey = collide(vector, stopkey)
        for lllll in range(hamer_g_len):
            if pygame.Rect.colliderect(hamer_g_rect[lllll], frame_scale_rect):
                vector, stopkey = collide(vector, stopkey)
        if pygame.Rect.colliderect(btr_rect, frame_scale_rect):
            vector, stopkey = collide(vector, stopkey)
        for o in range(car_1_g_len):
            if pygame.Rect.colliderect(car_1_g_rect[o], frame_scale_rect):
                vector, stopkey = collide(vector, stopkey)
        for oo in range(car_2_g_len):
            if pygame.Rect.colliderect(car_2_g_rect[oo], frame_scale_rect):
                vector, stopkey = collide(vector, stopkey)
        for ooo in range(car_3_g_len):
            if pygame.Rect.colliderect(car_3_g_rect[ooo], frame_scale_rect):
                vector, stopkey = collide(vector, stopkey)
        for oooo in range(car_4_g_len):
            if pygame.Rect.colliderect(car_4_g_rect[oooo], frame_scale_rect):
                vector, stopkey = collide(vector, stopkey)
        for ooooo in range(ammobox_len):
            if pygame.Rect.colliderect(ammobox_rect[ooooo], frame_scale_rect):
                ammo += 12
        for oooooo in range(ras):
            if pygame.Rect.colliderect(med_rect[oooooo], frame_scale_rect):
                MX[oooooo] = -10000
                HP += 75
                if HP > 300:
                    HP = 300
            if pygame.Rect.colliderect(ammobox_rect[oooooo], frame_scale_rect):
                AX[oooooo] = -10000
                ammo += 12
        ##  Если игрок ходил, движение камеры
        if vector != [0, 0]:
            player1.move(vector)
            camera.move(vector)
        vector_end[0] -= vector[0]
        vector_end[1] -= vector[1]
        sc.fill((255, 255, 255))
        x_b -= vector[0]
        x_b1 -= vector[0]
        y_b -= vector[1]
        y_b1 -= vector[1]
        rplX = 810 - vector_end[0]
        rplY = 480 - vector_end[1]
        objects = [object(0, 0, 10000, 10000)]

        ##  отрисовка других объектов
        for obj in objects:
            ##  Если объект на экране, отрисовать его
            if obj.rect.colliderect(camera.rect):
                buo, zomby_frame_scale_rect, zom_dead, reload, dead_v, score, ammo, ammo_het, med_het, MX, MY, AX, \
                AY, boss_HP, HP = obj.draw(ZX, ZY, x_b, y_b, buo, zomby_frame_scale_rect, reload, dead_v, lolololoo, score, ammo, ammo_het, med_het, MX, MY, AX, AY, boss_HP, HP)
        # отрисовка игрока #
        player1.draw()
        if player_dead == False and ammo > 0:
            if reload > 0:
                if n_t_t == 5:
                    n_t += 1
                    n_t_t = 0
                if n_t == 20:
                    n_t = 0
                    n_t_t = 0
                sc.blit(reload_sprite, (930,440))
                sc.blit(reload_frame[n_t],(920,435))
                reload -= 1
                n_t_t += 1
        if player_dead ==True:
            dead_tabl.set_alpha(alpha)
            dead_tabl2.set_alpha(alpha)
            if a_tic == 0:
                alpha += 5
            pygame.time.delay(30)
            if alpha > 254:
                a_tic = 1
            if a_tic == 1:
                alpha -= 5
                if alpha < 15:
                    a_tic = 0
            sc.blit(dead_tabl, [690,320])
            sc.blit(dead_tabl2, [750, 660])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                buo += 1

                (x_b, y_b) = pygame.mouse.get_pos()
                y_b1, x_b1 = 540, 960

        if pygame.Rect.colliderect(exit_zone_rect, frame_scale_rect) and boss_HP == 0:
            sc.blit(atent_press, [780,360])
            kpressed = pygame.key.get_pressed()
            if kpressed[pygame.K_SPACE]:
                evacuated.evac()
        ammo_text = my_font.render("ammo " + str(ammo), True, [0,0,0])
        HP_text = my_font.render("HP " + str(HP), True, [0,0,0])
        pygame.draw.rect(sc, [250, 0, 0], [40, 40, HP, 40])
        pygame.draw.rect(sc, [0, 0, 0], [40, 40, 300, 40], 3)
        sc.blit(ammo_text, [1750, 1020])
        sc.blit(HP_text, [140, 40])
        sbros_last_vec += 1
        if sbros_last_vec >15:
            lastVEC[0] = 0
            lastVEC[1] = 0
            sbros_last_vec = 0
        #pygame.draw.rect(sc, [250, 0, 0], player_triger_rect, 2)
        if HP <= 0:
            player_dead = True
        print(rplX, rplY)
        # обновление экрана #
        clock.tick(fps)
        pygame.display.update()