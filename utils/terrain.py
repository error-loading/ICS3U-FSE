import pygame
from support import import_sprite_sheet

# class for the terrain tiles
class Terrain(pygame.sprite.Sprite):
    def __init__(self, posX, posY, val = None):
        self.posX = posX
        self.posY = posY
        self.val = val


    def update(self, shiftX, shiftY):
        self.rect.centerx += shiftX
        self.rect.centery += shiftY