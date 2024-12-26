import pygame 
from pygame.sprite import Sprite


class Button(Sprite):
    def __init__(self, screen_rect, msg):

        self.rect = pygame.Rect(0, 0 , screen_rect.right // 18, screen_rect.bottom // 18)
        self.rect.center = screen_rect.center
        self.rect.top += 50
        self.font = pygame.font.SysFont('Pixel Emulator', 10)
        self.color = 255, 255, 255
        self.prep_msg = self.font.render(msg, True, self.color)

        self.msg_rect = self.prep_msg.get_rect()
        self.msg_rect.center = self.rect.center