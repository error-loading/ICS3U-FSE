import pygame

# class for the terrain tiles
class Terrain(pygame.sprite.Sprite):
    def __init__(self, posX, posY, tiles, val):
        super().__init__()
        self.posX = posX
        self.posY = posY
        self.val = val
        self.tiles = tiles

        self.image = self.tiles[val]
        self.rect = self.image.get_rect(topleft = (posX, posY))
