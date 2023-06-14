import pygame
from utils.support import import_sprite_sheet, import_csv
from utils.overworldTiles.terrain import Terrain
from utils.overworldTiles.player import Player

TILESIZE = 32

class Overworld:
    def __init__(self, screen):
        self.screen = screen
        self.player = "Samurai"


        self.house_csv = import_csv("levels/overworld/overworld_houses.csv")
        self.house_imgs = import_sprite_sheet("assets/overworld/house.png", (16, 16), (32, 32))
        self.house_sprites = self.create_group("house")

        self.limit_csv = import_csv("levels/overworld/overworld_contraints.csv")
        self.limit_sprites = self.create_group("limit")

        self.water_csv = import_csv("levels/overworld/overworld_water.csv")
        self.water_imgs = import_sprite_sheet("assets/overworld/water.png", (16, 16), (32, 32))
        self.water_sprites = self.create_group("water")

        self.water_details_csv = import_csv("levels/overworld/overworld_water_details.csv")
        self.water_details_sprites = self.create_group("water_details")

        self.nature_csv = import_csv("levels/overworld/overworld_nature.csv")
        self.nature_imgs = import_sprite_sheet("assets/overworld/nature.png", (16, 16), (32, 32))
        self.nature_sprites = self.create_group("nature")

        self.terrain_csv = import_csv("levels/overworld/overworld_terrain.csv")
        self.terrain_imgs = import_sprite_sheet("assets/overworld/terrain.png", (16, 16), (32, 32))
        self.terrain_sprites = self.create_group("terrain")

        self.floor_csv = import_csv("levels/overworld/overworld_floor.csv")
        self.floor_imgs = import_sprite_sheet("assets/overworld/floor.png", (16, 16), (32, 32))
        self.floor_sprites = self.create_group("floor")

        self.player_csv = import_csv("levels/overworld/overworld_floor.csv")
        self.player_sprites = self.create_group("player")

    def create_group(self, type):
        group = pygame.sprite.Group()

        for x, row in enumerate(self.house_csv):
            for y, val in enumerate(row):
                posX = y * TILESIZE
                posY = x * TILESIZE

                if type == "terrain":
                    sprite = Terrain(posX, posY, self.terrain_imgs, int(self.terrain_csv[x][y]))
                    group.add(sprite)
                
                elif type == "nature":
                    sprite = Terrain(posX, posY, self.nature_imgs, int(self.nature_csv[x][y]))
                    group.add(sprite)
                
                elif type == "floor":
                    sprite = Terrain(posX, posY, self.floor_imgs, int(self.floor_csv[x][y]))
                    group.add(sprite)
                
                elif type == "house":
                    sprite = Terrain(posX, posY, self.house_imgs, int(self.house_csv[x][y]))
                    group.add(sprite)
                
                elif type == "water":
                    sprite = Terrain(posX, posY, self.water_imgs, int(self.water_csv[x][y]))
                    group.add(sprite)
                
                elif type == "water_details":
                    sprite = Terrain(posX, posY, self.water_imgs, int(self.water_details_csv[x][y]))
                    group.add(sprite)
                
                elif type == "player" and self.player_csv[x][y] == "1":
                    group = pygame.sprite.GroupSingle()
                    sprite = Player((posX, posY), self.screen, self.limit_sprites)
                    group.add(sprite)
                    return group

                elif type == "limit":
                    if self.limit_csv[x][y] == "-1":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)
                
        
        return group


    def run(self):
        self.terrain_sprites.draw(self.screen)
        self.terrain_sprites.update()

        self.floor_sprites.draw(self.screen)
        self.floor_sprites.update()

        self.nature_sprites.draw(self.screen)
        self.nature_sprites.update()

        self.water_sprites.draw(self.screen)
        self.water_sprites.update()

        self.water_details_sprites.draw(self.screen)
        self.water_details_sprites.update()

        self.house_sprites.draw(self.screen)
        self.house_sprites.update()

        self.player_sprites.draw(self.screen)
        self.player_sprites.update()
        