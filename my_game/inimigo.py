import pygame
from pygame.sprite import  Sprite
import random
import math
import time



 
class Inimigo(Sprite):
   # variavel de classe
    qtd_inimigo = 8
    velocidade = 100
    def __init__(self):
        super().__init__()
        # variaveis de instancia
        self.image = pygame.image.load('imagens/inimigoG.png')
        self.rect = self.image.get_rect()

        self.pos_personagem_x = 0
        self.pos_personagem_y = 0

        self.pos_inicial_x = 0
        self.pos_inicial_y = 0

    
    

# tempo para aumentar a velocidade do inimigo   
   
# aumenta a velociade do inimigo a cada N segundos
tempo_aumentar_velo = 12
time_up_velo = time.time()

def create_inimigo(Inimigo_class, screen_rect, grupo_inimigos, rect_personagem):
    global tempo_aumentar_velo
    #global time_up_velo
    # a cada {tempo_aumentar_velo} a velocidade dos inimigos aumenta
    if int(time.time() - time_up_velo) >= tempo_aumentar_velo:
            Inimigo_class.velocidade += tempo_aumentar_velo * 0.85
            
    print(Inimigo_class.velocidade)
    # cria a quantidade de inimigos definica em "Inimigo_class.qtd_inimigo"
    for i in range(Inimigo_class.qtd_inimigo):       
        posicao_x = random.randint(30, 1150)
        posicao_y = random.randint(20, 800)
        new_inimigo = Inimigo_class()
        new_inimigo.rect.bottom = screen_rect.bottom
        new_inimigo.rect.x = posicao_x
        
           
        if i >= 2 and  i < 5 :
            new_inimigo.rect.top = screen_rect.top
            new_inimigo.rect.x = posicao_x
        
        elif i >= 5 and i < 7:
            new_inimigo.rect.y = posicao_y
            new_inimigo.rect.x = screen_rect.left
        
        else:
            new_inimigo.rect.y = posicao_y
            new_inimigo.rect.x = screen_rect.right
        
            
        # new_inimigo.pos_personagem_x, new_inimigo.pos_personagem_y = rect_personagem.center
        # new_inimigo.pos_inicial_x, new_inimigo.pos_inicial_y = new_inimigo.rect.center
        
        grupo_inimigos.add(new_inimigo)






def update_inimigo(grupo_inimigo, personagem_rect, delta_time):
    #delta_time = 0.03
    
    for inimigo in grupo_inimigo:       
        
        # inimigo.rect.x =  inimigo.rect.x + (personagem_rect.x - inimigo.rect.x) * delta_time
        # inimigo.rect.y =  inimigo.rect.y + (personagem_rect.y - inimigo.rect.y) * delta_time

        # Calcula o vetor
        vetor_x = personagem_rect.x - inimigo.rect.x
        vetor_y = personagem_rect.y - inimigo.rect.y
    
        # Calcula a magnitude (distância) do vetor
        magnitude = math.sqrt(vetor_x**2 + vetor_y**2)
        
        if magnitude > 0:  # Garante que magnitude não seja zero para evitar problemas de divisão
            # Normaliza os vetores
            vetor_x /= magnitude
            vetor_y /= magnitude
            
            # Atualiza a posição do inimigo
            inimigo.rect.x += vetor_x * inimigo.velocidade * delta_time
            inimigo.rect.y += vetor_y * inimigo.velocidade * delta_time

        
 
 
 
