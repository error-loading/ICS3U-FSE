import pygame
from utils.support import import_sprite_sheet
from utils.particles import Particles
from constants import *

# class for the player, all the functionality of the player will be here
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen, create_particles, char="Virtual Guy"):
        super().__init__()
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
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.in_air = True
        self.double_jump = True

        # animations
        self.animation = []
        self.flip = False

        # particles
        self.run_particles = []

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

        self.action = 0

        self.frame_index = 0
        self.frame_rate = 0.25

        self.run_frame_index = 0
        self.run_frame_rate = 0.15

        self.image = self.animation[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(pos[0] - self.image.get_width() // 2, pos[1]))

    # animating
    def animate(self):
        self.frame_index += self.frame_rate

        if self.frame_index >= len(self.animation[self.action]):
            if self.action == self.HIT or self.action == self.JUMP or self.action == self.DOUBLEJUMP:
                if self.action == self.DOUBLEJUMP: self.action = self.JUMP
                self.frame_index = len(self.animation[self.action]) - 1
            
            else:
                self.frame_index = 0

        self.image = self.animation[self.action][int(self.frame_index)]
    
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
        idle = import_sprite_sheet(
            f"assets/character/{self.char}/idle.png", (32, 32), self.scale)
        jump = import_sprite_sheet(
            f"assets/character/{self.char}/jump.png", (32, 32), self.scale)
        run = import_sprite_sheet(
            f"assets/character/{self.char}/run.png", (32, 32), self.scale)
        fall = import_sprite_sheet(
            f"assets/character/{self.char}/fall.png", (32, 32), self.scale)
        hit = import_sprite_sheet(
            f"assets/character/{self.char}/hit.png", (32, 32), self.scale)
        wall = import_sprite_sheet(
            f"assets/character/{self.char}/wall.png", (32, 32), self.scale)
        doublejump = import_sprite_sheet(
            f"assets/character/{self.char}/doublejump.png", (32, 32), self.scale)
        
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

    def update(self):
        self.get_input()
        self.get_gravity()
        self.animate()
        self.flip_img()
        self.run_animations()