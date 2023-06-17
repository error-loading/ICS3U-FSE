'''
Gurjas Dhillon
limits.py
THis is the class for Limit, mainly used to create a rect to detect collision
'''

import pygame
from constants import *

class Limit(pygame.sprite.Sprite):
    def __init__(self, posX, posY, screen):
        super().__init__()
        self.posX = posX
        self.posY = posY
        self.screen = screen

        self.image = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA).convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.posX, self.posY))
        self.image.set_colorkey(RED)
    
    def update(self, shiftX, shiftY):
        self.rect.x += shiftX
        self.rect.y += shiftY