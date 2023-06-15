import pygame
import sys

from constants import *
from utils.level import Level
from utils.overworld import Overworld
from config import config
from game_data import lvl1, lvl2

pygame.init()

running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))

myClock = pygame.time.Clock()

# creating instances
lvl1 = Level(screen, lvl1)
lvl2 = Level(screen, lvl2)

overworld = Overworld(screen)

while running:
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)

    lvl2.run()

    # run instances here
    # if config.state == "overworld":
    #     overworld.run()

    # elif config.state == "lvl1":
    #     lvl1.run()
    
    # elif config.state == "lvl2":
    #     lvl2.run()


    myClock.tick(60)
    pygame.display.update() 


pygame.quit()
sys.exit()