import pygame

class Fundo():
    def __init__(self, screen_rect) :
        self.image = pygame.image.load('imagens/fundo_game.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
    

    def draw_fundo(self, screen):
        screen.blit(self.image, self.rect)
