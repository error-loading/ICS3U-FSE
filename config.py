'''
Gurjas Dhillon
config.py
This is a simple Config class that stores general info related to the game. Last time I used a json file for this data, but it ran into multiple problems since sometimes it was trying to access a key in the json while it was updating. 
'''

class Config:
    def __init__(self):
        self.state = "menu"
        self.overworld_player = "Samurai"
        self.platform_player = "Virtual Guy"

config = Config()