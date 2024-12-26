import pygame
from time import time




class loopinterrompido(Exception):
    pass  




class Vida():
    def __init__(self, screen_rect):
       
   
        # imagens da vida do player
       self.vida_cheia = pygame.image.load('imagens/vida_cheia.png')
       self.vida_menos_um = pygame.image.load('imagens/vida-1.png')
       self.vida_menos_dois = pygame.image.load('imagens/vida-2.png')
       self.vida_menos_tres = pygame.image.load('imagens/vida-3.png')
       self.vida_menos_quatro = pygame.image.load('imagens/vida-4.png')
       self.vida_menos_cinco = pygame.image.load('imagens/vida-5.png')
       
       
       self.image = self.vida_cheia
       self.rect = self.image.get_rect()

       self.rect.top = screen_rect.top + 10
       self.rect.right = screen_rect.right - 50

       self.total_vidas = 5
        # tem po para para auxiliar nas colisoes dos inimigos e personagem
        # para que a vida nao esvazie imediatamente com a colisao
       self.tempo_colisao = time()

       # imagem que vai aparecer quando o player perder uma vida
       self.menos_vida = pygame.image.load('imagens/perde_vida.png')
       self.menos_vida = pygame.transform.scale(self.menos_vida, (70, 70))
       self.menos_vida_rect = self.menos_vida.get_rect()
       self.menos_vida_rect.center = screen_rect.center
       
       self.time_draw_menos_vida = 1
       self.draw_menos_vida = False

    
    
    def check_vida(self,grupo_personagem, grupo_inimigos, screen):
        tempo_atual = time()
        

        if int(tempo_atual) - int(self.tempo_colisao) >= 2:      
            collisions = pygame.sprite.groupcollide(grupo_personagem, grupo_inimigos, False, False)

            for chave in collisions:
                self.total_vidas -= 1
                self.tempo_colisao = tempo_atual
                self.time_draw_menos_vida = time()
        
        if int(time()) - int(self.time_draw_menos_vida) <= 1 :
            screen.blit(self.menos_vida, self.menos_vida_rect) 

    
    def draw_vida(self, screen):
        if self.total_vidas == 5:
            screen.blit(self.vida_cheia, self.rect)
        elif self.total_vidas == 4:
            screen.blit(self.vida_menos_um, self.rect)
        elif self.total_vidas == 3 :
            screen.blit(self.vida_menos_dois, self.rect)
        elif self.total_vidas == 2 :
            screen.blit(self.vida_menos_tres, self.rect)
        elif self.total_vidas == 1 :
            screen.blit(self.vida_menos_quatro, self.rect)
        elif self.total_vidas <= 0:
            screen.blit(self.vida_menos_cinco, self.rect)
            pygame.time.wait(2000)
                                            
    

    def check_died(self, grupo_inimigos, grupo_bullets, personagem_rect, screen_rect, score, Inimigo):
        import meu_jogo

        if self.total_vidas <= 0:
            meu_jogo.game_activate = False
            grupo_bullets.empty()
            grupo_inimigos.empty()
            personagem_rect.center = screen_rect.center
            self.total_vidas = 5
            # se o jogador morrer soma o xp que ele ganhou nesta partida com o seu nivel 
            with open('nivel_player.py', 'r') as arquivo:
                conteudo = arquivo.read()
            # soma o xp ganho na partida com o nivel
            novo_nivel = float(conteudo) + score.nivel_player
            with open('nivel_player.py', 'w') as arquivinho:
                arquivinho.write(str(novo_nivel))
            # se o jogador morrer sua pontuaçao zera
            score.score = 0
            # o xp adiquirido nesta parida tambem é zerados após ser adicionado ao seu nivel
            score.nivel_player = 0
            # velociade do inimigo é ajustada para seu valor inicial
            Inimigo.velocidade = 100
            

            



