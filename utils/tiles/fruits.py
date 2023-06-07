import pygame
from utils.support import import_sprite_sheet

class Apple(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.posX = posX
        self.posY = posY

        self.frame_index = 0
        self.frame_rate = 0.5

        self.collection = import_sprite_sheet("assets/items/apple/apple.png", (32, 32), (30, 30))
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.rect.centery -= self.image.get_height()

    def animate(self):
        self.frame_index += self.frame_rate
        self.frame_index %= len(self.collection)

        self.image = self.collection[int(self.frame_index)]

    def update(self, shiftX, shiftY):
        # animate
        self.animate()

        self.rect.centerx += shiftX
        self.rect.centery += shiftY

class Banana(Apple):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.frame_index = 0
        self.frame_rate = 0.5

        self.collection = import_sprite_sheet("assets/items/banana/banana.png", (32, 32), (30, 30))
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.rect.centery -= self.image.get_height()

class Cherry(Apple):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.frame_index = 0
        self.frame_rate = 0.5

        self.collection = import_sprite_sheet("assets/items/cherry/cherry.png", (32, 32), (30, 30))
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.rect.centery -= self.image.get_height()

class Stawberry(Apple):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.frame_index = 0
        self.frame_rate = 0.5

        self.collection = import_sprite_sheet("assets/items/strawberry/strawberry.png", (32, 32), (30, 30))
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.rect.centery -= self.image.get_height()

class Pineapple(Apple):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.frame_index = 0
        self.frame_rate = 0.5

        self.collection = import_sprite_sheet("assets/items/pineapple/pineapple.png", (32, 32), (30, 30))
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.rect.centery -= self.image.get_height()