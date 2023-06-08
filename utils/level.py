import pygame
from utils.support import import_csv, import_sprite_sheet
from utils.tiles.terrain import Terrain
from utils.tiles.spikes import Spikes
from utils.tiles.fruits import Apple, Banana, Cherry, Stawberry, Pineapple
from utils.tiles.falling_trap import FallingTrap
from utils.player import Player
from constants import *

# keep creating new instances of this class for different levels


class Level:
    def __init__(self, screen, data):
        # general info
        self.screen = screen
        self.data = data
        self.shiftX = 0
        self.shiftY = 0
        self.fruit_count = 0
        self.player_died = False

        # terrain
        self.terrain = import_csv(self.data["terrain"])
        self.terrain_sprite_sheet = import_sprite_sheet(
            "assets/terrain/terrain.png", (16, 16))
        self.terrain_sprites = self.create_group("terrain")

        # player
        self.player = import_csv(self.data["player"])
        self.player_sprite = self.create_group("player")

        # traps
        self.traps = import_csv(self.data["traps"])

        self.falling_trap_sprites = self.create_group("traps", "0")
        self.spike_sprites = self.create_group("traps", "5")

        # fruits
        self.fruits = import_csv(self.data["fruits"])
        self.fruits_sprites = self.create_group("fruits")

    # creating the tiles for terrains and collectables
    def create_group(self, type, trap_type = "-1"):
        group = pygame.sprite.Group()

        for x, row in enumerate(self.terrain):
            for y, val in enumerate(row):
                posX = y * TILESIZE
                posY = x * TILESIZE

                # this class creates groups for multiple types of tilesets

                if type == "player" and self.player[x][y] == "1":
                    sprite = pygame.sprite.GroupSingle()

                    self.start_pos = (posX, posY)
                    player = Player((posX, posY))
                    sprite.add(player)

                    return sprite


                # terrain tileset and the value is not -1
                if type == "terrain" and val != "-1":
                    sprite = Terrain(
                        posX, posY, self.terrain_sprite_sheet, int(val))
                    group.add(sprite)

                # traps tilesets
                if type == "traps":
                    # falling trap
                    if self.traps[x][y] == "0" and trap_type == "0":
                        sprite = FallingTrap(posX, posY)
                        group.add(sprite)

                    # saw trap
                    if self.traps[x][y] == "3" and trap_type == "3":
                        pass

                    # spikes
                    if self.traps[x][y] == "5" and trap_type == "5":
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
        fruits_hit = pygame.sprite.spritecollide(self.player_sprite.sprite, self.fruits_sprites, True, pygame.sprite.collide_mask)

        for fruit in fruits_hit:
            self.fruit_count += 1

    # check for horizontal collision
    def horizonal_collide(self):
        player = self.player_sprite.sprite

        player.rect.x += player.direction.x * player.speed

        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                player.in_air = False
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    # call function to reset the level
    def reset(self):
        pass

    # scrolling function
    def scrollX(self):
        player = self.player_sprite.sprite
        posX = player.rect.x
        
        if 700 < posX < WIDTH and player.direction.x > 0:
            player.speed = 0
            self.shiftX = -5
        
        elif 0 < posX < 300 and player.direction.x < 0:
            player.speed = 0
            self.shiftX = 5

        else:
            self.shiftX = 0
            player.speed = 5
    
    def scrollY(self):
        pass
        # player = self.player_sprite.sprite
        # self.shiftY = player.direction.y
    
    # spiek collide
    def spike_collide(self):
        dead = pygame.sprite.spritecollide(self.player_sprite.sprite, self.spike_sprites, False, pygame.sprite.collide_mask)

        for i in dead:
            self.player_died = True
            self.player_sprite.sprite.kill()
            print("dead")

    # function for teleporting
    def teleport(self):
        pass

    # check for vertical collision
    def vertical_collide(self):
        player = self.player_sprite.sprite 
        player.get_gravity()

        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                player.in_air = False
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    # this method will be called by the main function, all the stuff that will be going in the while loop will be called here
    def run(self):
        # terrain sprites draw and update
        self.terrain_sprites.draw(self.screen)
        self.terrain_sprites.update(self.shiftX, self.shiftY)

        # player sprites draw and update
        self.player_sprite.draw(self.screen)
        self.player_sprite.update()

        # falling trap sprites draw and update
        self.falling_trap_sprites.draw(self.screen)
        self.falling_trap_sprites.update(self.shiftX, self.shiftY)

        # spike strap sprites draw and update
        self.spike_sprites.draw(self.screen)
        self.spike_sprites.update(self.shiftX, self.shiftY)

        # fruit sprites draw and update
        self.fruits_sprites.draw(self.screen)
        self.fruits_sprites.update(self.shiftX, self.shiftY)


        # call other stuff
        if not self.player_died:
            self.vertical_collide()
            self.horizonal_collide()
            self.fruit_collide()
            self.scrollX()
            self.scrollY()
            self.spike_collide()