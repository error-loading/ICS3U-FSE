import pygame
from utils.support import import_sprite_sheet
from constants import *

class FallingTrap(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.posX = posX
        self.posY = posY
        self.gravity = 15

        self.collection = import_sprite_sheet("assets/traps/falling/On (32x10).png", (32, 10))

        # animation stuff
        self.frame_index = 0
        self.frame_rate = 0.25

        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.dead = False
        self.timer = 0

    def animate(self):
        self.frame_index += self.frame_rate
        self.frame_index %= len(self.collection)

        self.image = self.collection[int(self.frame_index)]
    
    def destroy(self):
        self.frame_rate = 0
        self.collection = [pygame.image.load("assets/traps/falling/Off.png").convert_alpha()]

        if self.timer >= 10:
            self.rect.y += self.gravity

        self.timer += 1

        if  self.rect.y > HEIGHT:
            self.kill()

    def update(self, shiftX, shiftY):
        self.rect.centerx += shiftX
        self.rect.centery += shiftY

        if not self.dead:
            self.animate()
        else:
            self.destroy()