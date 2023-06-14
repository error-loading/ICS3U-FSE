import pygame
from utils.support import import_sprite_sheet
from utils.particles import Particles

# class for the player, all the functionality of the player will be here
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen, limit, char="Samurai"):
        super().__init__()
        self.pos = pos
        self.char = char
        self.screen = screen
        self.limit = limit

        # character stuff
        self.scale = (32, 32)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3

        # animations
        self.animation = []
        self.flip = False

        self.get_imgs()

        # states
        self.IDLE = 0
        self.DOWN = 1
        self.UP = 2
        self.LEFT = 3
        self.RIGHT = 4

        self.idle = False
        self.action = 0

        self.frame_index = 0
        self.frame_rate = 0.15

        self.image = self.animation[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(pos[0] - self.image.get_width() // 2, pos[1]))

    # animating
    def animate(self):
        if not self.idle:
            self.frame_index += self.frame_rate

            if self.frame_index >= len(self.animation[self.action]):
                self.frame_index = 0

            self.image = self.animation[self.action][int(self.frame_index)]
        
        else:
            self.image = self.animation[self.IDLE][self.action - 1]
    
    # check
    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.limit:
                if sprite.rect.colliderect(self.rect):
                    # moving right
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    # moving left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == "vertical":
            for sprite in self.limit:
                if sprite.rect.colliderect(self.rect):
                    # moving down
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    # moving up
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
            

        
        

    # flipping the image
    def flip_img(self):
        self.image = pygame.transform.flip(self.image, self.flip, False)


    # getting imgs
    def get_imgs(self):
        idle = import_sprite_sheet(
            f"assets/overworld/Characters/{self.char}/SeparateAnim/Idle.png", (16, 16), self.scale)
        move = import_sprite_sheet(
            f"assets/overworld/Characters/{self.char}/SeparateAnim/Walk.png", (16, 16), self.scale)

        row = 4
        
        self.animation.append(idle)

        for k in range(0, row):
            temp = []
            for i in range(k, len(move), row):
                temp.append(move[i])
            
            self.animation.append(temp)




    # getting input from the user
    def get_input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_RIGHT]:
            self.direction.x = 1
            self.idle = False
            self.update_action(self.RIGHT)
        
        elif key[pygame.K_LEFT]:
            self.direction.x = -1
            self.idle = False
            self.update_action(self.LEFT)
        
        elif key[pygame.K_UP]:
            self.direction.y = -1
            self.idle = False
            self.update_action(self.UP)
        
        elif key[pygame.K_DOWN]:
            self.direction.y = 1
            self.idle = False
            self.update_action(self.DOWN)
            
        else:
            self.direction.x = 0
            self.direction.y = 0
            self.idle = True

        
        if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT] and not key[pygame.K_UP] and not key[pygame.K_DOWN]:
            self.direction.x = 0
            self.direction.y = 0 
            self.idle = False

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * speed
        self.collision("horizontal")
        self.rect.y += self.direction.y * speed 
        self.collision("vertical")


    # updating an action
    def update_action(self, val):
        if val != self.action:
            self.action = val
            self.frame_index = 0
            
            self.animate()

    def update(self):
        self.get_input()
        self.animate()
        self.move(self.speed)
        self.flip_img()
