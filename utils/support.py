import pygame
from csv import reader
import json

# cutting a sprite sheet and return the individual images in a python list
def import_sprite_sheet(path, sz, scale=None):
	imgs = []

	sprite_sheet = pygame.image.load("assets/terrain/terrain.png").convert_alpha()
	width = sprite_sheet.get_width()
	height = sprite_sheet.get_height()

	rows = int(height / sz[1])
	
	for row in range(rows):
		frame_no = 0

		while frame_no * sz[0] < width:
			frame = pygame.Surface(sz)
			rect = (frame_no * sz[0], row * sz[1], sz[0], sz[1])

			frame.blit(sprite_sheet, (0, 0), rect)
			frame.set_colorkey((0, 0, 0))

			if scale:
				frame = pygame.transform.scale(frame, scale)

			imgs.append(frame)
			frame_no += 1

	return imgs

# read a csv file and return a 2D list conversion
def import_csv(path):
    lvl = reader(open(path), delimiter=",")
    layout = [list(line) for line in lvl]
    return layout

# updating json value given a key and a value
def update_json(path, key, val):
	with open(path) as f:
		data = json.load(f)
	
	data[key] = val

	with open(path, "w") as f:
		json.dump(data, f)

# returning the value of a certain key in a json file
def get_json(path, key):
	with open(path, "r") as f:
		data = json.load(f)

	return data[key] 