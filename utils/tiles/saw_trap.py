import pygame
from utils.support import import_sprite_sheet

class Saw_Trap(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.posX = posX
        self.posY = posY

        # frame stuff
        self.frame_index = 0
        self.frame_rate = 0.25

        self.animations = import_sprite_sheet("assets/traps/Saw/On (38x38).png", (38, 38))
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(centerx = posX, centery = posY)
    
    def animate(self):
        self.frame_index += self.frame_rate
        
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        
        self.image = self.animations[int(self.frame_index)]

    def update(self, shiftX, shiftY):
        self.rect.centerx += shiftX
        self.rect.centery += shiftY

        self.animate()