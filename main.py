import pygame
import sys

from constants import *
from utils.level import Level
from utils.overworld import Overworld
from utils.intro import Intro
from config import config
from game_data import lvl1, lvl2, lvl3, lvl4, lvl5, lvl6

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
lvl5 = Level(screen, lvl5, overworld, (32, 32))
lvl6 = Level(screen, lvl6, overworld, (32, 32))
intro = Intro(screen)

while running:
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and config.state == "overworld":
                overworld.toggle()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q and config.state == "overworld":
                overworld.toggle()


    # run instances here
    if config.state == "menu":
        intro.update()

    elif config.state == "overworld":
        overworld.run()

    elif config.state == "lvl1":
        lvl1.run()
    
    elif config.state == "lvl2":
        lvl2.run()
    
    elif config.state == "lvl3":
        lvl3.run()
    
    elif config.state == "lvl4":
        lvl4.run()
    
    elif config.state == "lvl5":
        lvl5.run()
    
    elif config.state == "lvl6":
        lvl6.run()

    myClock.tick(60)
    pygame.display.update() 


pygame.quit()
sys.exit()