import pygame
from constants import *
from utils.btn import Button
from config import config


class Intro:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("assets/bg.png").convert()
        self.start_image = pygame.image.load("assets/btn/start_btn.png").convert()

        self.zombiootitle = pygame.font.Font("font/Futurot.ttf", 130)

        self.start_btn = Button(WIDTH // 2 - 75, HEIGHT // 2 - 90, self.start_image, 1)

        self.clicked = False

        # circle animations stuff
        self.circle_pos = (WIDTH // 2, HEIGHT // 2)
        self.initial_radius = 0
        self.target_radius = (WIDTH ** 2 + HEIGHT ** 2) ** 0.5 // 2
        self.current_radius = self.initial_radius
        self.animation_speed = 20

    
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def cover_bg(self):
        # Increase the circle's radius
        self.current_radius += self.animation_speed

        # Ensure the circle does not exceed the screen size
        self.current_radius = min(self.current_radius, self.target_radius)

        pygame.draw.circle(self.screen, GRAY, self.circle_pos, self.current_radius)

        if self.current_radius == self.target_radius:
            config.state = f"overworld"
    
    def update(self):
        self.screen.blit(self.image, (0, 0))
        self.draw_text('TITLE', self.zombiootitle, WHITE, 350, 125)

        if self.start_btn.draw(self.screen):
            self.clicked = True
        
        if self.clicked:
            self.cover_bg()