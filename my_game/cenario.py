import pygame
from pygame.sprite import Sprite


class Cenario(Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
