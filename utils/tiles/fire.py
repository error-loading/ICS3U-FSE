import pygame
from utils.support import import_sprite_sheet
from constants import *

class Fire(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.posX = posX
        self.posY = posY

        self.fire_off = pygame.image.load("assets/traps/Fire/Off.png").convert_alpha()
        self.fire_on = import_sprite_sheet("assets/traps/Fire/On (16x32).png", (18, 32)) + import_sprite_sheet("assets/traps/Fire/Hit (16x32).png", (18, 32))

        self.hit = False

        # animation stuff
        self.frame_index = 0
        self.frame_rate = 0.25

        self.image = self.fire_off
        self.rect = self.image.get_rect(topleft = (posX, posY))

    def animate(self):
        self.frame_index += self.frame_rate
        if self.frame_index >= len(self.fire_on):
            if self.get_hit(): 
                self.image = self.fire_off
                self.set_hit(False)

            else: 
                self.frame_index = 0

        if self.get_hit():
            self.image = self.fire_on[self.frame_index]

        else:
            self.image = self.fire_off

        
    def set_hit(self, val : bool):
        self.hit = val
        self.frame_index = 0
    
    def get_hit(self):
        return self.hit

    def update(self, shiftX, shiftY):
        self.rect.centerx += shiftX
        self.rect.centery += shiftY

        self.animate()