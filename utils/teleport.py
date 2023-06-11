from utils.player import Player
from utils.support import import_sprite_sheet
import pygame
import time

class Teleport(pygame.sprite.Sprite):
    def __init__(self, posX, posY, portal):
        super().__init__()
        self.posX = posX
        self.posY = posY
        self.portal = portal
        self.cnt = 0

        self.animations = import_sprite_sheet("assets/character/Appearing (96x96).png", (96, 96))


        self.frame_index = 0
        self.frame_rate = 0.15
        self.image = self.animations[0]
        self.rect = self.image.get_rect(center = (self.posX, self.posY))

    def animate(self):
        self.frame_index += self.frame_rate

        if self.frame_index >= len(self.animations):
            self.portal.kill()
            self.kill()
        
        else:
            self.image = self.animations[int(self.frame_index)]
    

    def update(self, shiftX):
        self.cnt += 1

        if self.cnt > 30:
            self.animate()

        self.rect.x += shiftX

class Portal(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.posX = posX
        self.posY = posY

        self.image = pygame.image.load("assets/character/transition.png").convert_alpha()
        self.rect = self.image.get_rect(center = (self.posX, self.posY))

    def update(self, shiftX):
        self.rect.x += shiftX