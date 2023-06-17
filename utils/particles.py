'''
Gurjas Dhillon
particles.py
This file contains the class for jumps particles
'''

import pygame

class Particles(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.animations = []

        self.get_imgs()

        self.image = self.animations[0]
        self.rect = self.image.get_rect(center = pos)
        self.rect.y -= 20

        # frame
        self.frame_index = 0
        self.frame_rate = 0.5
    
    def animation(self):
        self.frame_index += self.frame_rate

        # delete if it reaches the end
        if self.frame_index >= len(self.animations):
            self.kill()
        else:
            self.image = self.animations[int(self.frame_index)]

    # getting all the images 
    def get_imgs(self):
        for i in range(1, 7):
            img = pygame.image.load(f"assets/items/dust_particles/jump/jump_{i}.png").convert_alpha()
            self.animations.append(img)
        

    def update(self, shiftX):
        self.animation()  
        self.rect.x += shiftX
