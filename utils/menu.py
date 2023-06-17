import pygame
import os
from constants import *
from utils.support import import_sprite_sheet
from config import config


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

    # overworld imgs
        self.overworld_chars = []
        self.overworld_names = []

        self.platform_chars = []
        self.platform_names = []

        self.get_imgs()

    # selection system
        self.index = 0
        self.index2 = 0
        self.quelleUn = 0   # pov: me going crazy while coding at 3am one day
        self.selection_time = None
        self.can_move = True
    
    def get_imgs(self):
        for char in os.listdir("assets/overworld/Characters"):
            if char != ".DS_Store":
                img = pygame.image.load(f"assets/overworld/Characters/{char}/Faceset.png").convert_alpha()
                img = pygame.transform.scale(img, (200, 200))
                self.overworld_chars.append(img)
                self.overworld_names.append(char)
        
        for char in os.listdir("assets/character/chars"):
            if char != ".DS_Store":
                img = import_sprite_sheet(f"assets/character/chars/{char}/idle.png", (32, 32))[0]
                img = pygame.transform.scale(img, (200, 200))
                self.platform_chars.append(img)
                self.platform_names.append(char)



    def input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:
            if self.quelleUn == 0:
                if keys[pygame.K_UP] and self.index < len(self.overworld_chars) - 1:
                    self.index += 1
                    self.can_move = False
                    self.selection_time = pygame.time.get_ticks()
                elif keys[pygame.K_DOWN] and self.index > 0:
                    self.index -= 1
                    self.can_move = False
                    self.selection_time = pygame.time.get_ticks()
            
            else:
                if keys[pygame.K_UP] and self.index2 < len(self.platform_chars) - 1:
                    self.index2 += 1
                    self.can_move = False
                    self.selection_time = pygame.time.get_ticks()
                elif keys[pygame.K_DOWN] and self.index2 > 0:
                    self.index2 -= 1
                    self.can_move = False
                    self.selection_time = pygame.time.get_ticks()
            
            if keys[pygame.K_RIGHT]:
                self.quelleUn = 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            
            elif keys[pygame.K_LEFT]:
                self.quelleUn = 0
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

            print(item, index)
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
        config.overworld_player = self.overworld_names[self.index]
        config.platform_player = self.platform_names[self.index2]

        for index, item in enumerate(self.item_list):       
            if not index:           
                item.display(self.display_surface, self.quelleUn, self.index, self.names[index], self.overworld_chars, self.overworld_names)
            else:           
                item.display(self.display_surface, self.quelleUn, self.index2, self.names[index], self.platform_chars, self.platform_names)

class Item:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.Rect(l, t, w, h)
        self.index = index
        self.font = font

    def display_name(self, surface, name, img, img_name, colour):
        title = self.font.render(name, False, colour)
        title_rect = title.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0, 20))

        char = pygame.Surface((img.get_width(), img.get_height()))
        char.blit(img, (0, 0))
        char_rect = char.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0, 80))

        name = self.font.render(img_name, False, colour)
        name_rect = name.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0, 300))

        surface.blit(title, title_rect)
        surface.blit(char, char_rect)
        surface.blit(name, name_rect)
                
    def display(self, surface, selection_num, num, name, char_imgs : list, char_names : list):
        pygame.draw.rect(surface, "#222222", self.rect, 0, 5)
        if self.index == selection_num:
            pygame.draw.rect(surface, BLUE, self.rect, 5, 5)
            self.display_name(surface, name, char_imgs[num], char_names[num], WHITE)
        
        else:
            self.display_name(surface, name, char_imgs[num], char_names[num], "#EEEEEE")



