import os
import pygame


class Carrier(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.width, self.height = 47, 187
        sprite_image = pygame.image.load(os.path.join(
            'assets', 'ships', 'carrier', 'carrier.png'))
        self.image = pygame.transform.scale(
            sprite_image, (self.width, self.height))

        self.life = None
        self.rect = self.image.get_rect()

