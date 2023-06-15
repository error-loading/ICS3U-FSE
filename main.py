import pygame
import sys

from constants import *
from utils.level import Level
from utils.overworld import Overworld
from config import config
from game_data import lvl1, lvl2, lvl3

pygame.init()

running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))

myClock = pygame.time.Clock()

# creating instances
lvl1 = Level(screen, lvl1)
lvl2 = Level(screen, lvl2)
lvl3 = Level(screen, lvl3, (32, 32))

overworld = Overworld(screen)

while running:
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            running = False

    # run instances here
    if config.state == "overworld":
        overworld.run()

    elif config.state == "lvl1":
        lvl1.run()
        overworld.reset()
    
    elif config.state == "lvl2":
        lvl2.run()
        overworld.reset()
    
    elif config.state == "lvl3":
        lvl3.run()
        overworld.reset()


    myClock.tick(60)
    pygame.display.update() 


pygame.quit()
sys.exit()