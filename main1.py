import pygame
import math
import time
import random
import neuro
import pickle
import classes
import traceback
import nullify_memory
import copy


pygame.font.init()

pygame.init()


speed = 2
speed_obstacle = 1
size = 800

screen = pygame.display.set_mode((size, size))



running = True
key = None
obs = []
gen_am = 100
pygame.display.flip()
try:
    with open("memory.txt", "rb") as f:
        best = pickle.load(f)
except FileNotFoundError:
    nullify_memory.fun()
    with open("memory.txt", "rb") as f:
        best = pickle.load(f)
except EOFError:
    nullify_memory.fun()
    with open("memory.txt", "rb") as f:
        best = pickle.load(f)

generation_number = 0
number_of_living = 5
draw_apples = True
with open("settings", "rb") as f:
    delay_time, difficulty, draw_everyone, generation_number, gen_am = pickle.load(f)

rnu = True
try:
    while rnu:
        generation_number += 1
        best = [*best]
        players = []
        for i in range(number_of_living):
            players.append(classes.smartPlayer())
            players[-1].nn = copy.deepcopy(best[i])
        for i in range(number_of_living, gen_am):    
            players.append(classes.smartPlayer())
            players[-1].nn = copy.deepcopy(random.choice(best))
            players[-1].nn.mutate()
            players[-1].nn.mutate()
            players[-1].nn.mutate()
            players[-1].nn.mutate()
            players[-1].nn.mutate()
            players[-1].nn.mutate()
            players[-1].apple.spawn(100)
            print(players[-1], type(players[-1]))
        
        running = True
        scoreboard = {}
        obs = []
        for i in range(number_of_living, gen_am):
            rannum = random.randint(0, number_of_living-1)
        print("generation_nummer", generation_number)
        framecount = 0
        alive = True
        main_player_num = 0
        obs.append  (
                        classes.obstacle(
                                speed_y= 1,
                                x= size/2,
                                y= 1
                                )
                    )
        while running:
            framecount += 2
            if random.randint(0, difficulty) == 0:
                obs.append  (
                                classes.obstacle(
                                        speed_y= 1,
                                        x= random.randint(1, size-1),
                                        y= 1
                                        )
                            )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    rnu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        b = True
                        while b:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        b = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    for i in range(len(players)):
                                        if (event.pos[0] - players[i].x)**2 + (event.pos[1] - players[i].y)**2 <= players[i].radius**2:
                                            if event.button == pygame.BUTTON_LEFT:
                                                players[i].score += players[i].apple.price*20
                                                print("gotcha")
                                            elif event.button == pygame.BUTTON_RIGHT:
                                                print("new favourite")
                                                main_player_num = i
                                                alive = True
                                            elif event.button == pygame.BUTTON_MIDDLE:
                                                print("die")
                                                players[i].score = -players[i].apple.price*20
                                                
                                                

                    elif event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_d:
                        draw_everyone = not draw_everyone
                    elif event.key == pygame.K_t:
                        delay_time = int(input("enter delay time"))
                    elif event.key == pygame.K_s:
                        difficulty = int(input("enter difficulty(0 = hard, 10 = easy)"))
                    elif event.key == pygame.K_n:
                        gen_am = int(input("amount in generation"))
                    elif event.key == pygame.K_a:
                        draw_apples = not draw_apples


            screen.fill((255, 255, 255))
            for pl in players:
                if draw_everyone:
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
                    if draw_apples:
                        pygame.draw.circle(
                                            screen,
                                            (0, 0, 0),
                                            (pl.apple.x, pl.apple.y),
                                            pl.apple.radius
                        )

                        pygame.draw.circle(
                                            screen,
                                            (255, 0, 0),
                                            (pl.apple.x, pl.apple.y),
                                            pl.apple.radius-3
                        )
                pl.move()

            


            if alive:
                pygame.draw.circle(
                                    screen,
                                    (0, 0, 0),
                                    (players[main_player_num].x, players[main_player_num].y),
                                    players[main_player_num].radius
                )

                pygame.draw.circle(
                                    screen,
                                    (0, 100, 255),
                                    (players[main_player_num].x, players[main_player_num].y),
                                    players[main_player_num].radius-3
                )

                pygame.draw.circle(
                                    screen,
                                    (0, 0, 0),
                                    (players[main_player_num].apple.x, players[main_player_num].apple.y),
                                    players[main_player_num].apple.radius
                )

                pygame.draw.circle(
                                    screen,
                                    (255, 0, 0),
                                    (players[main_player_num].apple.x, players[main_player_num].apple.y),
                                    players[main_player_num].apple.radius-3
                )


            for i in obs:
                i.speed_y = 1
                pygame.draw.circle(
                            screen,
                            (0, 0, 0),
                            (i.x, i.y),
                            i.radius
                            )
                if i.move():
                    obs.remove(i)
                
                for pl in players:
                    if math.sqrt((pl.x - pl.apple.x)**2 + (pl.y - pl.apple.y)**2) <= pl.radius + pl.apple.radius:
                        pl.time += pl.apple.time_price
                        pl.apple.spawn(100)
                    pl.score += 0.01*((size-100)*math.sqrt(2) - math.sqrt((pl.x - pl.apple.x)**2 + (pl.y - pl.apple.y)**2))
                    #pl.score += 1
                    
                    if pl.check_collision(i) or pl.y + pl.radius >= size or pl.x + pl.radius >= size or pl.x - pl.radius <= 0 or pl.y - pl.radius <= 0 or pl.time < 0:
                        scoreboard[pl.score] = copy.deepcopy(pl.nn)
                        if alive:
                            prev_pl_main = players[main_player_num]
                            if pl is players[main_player_num]:
                                alive = False
                        players.remove(pl)
                        if alive:
                            try:
                                if not prev_pl_main is players[main_player_num]:
                                    main_player_num -= 1
                            except IndexError:
                                alive = False
                        if len(players) == 0:
                            mx = []
                            for i in range(1, number_of_living + 1):
                                try:
                                    mx.append(scoreboard[sorted(scoreboard.keys())[-i]])
                                except IndexError:
                                    print(i, "horrible")
                                    nullify_memory.fun(10, number_of_living)
                                    with open("memory.txt", "rb") as f:
                                        mx = pickle.load(f)
                                    for i in range(len(scoreboard.keys())):
                                        mx[i] = scoreboard[sorted(scoreboard.keys())[-i]]
                                    with open("memory.txt", "wb+") as f:
                                        pickle.dump(mx, f)
                                    break

                            print(len(scoreboard.keys()))
                            running = False

            for pl in players:
                outs = [0 for _ in range(8)]
                '''
                outs[1] = size - pl.x
                outs[0] = pl.x
                outs[3] = size - pl.y
                outs[2] = pl.y
                outs[4] = min(size - pl.x, size - pl.y) * math.sqrt(2)
                outs[5] = min(pl.x, pl.y) * math.sqrt(2)
                outs[6] = min(pl.x, pl.y) * math.sqrt(2)
                outs[7] = min(size - pl.x, pl.y) * math.sqrt(2)
                '''
                
                for i in obs:
                    temp = pl.look(i)
                    if temp:
                        if temp[0] not in outs or temp[1] < outs[temp[0]] or outs[temp[0]] == 0:
                            outs[temp[0]] = int(temp[1])
                pl.decide(*outs, pl.x - pl.apple.x, pl.y - pl.apple.y)
            pygame.display.flip()
            pygame.time.wait(1)
        if generation_number%10 == 0:
            print("remembering")
            with open("settings", "wb+") as f:
                pickle.dump((delay_time, difficulty, draw_everyone, generation_number, gen_am), f)
            with open("memory.txt", "wb+") as f:
                pickle.dump(mx, f)
except Exception:
    print(traceback.format_exc())
except KeyboardInterrupt:
    print("interrupted")
print("rememberin\'")
with open("settings", "wb+") as f:
    pickle.dump((delay_time, difficulty, draw_everyone, generation_number, gen_am), f)
with open("memory.txt", "wb+") as f:
    pickle.dump(best, f)