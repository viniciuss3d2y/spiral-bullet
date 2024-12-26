import pygame
import sys


# class Surface_inicio():
#     def __init__(self, screen_rect):
#         self.surface = pygame.Surface((600, 350), pygame.SRCALPHA)
#         self.surface.fill((165, 173, 172, 150))
#         self.rect = self.surface.get_rect()
#         self.rect.center = screen_rect.center

class Button_play():
    
    def __init__(self, screen_rect):
        # imagem botao normal
        self.image = pygame.image.load('imagens/button_play.png')
        # imagem do botao com efeito de click so vai ser desenhada quando o cursor do mouse etiver em cima 
        self.image2 = pygame.image.load('imagens/button_click.png')
        # o valor desta variavel de instancia vai ficar alternando entre "self.image" e "self.image2"
        self.imagem_para_desenhar = self.image
        self.rect = self.imagem_para_desenhar.get_rect()
        self.rect.center = screen_rect.center
        # cria o objeto surface ; argumento 'pygame.SRCALPHA' para definir que o surface pode suportar trasnparencia
        self.surface = pygame.Surface((1280, 800), pygame.SRCALPHA)
        self.surface.fill((250, 250, 250, 128)) # aqui o quarto valor define a transparencia(0 até 255)
        self.sur_rect = self.surface.get_rect()
        self.sur_rect.center = screen_rect.center

# bopleana para manter a tela ativa
tela_inicio_ativa = True
def Tela_inicio(screen, screen_rect, button_play, ceu_game, grupo_cenario, persongem):
    # torna a variavel no escopo global para que seu valor possa ser alterado de dentro da funcao   
    global tela_inicio_ativa

    while tela_inicio_ativa:   
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            eixo_x, eixo_y = pygame.mouse.get_pos()
            if button_play.rect.collidepoint(eixo_x, eixo_y):
                button_play.imagem_para_desenhar = button_play.image2
                
                if event.type == pygame.MOUSEBUTTONDOWN:                                  
                    tela_inicio_ativa = False
                    
                    pygame.time.wait(2000)      
           
            else:
                button_play.imagem_para_desenhar = button_play.image
        
        # pinta a tela
        screen.fill((52, 235, 88))
        button_play.surface.fill((250, 250, 250, 128))
        # desenha o 'céu'   
        screen.blit(ceu_game, (screen_rect.x, screen_rect.top))
        # desenha todos os objetos do cenario presentes no grupo de sprites 
        grupo_cenario.draw(screen)   
        # desenha o personagem 
        screen.blit(persongem.parado_frente, (screen_rect.centerx, screen_rect.centery + 20)) 
        # desenha o botao de play 
        button_play.surface.blit(button_play.imagem_para_desenhar, button_play.rect)
        # desenha o surface por cima da tela
        screen.blit(button_play.surface, button_play.sur_rect)
        pygame.display.flip()
        