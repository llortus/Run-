import pygame
import level
import surface_manager

class Projectile(pygame.sprite.DirtySprite):
    def __init__(self, player):
        super(Projectile, self).__init__()
        self.display = pygame.display.get_surface()
        self.image = pygame.image.load("data/images/shuriken.png").convert_alpha()
        self.rect = pygame.Rect((0, 0), (self.image.get_width(), self.image.get_height()))
        self.pos_x = player.pos_x + player.rect.width
        self.pos_y = player.pos_y + 50
        self.velocity = 8
        self.dirty = 1

    def update(self):
        if self.pos_x > self.display.get_width():
            surface_manager.remove(self)
        self.pos_x += self.velocity

        self.rect.topleft = (self.pos_x, self.pos_y)
        self.dirty = 1