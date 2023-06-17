'''
Gurjas Dhillon
saw_rtrappy
This file contains the Saw_trap class
'''

import pygame
from utils.support import import_sprite_sheet
from constants import *

from math import floor

class Saw_Trap(pygame.sprite.Sprite):
    def __init__(self, posX, posY, x, y, terrain, limit_sprites):
        super().__init__()
        self.posX = posX
        self.posY = posY
        self.x = x
        self.y = y
        self.terrain = terrain
        self.limit = limit_sprites

        # frame stuff
        self.frame_index = 0
        self.frame_rate = 0.25

        # direction/speed
        self.direction = pygame.math.Vector2(1, 0)

        self.animations = import_sprite_sheet("assets/traps/Saw/On (38x38).png", (38, 38))
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(centerx = posX, centery = posY)

    def animate(self):
        self.frame_index += self.frame_rate
        
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        
        self.image = self.animations[int(self.frame_index)]
    
    def switch(self):
        self.direction.x *= -1

    def move(self):
        self.rect.center += self.direction

    def update(self, shiftX, shiftY):
        self.rect.centerx += shiftX
        self.rect.centery += shiftY

        self.x += (self.rect.x - self.x * TILESIZE) // TILESIZE
        self.y += (self.rect.y - self.y * TILESIZE) // TILESIZE

        self.animate()
        self.move()