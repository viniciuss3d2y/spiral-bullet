import pygame
from pygame.sprite import Sprite

class Personagem(Sprite):
    def __init__(self, screen_rect):
        super().__init__()
        # personagem subindo na  tela
        self.andando_costa_direito = pygame.image.load('imagens/andando costa pé direito.png')
        self.andando_costa_esquerdo = pygame.image.load('imagens/andando costa pé esquerdo.png')
        self.parado_costa = pygame.image.load('imagens/parado costa.png')
        # personagem indo pra direita da  tela
        self.andando_direita_esquerdo = pygame.image.load('imagens/andando direita pé esquerdo.png')
        self.andando_direita_direito = pygame.image.load('imagens/andando direita pé direito.png')
        self.parado_direita = pygame.image.load('imagens/parado direita.png')
        # personagem indo pra esquerda da tala
        self.andando_esquerda_direito = pygame.image.load('imagens/andando esquerda pé direito.png')
        self.andando_esquerda_esquerdo = pygame.image.load('imagens/andando esquerda pé esquerdo.png')
        self.parado_esquerda = pygame.image.load('imagens/parado esquerda.png')
        # persongem descendo na tela 
        self.andando_frente_direito = pygame.image.load('imagens/andando frente pé direito.png')
        self.andando_frente_esquerdo = pygame.image.load('imagens/andando frente pé esquerdo.png')
        self.parado_frente = pygame.image.load('imagens/parado frente.png')

        # rect para mover as imagens
        self.rect = pygame.Rect(screen_rect.center[0], screen_rect.center[1], 24, 40)
        
        self.speed = 5