'''
Gurjas Dhillon
config.py
This contains the code for everything related to teleport. 
'''

import pygame
from utils.player import Player
from utils.support import import_sprite_sheet
from config import config
from constants import *

# starting teleport class
class Teleport(pygame.sprite.Sprite):
    def __init__(self, posX, posY, portal):
        super().__init__()
        self.posX = posX
        self.posY = posY
        self.portal = portal
        self.cnt = 0  # used to keep a delay -> better alternative is to use clock.tick() but oh well

        # split the sprite sheet and returns a list
        self.animations = import_sprite_sheet("assets/character/Appearing (96x96).png", (96, 96))


        self.frame_index = 0
        self.frame_rate = 0.15
        self.image = self.animations[0]
        self.rect = self.image.get_rect(center = (self.posX, self.posY))

    def animate(self):
        self.frame_index += self.frame_rate

        # when the last image is reached, delete the portal and the teleport sprites
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

# ending teleport class
class TeleportAway(Teleport):
    def __init__(self, posX, posY, portal, player, overworld, reset, screen):
        # inherit these parameter from og teleport class
        super().__init__(posX, posY, portal)
        self.player = player
        self.portal = portal
        self.overworld = overworld
        self.reset = reset
        self.screen = screen
        self.animations = import_sprite_sheet("assets/character/Desappearing (96x96).png", (96, 96))

        # circle animations stuff
        self.clicked = False

        # circle transition properties
        self.circle_pos = (WIDTH // 2, HEIGHT // 2)
        self.initial_radius = 0
        self.target_radius = (WIDTH ** 2 + HEIGHT ** 2) ** 0.5 // 2
        self.current_radius = self.initial_radius
        self.animation_speed = 20

    
    def animate(self):
        self.frame_index += self.frame_rate
        
        # delete the portal when the last image has been reached
        if self.frame_index >= len(self.animations):
            self.portal.sprite.kill()
        
        else:
            self.image = self.animations[int(self.frame_index)]

    def cover_bg(self):
        # increase the circle's radius
        self.current_radius += self.animation_speed

        # ensure the circle does not exceed the screen size
        self.current_radius = min(self.current_radius, self.target_radius)

        # draw the circle
        pygame.draw.circle(self.screen, GRAY, self.circle_pos, self.current_radius)
        
        # if the circle covers the screen, switch to overworld and delete everything that is not required anymore
        if self.current_radius == self.target_radius:
            config.state = f"overworld"
            self.reset()
            self.overworld.reset()
            self.kill()
    
    # to check if the player collides with the portal using circles instead of rects this time for no particular reason
    def check_collision(self):
        return pygame.sprite.collide_circle(self.player.sprite, self.portal.sprite)

    def update(self, shiftX):
        if self.check_collision():
            self.animate()
            self.cover_bg()
            
        self.rect.x += shiftX


# portal class aka particles that flash by
class Portal(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.posX = posX
        self.posY = posY

        self.image = pygame.image.load("assets/character/transition.png").convert_alpha()
        self.rect = self.image.get_rect(center = (self.posX, self.posY))

    def update(self, shiftX):
        self.rect.x += shiftX