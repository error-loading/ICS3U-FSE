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

    
    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))
    
    def update(self):
        self.screen.blit(self.image, (0, 0))
        self.draw_text('TITLE', self.zombiootitle, WHITE, 350, 125)

        if self.start_btn.draw(self.screen):
            config.state = "overworld"