import pygame
import math
import time
import random
import neuro

import classes


pygame.font.init()

pygame.init()


speed = 2
speed_obstacle = 1
size = 800

pl = classes.player(size//2, size*3//4)

screen = pygame.display.set_mode((size, size))

fnt = pygame.font.SysFont("ComicSans", 30)

txt = fnt.render("hello", True, (0, 0, 0))



running = True
key = None
obs = []

pygame.display.flip()
while running:
    outs = {}
    if random.randint(0, 3) == 0:
        obs.append  (
                        classes.obstacle(
                                speed_y= 1,
                                x= random.randint(1, size-1),
                                y= 1
                                )
                    )


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                print("up")
                pl.speed_y = -speed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("down")
                pl.speed_y = speed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("right")
                pl.speed_x = speed
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("left")
                pl.speed_x = -speed
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                b = True
                while b:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                b = False


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                pl.speed_y = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_d:
                pl.speed_x = 0
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    pl.move()

    color_e = (255, 0, 0)
    color_w = (255, 0, 0)
    color_n = (255, 0, 0)
    color_s = (255, 0, 0)
    color_ne = (255, 0, 0)
    color_nw = (255, 0, 0)
    color_se = (255, 0, 0)
    color_sw = (255, 0, 0)



    for i in obs:
        temp = pl.look(i)
        if temp:
            print(temp[0])
            if temp[0] not in outs or temp[1] < outs[temp[0]]:
                outs[temp[0]] = temp[1]
            if temp[0] == "N":
                color_n = (0, 0, 255)
            if temp[0] == "S":
                color_s = (0, 0, 255)
            if temp[0] == "W":
                color_w = (0, 0, 255)
            if temp[0] == "E":
                color_e = (0, 0, 255)
            if temp[0] == "NE":
                color_ne = (0, 0, 255)
            if temp[0] == "SW":
                color_sw = (0, 0, 255)
            if temp[0] == "NW":
                color_nw = (0, 0, 255)
            if temp[0] == "SE":
                color_se = (0, 0, 255)
    text = ""
    cnt = -1
    for i in outs:
        cnt += 1
        txt = fnt.render(str(i) + ": " + str(outs[i]), True, (0, 0, 0))
        screen.blit(txt, (0, cnt*30))
        
    pygame.draw.line(screen, color_e, (pl.x + pl.radius, pl.y), (size, pl.y))
    pygame.draw.line(screen, color_w, (pl.x - pl.radius, pl.y), (0, pl.y))
    pygame.draw.line(screen, color_n, (pl.x, pl.y - pl.radius), (pl.x, 0))
    pygame.draw.line(screen, color_s, (pl.x, pl.y + pl.radius), (pl.x, size))
    pygame.draw.line(screen, color_sw, (pl.x-int(math.sqrt(2)*pl.radius), pl.y+int(math.sqrt(2)*pl.radius)), (0, pl.y + pl.x))
    pygame.draw.line(screen, color_se, (pl.x+int(math.sqrt(2)*pl.radius), pl.y+int(math.sqrt(2)*pl.radius)), (size, pl.y + size - pl.x))
    pygame.draw.line(screen, color_ne, (pl.x+int(math.sqrt(2)*pl.radius), pl.y-int(math.sqrt(2)*pl.radius)), (size, pl.y - size + pl.x))
    pygame.draw.line(screen, color_nw, (pl.x-int(math.sqrt(2)*pl.radius), pl.y-int(math.sqrt(2)*pl.radius)), (0, pl.y - pl.x))


    pygame.draw.circle(
                    screen,
                    (0, 0, 0),
                    (pl.x, pl.y),
                    pl.radius
                    )

    pygame.draw.circle(
                    screen,
                    (255, 255, 255),
                    (pl.x, pl.y),
                    pl.radius-3
                    )
    
    for i in obs:
        i.speed_y = 1
        if i.move():
            obs.remove(i)
        
        pygame.draw.circle(
                    screen,
                    (0, 0, 0),
                    (i.x, i.y),
                    i.radius
                    )
        if pl.check_collision(i):
            print("end")
            b = True
            while b:
                for _ in pygame.event.get():
                    if _.type == pygame.KEYDOWN or _.type == pygame.MOUSEBUTTONDOWN or _.type == pygame.QUIT:
                        b = False
                        running = False
    pygame.display.flip()
    time.sleep(0.01)
