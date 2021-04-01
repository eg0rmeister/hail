import pygame
import math
import time
import random
import neuro


class thing():

    def __init__(self, x = 0, y = 0, radius = 10, speed = 2, speed_x = 0, speed_y = 0, size = 800):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.size = size




class player(thing):
    
    def move(self):
        self.y += self.speed_y
        self.x += self.speed_x
        if self.x > self.size:
            self.x = self.size
        if self.x < 0:
            self.x = 0
        if self.y > self.size:
            self.y = self.size
        if self.y < 0:
            self.y = 0
    
    def check_collision(self, obj:thing):
        if math.sqrt((obj.x - self.x)**2 + (obj.y - self.y)**2) <= self.radius + obj.radius:
            return True
        return False
    
    def look(self, obj:thing):
        if math.abs(obj.x - self.x) < self.radius + obj.radius:
            if obj.y > self.y:
                return ("N", obj.y - self.y)
            else:
                return ("S", self.y - obj.y)
        if math.abs(obj.y - self.y) < self.radius + obj.radius:
            if obj.x > self.x:
                return("E", obj.x - self.x)
            else:
                return("W", self.x - obj.x)]
        if obj.y < self.y + obj.x + math.sqrt(2)*self.radius and obj.y > self.y + obj.x - math.sqrt(2)*self.radius:
            return("diag_right", math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2))
        if obj.y < self.y - obj.x + math.sqrt(2)*self.radius and obj.y > self.y - obj.x - math.sqrt(2)*self.radius:
            return("diag_right", math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2))
            

class obstacle(thing):

    def move(self):
        self.y += self.speed_y
        self.x += self.speed_x  
        if self.y >= self.size or self.x >= self.size or self.x <= 0:
            return True
        return False


pygame.font.init()

pygame.init()


speed = 2
speed_obstacle = 1
size = 800

pl = player(size//2, size*3//4)

screen = pygame.display.set_mode((size, size))



running = True
key = None
obs = []

pygame.display.flip()

for i in 


neu = neuro.Neuro()


while running:
    if random.randint(0, 50) == 0:
        obs.append  (
                        obstacle(
                                speed_y= 1,
                                x= random.randint(1, size-1),
                                y= 1
                                )
                    )


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

    screen.fill((255, 255, 255))
    pl.move()
    color_r = (255, 0, 0)
    color_l = (255, 0, 0)
    color_u = (255, 0, 0)
    color_d = (255, 0, 0)
    if pl.speed_x > 0:
        color_r = (0, 255, 0)
    elif pl.speed_x < 0:
        color_l = (0, 255, 0)
    if pl.speed_y > 0:
        color_d = (0, 255, 0)
    elif pl.speed_y < 0:
        color_u = (0, 255, 0)


    pygame.draw.line(screen, color_r, (pl.x + pl.radius, pl.y), (size, pl.y))
    pygame.draw.line(screen, color_l, (pl.x - pl.radius, pl.y), (0, pl.y))
    pygame.draw.line(screen, color_u, (pl.x, pl.y + pl.radius), (pl.x, 0))
    pygame.draw.line(screen, color_d, (pl.x, pl.y - pl.radius), (pl.x, size))

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
