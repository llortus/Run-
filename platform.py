import pygame
import random
import state
import level
import surface_manager

class Platform(pygame.sprite.Sprite):
    def __init__(self, img_location):
        super(Platform, self).__init__()
        self.display = pygame.display.get_surface()
        self.surface_manager = surface_manager
        self.image = pygame.image.load(img_location).convert_alpha()
        self.image = pygame.transform.scale(self.image, (random.randint(100, 1000), self.image.get_height()))
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.pos_x = self.display.get_width()
        self.pos_y = random.randint(self.display.get_height() - self.rect.height*5, self.display.get_height() - self.rect.height)

    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)
            return
        else:
            self.pos_x -= 12

            self.rect.topleft = (self.pos_x, self.pos_y)

class StartingPlatform(pygame.sprite.Sprite):
    def __init__(self, img_location):
        super(StartingPlatform, self).__init__()
        self.display = pygame.display.get_surface()
        self.image = pygame.image.load(img_location).convert_alpha()
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.pos_x = 0
        self.pos_y = self.display.get_height() - 100

    def update(self):
        if self.pos_x < 0 - self.rect.width:
            surface_manager.remove(self)
            return
        else:
            self.pos_x -= 12

            self.rect.topleft = (self.pos_x, self.pos_y)