import pygame
from pygame.sprite import  Sprite
import math


class Mira(Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('imagens/mira_menor.png')
        self.rect  = self.image.get_rect()
        
    
    def draw_mira(self, screen):       
        # pega a posicao x e y do cursor do mouse 
        mouse_x, mouse_y =  pygame.mouse.get_pos()
        # o centro da mira ficará exatamente onde o cursor estiver 
        self.rect.center = mouse_x, mouse_y
        # desenha a mira
        screen.blit(self.image, self.rect)


