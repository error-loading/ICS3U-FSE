import pygame
import sys

from constants import *
from utils.level import Level
from game_data import lvl1

pygame.init()

running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))

myClock = pygame.time.Clock()

# creating instances
level = Level(screen, lvl1)

while running:
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GRAY)

    # run instances here
    level.run()

    myClock.tick(50)
    pygame.display.update() 


pygame.quit()
sys.exit()