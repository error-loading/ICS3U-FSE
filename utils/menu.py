import pygame
from constants import *


class Menu:
    def __init__(self):
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.names = ["Overworld", "Platformer"]
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

    # item creation
        self.height = self.display_surface.get_size()[1] * 0.8
        self.width = self.display_surface.get_size()[0] // 3
        self.create_items()

    # selection system
        self.index = 0
        self.selection_time = None
        self.can_move = True

    def input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_RIGHT] and self.index < len(self.names) - 1:
                self.index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] and self.index > 0:
                self.index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                print(self.index)

    def create_items(self):
        self.item_list = []

        for item, index in enumerate(range(len(self.names))):
            full_width = self.display_surface.get_size()[0]
            increment = full_width // len(self.names)
            left = (item * increment) + (increment - self.width) // 2

            top = self.display_surface.get_size()[1] * 0.1

            item = Item(left, top, self.width, self.height, index, self.font)
            self.item_list.append(item)

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True

    def display(self):
        self.input()
        self.selection_cooldown()

        for item in self.item_list:
             item.display(self.display_surface, "test", 0)

class Item:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.Rect(l, t, w, h)
        self.index = index
        self.font = font
                
    def display(self, surface, num, name):
        pygame.draw.rect(surface, "#222222", self.rect, 0, 5)



