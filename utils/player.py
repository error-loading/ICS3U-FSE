'''
Gurjas Dhillon
player.py
This is the Player class for the main platform. This contains all the data for the player including moving the player, applying gravity, etc.
'''

# import stuff
import pygame
from utils.support import import_sprite_sheet
from utils.particles import Particles
from constants import *
from config import config

# class for the player, all the functionality of the player will be here
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen, create_particles, char="Virtual Guy"):
        super().__init__()  # inheriting from the pygame.sprite.Sprite class
        self.pos = pos
        self.char = char
        self.screen = screen
        self.create_particles = create_particles

        # character stuff
        self.gravity = 0.3
        self.scale = (50, 50)
        self.scrollY = 0
        self.jump_speed = -10
        self.jump_force = -10    
        self.direction = pygame.math.Vector2(0, 0) # direction represents which way it's currently moving -> (-1, 0) means it's moving to the left, (0, -1) would normally mean it is moving down, but since pygame is weird, this means that it is moving up, etc.
        self.speed = 5
        self.in_air = True
        self.double_jump = True

        # animations
        self.animation = []
        self.flip = False

        # particles
        self.run_particles = []

        # getting all the sprites and all the states for the character sprite and the run particle sprites
        self.get_imgs()

        # wall
        self.on_right = False
        self.on_left = False

        # states
        self.IDLE = 0
        self.JUMP = 1
        self.RUN = 2
        self.FALL = 3
        self.HIT = 4
        self.WALL = 5
        self.DOUBLEJUMP = 6

        # holds the current state of the player
        self.action = 0

        self.frame_index = 0
        self.frame_rate = 0.25

        # frame stuff for the run particles
        self.run_frame_index = 0
        self.run_frame_rate = 0.15

        self.image = self.animation[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(pos[0] - self.image.get_width() // 2, pos[1]))

    # animating
    def animate(self):
        self.frame_index += self.frame_rate

        if self.frame_index >= len(self.animation[self.action]):
            # if it has reached the end of the list, these states should stay at the last sprite
            if self.action == self.HIT or self.action == self.JUMP or self.action == self.DOUBLEJUMP:
                if self.action == self.DOUBLEJUMP: self.action = self.JUMP
                self.frame_index = len(self.animation[self.action]) - 1
            
            # the rest should be resetted to the start
            else:
                self.frame_index = 0

        self.image = self.animation[self.action][int(self.frame_index)]
    
    # method checks if the player was changed through the menu and updates the images if it returns true
    def check_player_name(self):
        if config.platform_player != self.char:
            self.char = config.platform_player
            self.get_imgs()

    # died
    def dead(self):
        self.jump()
        self.update_action(self.HIT)

    # flipping the image
    def flip_img(self):
        self.image = pygame.transform.flip(self.image, self.flip, False)

    # getting gravity
    def get_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    # getting imgs
    def get_imgs(self):
        # character sprites
        self.animation = []
        idle = import_sprite_sheet(
            f"assets/character/chars/{self.char}/idle.png", (32, 32), self.scale)
        jump = import_sprite_sheet(
            f"assets/character/chars/{self.char}/jump.png", (32, 32), self.scale)
        run = import_sprite_sheet(
            f"assets/character/chars/{self.char}/run.png", (32, 32), self.scale)
        fall = import_sprite_sheet(
            f"assets/character/chars/{self.char}/fall.png", (32, 32), self.scale)
        hit = import_sprite_sheet(
            f"assets/character/chars/{self.char}/hit.png", (32, 32), self.scale)
        wall = import_sprite_sheet(
            f"assets/character/chars/{self.char}/wall.png", (32, 32), self.scale)
        doublejump = import_sprite_sheet(
            f"assets/character/chars/{self.char}/doublejump.png", (32, 32), self.scale)
        
        # run particle sprites
        for i in range(1, 6):
            img = pygame.image.load(f"assets/items/dust_particles/run/run_{i}.png")
            self.run_particles.append(img)

        self.animation.append(idle)
        self.animation.append(jump)
        self.animation.append(run)
        self.animation.append(fall)
        self.animation.append(hit)
        self.animation.append(wall)
        self.animation.append(doublejump)

    # getting input from the user
    def get_input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_RIGHT]:
            self.direction.x = 1
            self.flip = False
            self.update_action(self.RUN)

            # wall stuff on right side
            if self.on_right:
                self.in_air = False
                self.direction.y = 0.5
                self.update_action(self.WALL)
        
        elif key[pygame.K_LEFT]:
            self.direction.x = -1
            self.flip = True
            self.update_action(self.RUN)

            # wall stuff on left side
            if self.on_left and not self.in_air:
                self.direction.y = 0.5
                self.update_action(self.WALL)
            
        else:
            self.direction.x = 0
            self.on_left = False
            self.on_right = False

        if key[pygame.K_SPACE] and not self.in_air:
            self.in_air = True
            self.update_action(self.JUMP)
            self.jump()
        
        elif key[pygame.K_UP] and self.in_air and self.double_jump:
            self.double_jump = False
            self.update_action(self.DOUBLEJUMP)
            self.higher_jump()
        
        # if nothing is pressed, return to idle position
        if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT] and not key[pygame.K_SPACE] and not key[pygame.K_UP]:
            self.update_action(self.IDLE)

    # jump
    def jump(self):
        self.create_particles(self.rect.midbottom)
        self.direction.y = self.jump_speed
    
    # higher jump
    def higher_jump(self):
        self.create_particles(self.rect.midbottom)
        self.direction.y = self.jump_force

    # run animations
    def run_animations(self):
        if self.action == self.RUN and not self.in_air:
            self.run_frame_index += self.run_frame_rate

            if self.run_frame_index >= len(self.run_particles):
                self.run_frame_index = 0
            
            dust_particle = self.run_particles[int(self.run_frame_index)]

            # check which side to place the dust_particles
            if self.direction.x > 0:
                pos = self.rect.bottomleft - pygame.math.Vector2(6, 10)
                self.screen.blit(dust_particle, pos)
            
            elif self.direction.x < 0:
                pos = self.rect.bottomright - pygame.math.Vector2(6, 10)
                self.screen.blit(dust_particle, pos)

    # updating an action
    def update_action(self, val):
        if val != self.action:
            self.action = val
            self.frame_index = 0
            
            self.animate()

    # update method, everything that should be run continiously is placed here and will be eventually be called in the original while loop
    def update(self):
        self.check_player_name()
        self.get_input()
        self.get_gravity()
        self.animate()
        self.flip_img()
        self.run_animations()