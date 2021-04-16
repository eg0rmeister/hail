import pygame
import math
import time
import random

import classes

pygame.init()
running = True
size = 800
screen = pygame.display.set_mode((size, size))
while running:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pygame.QUIT:
            exit()