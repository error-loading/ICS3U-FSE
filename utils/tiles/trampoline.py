import pygame
from utils.support import import_sprite_sheet
from constants import *

class Arrow(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.posX = posX
        self.posY = posY

        self.idle_image = pygame.image.load("assets/traps/trampoline/Idle.png").convert_alpha()
        self.collection = import_sprite_sheet("assets/traps/trampoline/Jump (28x28).png", (28, 28))

        self.bounce = False

        # animation stuff
        self.frame_index = 0
        self.frame_rate = 0.25

        self.image = self.idle_image
        self.rect = self.image.get_rect(topleft = (posX, posY))

    def animate(self):
        if self.bounce:
            self.frame_index += self.frame_rate

            if self.frame_index >= len(self.collection):
                self.bounce = False
                self.frame_index = 0
                self.image = self.idle_image
            
        
    def change_bounce(self):
        self.bounce = True

    def update(self, shiftX, shiftY):
        self.rect.centerx += shiftX
        self.rect.centery += shiftY

        self.animate()