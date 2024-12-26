import pygame
from pygame.sprite import Sprite
import math


class Arma(Sprite):
    def __init__(self, imagem_arma, personagem_rect):
        super().__init__()

        self.image = imagem_arma
        #personagem_rect.left,personagem_rect.top + 25
        self.rect = self.image.get_rect()
        self.rect.left = personagem_rect.centerx - 15
        self.rect.top = personagem_rect.centery 

    def draw_arma(self, screen):
              
        screen.blit(self.image, self.rect)




    
   # if angulo_graus >= -145 and angulo_graus <= -45:
    #     centro_x, centro_y = arma_rect.centerx, arma_rect.bottom
    # elif angulo_graus <= 140 and angulo_graus >= 25:
    #     centro_x, centro_y = arma_rect.centerx, arma_rect.top
    # elif  angulo_graus >= -145 and angulo_graus <= 140:
    #     centro_x, centro_y = arma_rect.left, arma_rect.centery
    # else:
    #     centro_x, centro_x = personagem_rect.center   




angulo_grau_help = 0

def girar_imagem_arma2(personagem_rect, mira_rect, imagem_arma, arma_rect):
    global angulo_grau_help
    # Calcular o centro do personagem 
    centro_x, centro_y = personagem_rect.center
    mouse_x, mouse_y = mira_rect.center
    if angulo_grau_help <= - 10 and angulo_grau_help >= -178:
        arma_rect.bottom = personagem_rect.bottom
    
    #elif angulo_grau_help >= -145 and angulo_grau_help <= -45:
    # Calcular o vetor e o ângulo
    vetor_x = mouse_x - centro_x
    vetor_y = mouse_y - centro_y
    angulo_rad = math.atan2(vetor_y, vetor_x)
    
    angulo_graus = math.degrees(angulo_rad)
    angulo_grau_help = angulo_graus
    #print(angulo_graus)
    
    if angulo_graus <= -130 or angulo_graus >= 90:       
        imagem_arma = pygame.transform.flip(imagem_arma, False, True)
        arma_rect.midright = personagem_rect.midright
        
    else:
        imagem_arma = pygame.image.load('imagens/arma_pixel.png')

    
    imagem_girada = pygame.transform.rotate(imagem_arma, -angulo_graus)
   
    return imagem_girada, angulo_graus
   

    


def update_imagem_boneco(my_personagem, angulo_graus):
   
    
        
        if angulo_graus >= -145 and angulo_graus <= -45 :
            nova_imagem = my_personagem.parado_costa
            return nova_imagem
            
        elif angulo_graus <= 140 and angulo_graus >= 25 :
            nova_imagem = my_personagem.parado_frente
            return nova_imagem
            
        elif angulo_graus >= -145 and angulo_graus <= 140 :
            nova_imagem = my_personagem.parado_direita
            return nova_imagem
            
        else :
            nova_imagem = my_personagem.parado_esquerda
            return nova_imagem
    
    





# def check_arma_angulo(arma, personagem_rect, angulo_graus):
#     # verifica se a mira esta em algum angulo a esquerdo do personagem 
#     # se tiver muda para uma imagem da arma invertida para que ela nao fique de cabeça pra baixo 
   
#     if angulo_graus <= -130 or angulo_graus >= 90:       
#         imagem_arma_angulo = pygame.image.load('imagens/arma_pixel_copia.png')
#         arma.rect.right = personagem_rect.right

        
#     else:
#         imagem_arma_angulo = pygame.image.load('imagens/arma_pixel.png')
    

#     return imagem_arma_angulo


