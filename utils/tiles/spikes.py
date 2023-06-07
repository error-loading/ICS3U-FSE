import pygame

class Spikes(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.posX = posX
        self.posY = posY

        self.image = pygame.image.load("assets/traps/spikes/spikes.png")
        self.rect = self.image.get_rect(topleft = (posX, posY))


    def update(self, shiftX, shiftY):
        self.rect.centerx += shiftX
        self.rect.centery += shiftY