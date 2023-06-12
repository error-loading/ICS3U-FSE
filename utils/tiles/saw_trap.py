import pygame
from utils.support import import_sprite_sheet
from constants import *

from math import floor

class Saw_Trap(pygame.sprite.Sprite):
    def __init__(self, posX, posY, terrain):
        super().__init__()
        self.posX = posX
        self.posY = posY
        self.terrain = terrain

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
    
    def check_pos(self):
        y = floor(self.rect.bottomleft[0] / TILESIZE)
        x = floor(self.rect.bottomleft[1] / TILESIZE)

        # check if the saw is in top row
        if self.terrain[x][y-1] == "-1":
            # top right
            if self.terrain[x+1][y] == "-1":
                self.direction.x = 1
                self.direction.y = 0
            
            # top left
            elif self.terrain[x-1][y] == "-1":
                self.direction.x = 1
                self.direction.y = 0
        
        # check it is in bottom row
        elif self.terrain[x][y+1] == "-1":
            # bottom right
            if self.terrain[x+1][y] == "-1":
                self.direction.x = -1
                self.direction.y = 0
            
            # bottom left
            if self.terrain[x-1][y] == "-1":
                self.direction.x = 0
                self.direction.y = -1

    def move(self):
        self.rect.center += self.direction

    def update(self, shiftX, shiftY):
        self.rect.centerx += shiftX
        self.rect.centery += shiftY

        self.check_pos()
        self.animate()
        self.move()