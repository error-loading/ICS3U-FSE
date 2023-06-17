'''
Gurjas Dhillon
arrow.py
This file contains the Arrow trap
'''

import pygame
from utils.support import import_sprite_sheet
from constants import *

class Arrow(pygame.sprite.Sprite):
    def __init__(self, posX, posY, scale):
        super().__init__()
        self.posX = posX
        self.posY = posY
        self.scale = scale

        # spritesheet for idle and when it collides
        self.collection = import_sprite_sheet("assets/traps/arrow/Idle (18x18).png", (18, 18), self.scale)
        self.hit_collection = import_sprite_sheet("assets/traps/arrow/Hit (18x18).png", (18, 18), self.scale)

        self.hit = False

        # animation stuff
        self.frame_index = 0
        self.frame_rate = 0.25

        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

# animating through the sprites
    def animate(self):
        self.frame_index += self.frame_rate

        if self.frame_index >= len(self.collection):
            if not self.hit: self.frame_index = 0
            else: self.kill()
        
        if self.hit:
            self.image = self.hit_collection[int(self.frame_index)]
            
        else:
            self.image = self.collection[int(self.frame_index)]
    
    # doing stuff if it collides
    def hit_arrow(self):
        self.frame_index = 0
        self.hit = True

    def update(self, shiftX, shiftY):
        self.rect.centerx += shiftX
        self.rect.centery += shiftY

        self.animate()