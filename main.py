import pygame
import sys
from constants import *

pygame.init()

running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))

myClock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GRAY)

    # run instances here
    level.run()

    myClock.tick(60)
    pygame.display.update() 


pygame.quit()
sys.exit()