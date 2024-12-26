import pygame
from pygame.sprite import Sprite
import math

class Bullet(Sprite):
    def __init__(self, imagem_bala, mira_rect, bullet_rect):
        super().__init__()

        self.image = imagem_bala
        self.rect = self.image.get_rect()

        self.pos_mira_atual_x, self.pos_mira_atual_y = mira_rect.center
        self.pos_inicial_bala_x, self.pos_inicial_bala_y = bullet_rect.center
        
        self.velocidade = 200
       



    def update_bullets(self, group_bullets, screen_rect, delta_time, angulo_graus):
        for bala in group_bullets:
            # Atualizar o tempo decorrido

            # bala.rect.x +=  (bala.pos - )  * delta_time
            # bala.rect.y +=  (bala.pos_mira_atual_y - bala.pos_inicial_bala_y)  * delta_time      
            vetor_x = (bala.pos_mira_atual_x - bala.pos_inicial_bala_x) 
            vetor_y = (bala.pos_mira_atual_y - bala.pos_inicial_bala_y)

            magnitude = math.sqrt(vetor_x**2 + vetor_y**2)

            if magnitude != 0:
                
                vetor_x /= magnitude
                vetor_y /= magnitude
            
                bala.rect.x += vetor_x * bala.velocidade * delta_time
                bala.rect.y += vetor_y * bala.velocidade * delta_time




            if bala.rect.right >= screen_rect.right or bala.rect.bottom >= screen_rect.bottom:
                group_bullets.remove(bala)
            
            if bala.rect.top <= 0 or bala.rect.left <= 0:
                group_bullets.remove(bala)
            
            

