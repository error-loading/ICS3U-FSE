import pygame

class Spikes(pygame.sprite.Sprite):
    def __init__(self, posX, posY, scale):
        super().__init__()
        self.posX = posX
        self.posY = posY
        self.scale = scale

        self.image = pygame.image.load("assets/traps/spikes/spikes.png")
        self.image = pygame.transform.scale(self.image, self.scale)
        self.rect = self.image.get_rect(topleft = (posX, posY))


    def update(self, shiftX, shiftY):
        self.rect.centerx += shiftX
        self.rect.centery += shiftY