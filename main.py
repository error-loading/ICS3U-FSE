import pygame
import sys

from constants import *
from utils.level import Level
from utils.overworld import Overworld
from config import config
from game_data import lvl1, lvl2, lvl3, lvl4

pygame.init()

running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))

myClock = pygame.time.Clock()

# creating instances
overworld = Overworld(screen)
lvl1 = Level(screen, lvl1, overworld)
lvl2 = Level(screen, lvl2, overworld)
lvl3 = Level(screen, lvl3, overworld)
lvl4 = Level(screen, lvl4, overworld)

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
    
    elif config.state == "lvl2":
        lvl2.run()
    
    elif config.state == "lvl3":
        lvl3.run()
    
    elif config.state == "lvl4":
        lvl4.run()


    myClock.tick(60)
    pygame.display.update() 


pygame.quit()
sys.exit()