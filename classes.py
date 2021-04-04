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
        if abs(obj.x - self.x) < self.radius + obj.radius:
            if obj.y > self.y:
                return ("S", obj.y - self.y)
            else:
                return ("N", self.y - obj.y)
        if abs(obj.y - self.y) < self.radius + obj.radius:
            if obj.x > self.x:
                return("E", obj.x - self.x)
            else:
                return("W", self.x - obj.x)
        if obj.y < obj.x + self.y - self.x + math.sqrt(2)*self.radius and obj.y > obj.x + self.y - self.x - math.sqrt(2)*self.radius:
            if obj.x > self.x:
                return("SE", int(math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)))
            else:
                return("NW", int(math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)))
        if obj.y < -obj.x + self.x + self.y + math.sqrt(2)*self.radius and obj.y > -obj.x + self.x + self.y - math.sqrt(2)*self.radius:
            if obj.x > self.x:
                return("NE", int(math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)))
            else:
                return("SW", int(math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)))
        return False
            

class obstacle(thing):

    def move(self):
        self.y += self.speed_y
        self.x += self.speed_x  
        if self.y >= self.size or self.x >= self.size or self.x <= 0:
            return True
        return False

class smartPlayer(player):
    
    def __init__(self, x = 0, y = 0, radius = 10, speed = 2, speed_x = 0, speed_y = 0, size = 800, mxi = []):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.size = size
        self.nn = neuro.Neuro(10, 2, mxi)
        self.score = 0

    def decide(self, *ins):
        a = self.nn.calculate(*ins)
        if not a:
            print(ins, "ai")
            raise Exception
        x = a[0]
        y = a[1]
        self.speed_x = (math.floor(x*3)-1)*2
        self.speed_y = (math.floor(y*3)-1)*2

    def look(self, obj:thing):
        if abs(obj.x - self.x) < self.radius + obj.radius:
            if obj.y > self.y:
                return (0, obj.y - self.y)
            else:
                return (1, self.y - obj.y)
        if abs(obj.y - self.y) < self.radius + obj.radius:
            if obj.x > self.x:
                return(2, obj.x - self.x)
            else:
                return(3, self.x - obj.x)
        if obj.y < obj.x + self.y - self.x + math.sqrt(2)*self.radius and obj.y > obj.x + self.y - self.x - math.sqrt(2)*self.radius:
            if obj.x > self.x:
                return(4, int(math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)))
            else:
                return(5, int(math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)))
        if obj.y < -obj.x + self.x + self.y + math.sqrt(2)*self.radius and obj.y > -obj.x + self.x + self.y - math.sqrt(2)*self.radius:
            if obj.x > self.x:
                return(6, int(math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)))
            else:
                return(7, int(math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)))
        return False
