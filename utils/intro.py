'''
Gurjas Dhillon
intro.py
This is the starting page of the game
'''

import pygame
from constants import *

from config import config


class Intro:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("assets/bg.png").convert()
        self.start_image = pygame.image.load("assets/btn/start_btn.png").convert()

        self.zombiootitle = pygame.font.Font("font/Futurot.ttf", 130)


        self.clicked = False

        # circle animations stuff
        self.circle_pos = (WIDTH // 2, HEIGHT // 2)
        self.initial_radius = 0
        self.target_radius = (WIDTH ** 2 + HEIGHT ** 2) ** 0.5 // 2
        self.current_radius = self.initial_radius
        self.animation_speed = 20

    
        self.rect = pygame.Rect(410, 373, 264, 75)

    def cover_bg(self):
        # Increase the circle's radius
        self.current_radius += self.animation_speed

        # Ensure the circle does not exceed the screen size
        self.current_radius = min(self.current_radius, self.target_radius)

        pygame.draw.circle(self.screen, GRAY, self.circle_pos, self.current_radius)

        if self.current_radius == self.target_radius:
            config.state = f"overworld"

    def collision(self):
        pos = pygame.mouse.get_pos()

		#check mouseover
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
    
    def update(self):
        self.screen.blit(self.image, (0, 0))
        pygame.draw.rect(self.screen, WHITE, self.rect, 3)
        self.collision()
        
        if self.clicked:
            self.cover_bg()