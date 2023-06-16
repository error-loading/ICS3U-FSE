import pygame

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        self.display_sur  = pygame.display.get_surface()
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pass
            
        if keys[pygame.K_RIGHT]:
            pass

        if keys[pygame.K_SPACE]:
            pass

    
    def display(self):
        self.display_sur.fill("BLACK")