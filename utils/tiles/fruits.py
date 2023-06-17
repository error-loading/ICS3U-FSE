'''
Gurjas Dhillon
fruits.py
This file contains the fruits classes
'''

import pygame
from utils.support import import_sprite_sheet

# Apple class
class Apple(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.posX = posX
        self.posY = posY

# animations
        self.frame_index = 0
        self.frame_rate = 0.5

# spritesheet
        self.collection = import_sprite_sheet("assets/items/apple/apple.png", (32, 32), (30, 30))
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        # offset
        self.rect.centery -= self.image.get_height()

# animating function
    def animate(self):
        self.frame_index += self.frame_rate
        self.frame_index %= len(self.collection)

        self.image = self.collection[int(self.frame_index)]

    def update(self, shiftX, shiftY):
        # animate
        self.animate()

        self.rect.centerx += shiftX
        self.rect.centery += shiftY

# banana class inheriting from apple class
class Banana(Apple):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.frame_index = 0
        self.frame_rate = 0.5

        self.collection = import_sprite_sheet("assets/items/banana/banana.png", (32, 32), (30, 30))
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.rect.centery -= self.image.get_height()

# cherry class inheriting from apple
class Cherry(Apple):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.frame_index = 0
        self.frame_rate = 0.5

        self.collection = import_sprite_sheet("assets/items/cherry/cherry.png", (32, 32), (30, 30))
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.rect.centery -= self.image.get_height()

# straberry class inheriting from apple
class Stawberry(Apple):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.frame_index = 0
        self.frame_rate = 0.5

        self.collection = import_sprite_sheet("assets/items/strawberry/strawberry.png", (32, 32), (30, 30))
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.rect.centery -= self.image.get_height()

# pineapple class inheriting from apple
class Pineapple(Apple):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.frame_index = 0
        self.frame_rate = 0.5

        self.collection = import_sprite_sheet("assets/items/pineapple/pineapple.png", (32, 32), (30, 30))
        self.image = self.collection[0]
        self.rect = self.image.get_rect(topleft = (posX, posY))

        self.rect.centery -= self.image.get_height()