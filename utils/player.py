import pygame
from utils.support import import_sprite_sheet

# class for the player, all the functionality of the player will be here


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, char="Virtual Guy"):
        super().__init__()
        self.pos = pos
        self.char = char

        # character stuff
        self.gravity = 1
        self.scale = (50, 50)
        self.scrollY = 0
        self.jump_speed = -19
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.in_air = True

        # animations
        self.animation = []
        self.flip = False
        self.get_imgs()

        self.IDLE = 0
        self.JUMP = 1
        self.RUN = 2
        self.FALL = 3

        self.action = 0

        self.frame_index = 0
        self.frame_rate = 0.25

        self.image = self.animation[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    # animating
    def animate(self):
        self.frame_index += self.frame_rate

        if self.frame_index >= len(self.animation[self.action]):
            self.frame_index = 0

        self.image = self.animation[self.action][int(self.frame_index)]

    # flipping the image
    def flip_img(self):
        self.image = pygame.transform.flip(self.image, self.flip, False)

    # getting gravity
    def get_gravity(self):
        if self.in_air:
            self.direction.y += self.gravity
        else:
            self.direction.y = 0

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

        self.animation.append(idle)
        self.animation.append(jump)
        self.animation.append(run)
        self.animation.append(fall)

    # getting input from the user
    def get_input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_RIGHT]:
            self.direction.x = 1
            self.flip = False
            self.update_action(self.RUN)
        
        elif key[pygame.K_LEFT]:
            self.direction.x = -1
            self.flip = True
            self.update_action(self.RUN)
            
        else:
            self.direction.x = 0

        
        if key[pygame.K_SPACE] and not self.in_air:
            self.in_air = True
            self.jump()
        
        if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT] and not key[pygame.K_SPACE]:
            self.update_action(self.IDLE)

    # jump
    def jump(self):
        self.direction.y = self.jump_speed

    # updating an action
    def update_action(self, val):
        if val != self.action:
            self.action = val
            self.frame_index = 0
            
            self.animate()

    def update(self):
        self.get_input()
        self.animate()
        self.flip_img()