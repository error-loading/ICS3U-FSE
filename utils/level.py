import pygame
from utils.support import import_csv

# keep creating new instances of this class for different levels
class Level:
    def __init__(self, screen, data):
        self.screen = screen
        self.data = data

        # terrain
        self.terrain = import_csv()
    
    # creating the tiles for terrains and collectables
    def create_group(self, type):
        pass

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
    def run():
        pass