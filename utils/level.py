import pygame
from utils.support import import_csv, import_sprite_sheet
from utils.tiles.terrain import Terrain
from utils.tiles.spikes import Spikes
from utils.tiles.fruits import Apple, Banana, Cherry, Stawberry, Pineapple
from utils.tiles.falling_trap import FallingTrap
from constants import *

# keep creating new instances of this class for different levels


class Level:
    def __init__(self, screen, data):
        # general info
        self.screen = screen
        self.data = data
        self.shiftX = -1
        self.shiftY = 0

        # terrain
        self.terrain = import_csv(self.data["terrain"])
        self.terrain_sprite_sheet = import_sprite_sheet(
            "assets/terrain/terrain.png", (16, 16))
        self.terrain_sprites = self.create_group("terrain")

        # traps
        self.traps = import_csv(self.data["traps"])
        self.traps_sprites = self.create_group("traps")

        # fruits
        self.fruits = import_csv(self.data["fruits"])
        self.fruits_sprites = self.create_group("fruits")

    # creating the tiles for terrains and collectables
    def create_group(self, type):
        group = pygame.sprite.Group()

        for x, row in enumerate(self.terrain):
            for y, val in enumerate(row):
                posX = y * TILESIZE
                posY = x * TILESIZE

                # this class creates groups for multiple types of tilesets

                # terrain tileset and the value is not -1
                if type == "terrain" and val != "-1":
                    sprite = Terrain(
                        posX, posY, self.terrain_sprite_sheet, int(val))
                    group.add(sprite)

                # traps tilesets
                if type == "traps":
                    # falling trap
                    if self.traps[x][y] == "0":
                        sprite = FallingTrap(posX, posY)
                        group.add(sprite)

                    # saw trap
                    if self.traps[x][y] == "3":
                        pass

                    # spikes
                    if self.traps[x][y] == "5":
                        sprite = Spikes(posX, posY)
                        group.add(sprite)

                # fruit tilesets
                if type == "fruits":
                    # Apple
                    if self.fruits[x][y] == "1":
                        sprite = Apple(posX, posY)
                        group.add(sprite)

                    # Banana
                    elif self.fruits[x][y] == "2":
                        sprite = Banana(posX, posY)
                        group.add(sprite)

                    # Cherry
                    elif self.fruits[x][y] == "3":
                        sprite = Cherry(posX, posY)
                        group.add(sprite)

                    # Stawberry
                    elif self.fruits[x][y] == "4":
                        sprite = Stawberry(posX, posY)
                        group.add(sprite)

                    # Pineapple
                    elif self.fruits[x][y] == "6":
                        sprite = Pineapple(posX, posY)
                        group.add(sprite)

        return group

    # creating the player
    def create_player(self):
        pass

    # method is called to check if game is over
    def check_game_over(self):
        pass

    # fruit collision
    def fruit_collide(self):
        pass

    # check for horizontal collision
    def horizonal_collide(self):
        pass

    # call function to reset the level
    def reset(self):
        pass

    # function for teleporting
    def teleport(self):
        pass

    # check for vertical collision
    def vertical_collide(self):
        pass

    # this method will be called by the main function, all the stuff that will be going in the while loop will be called here
    def run(self):
        # terrain sprites draw and update
        self.terrain_sprites.draw(self.screen)
        self.terrain_sprites.update(self.shiftX, self.shiftY)

        # trap sprites draw and update
        self.traps_sprites.draw(self.screen)
        self.traps_sprites.update(self.shiftX, self.shiftY)

        # fruit sprites draw and update
        self.fruits_sprites.draw(self.screen)
        self.fruits_sprites.update(self.shiftX, self.shiftY)
