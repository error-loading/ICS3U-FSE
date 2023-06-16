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

        self.lvl1_sprites = self.create_group("lvl1")
        self.lvl2_sprites = self.create_group("lvl2")
        self.lvl3_sprites = self.create_group("lvl3")
        self.lvl4_sprites = self.create_group("lvl4")

        self.lvl_sprites = [self.lvl1_sprites, self.lvl2_sprites, self.lvl3_sprites, self.lvl4_sprites]

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
                    self.start_pos = (posX, posY)
                    sprite = Player((posX, posY), self.screen, self.limit_sprites, self.lvl_sprites)
                    group.add(sprite)
                    return group

                elif type == "limit":
                    if self.limit_csv[x][y] == "-1":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)
                
                elif type == "lvl1":
                    if self.limit_csv[x][y] == "104":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)

                elif type == "lvl2":
                    if self.limit_csv[x][y] == "105":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)
                
                elif type == "lvl3":
                    if self.limit_csv[x][y] == "106":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)

                elif type == "lvl4":
                    if self.limit_csv[x][y] == "146":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)
                
        
        return group

    def reset(self):
        self.__init__(self.screen)


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
        