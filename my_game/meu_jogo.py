import pygame
from personagem import Personagem
from pygame.sprite import Group
import sys
from fundo import Fundo
from cenario import Cenario
import random
from arma import Arma, girar_imagem_arma2, update_imagem_boneco
from bullet import Bullet
from mira import Mira
import time
from inimigo import Inimigo , create_inimigo, update_inimigo
import math
from vida import Vida
from button import Button
from score import Score, draw_nivel_player
from tela_inicio import Tela_inicio, Button_play



def run_game():
    
    pygame.init()
    # pygame.mixer.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((1080, 800), flags=pygame.DOUBLEBUF | pygame.SCALED)
    pygame.display.set_caption('mata pombo')
    screen_rect = screen.get_rect()
    # apenas testando criar um surface e deixar ele tranparente
    teste = pygame.Surface((100, 100), pygame.SRCALPHA)
    teste.fill((0, 0, 0, 128))
    
    try:
        pygame.mixer.music.load("sons_jogo/som_fundo.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Erro ao carregar ou tocar a música: {e}")


    my_personagem = Personagem(screen_rect)
    #arma do meu personagem
    imagem_arma = pygame.image.load('imagens/arma_pixel.png')
    #imagem_arma_invertida = pygame.transform.flip(imagem_arma, False, True)
    
    arm = Arma(imagem_arma, my_personagem.rect)
    # imagem que representa a mira
    #global imagem_arma_para_gira
    imagem_arma_para_gira = imagem_arma
    # imagem que representa o tiro 
    imagem_bala = pygame.image.load('imagens/bola_fogo.bmp')
    # redimensiona a imagem da bala
    imagem_bala = pygame.transform.scale(imagem_bala, (5, 5))

    mira = Mira()
    # imagem que representa a vida do jogador
    vida = Vida(screen_rect)

    
    bullet = Bullet(imagem_bala, mira.rect, arm.rect)
 
    # grupo de sprite dos objetos do jogo
    grupo_cenario = Group()
    grupo_bullet = Group()
    grupo_inimigo = Group()
    grupo_personagem = Group()
    grupo_personagem.add(my_personagem)

    # butao de pause
    msg_button = "PLAY"
    button = Button(screen_rect, msg_button)
    color_button = (103, 113, 117)
    

    # objetos do cenario  
    casa_rosa = pygame.image.load('imagens/casa rosa.png')
    pink_house = Cenario(casa_rosa)
    # cria as casas do cenario e as posiciona
    posicao_x = 1100
    posicao_y = 150
    pink_house.rect.center = posicao_x, posicao_y
    grupo_cenario.add(pink_house)
    # sol 
    sun = pygame.image.load('imagens/sol.png')
    sol = Cenario(sun)
    sol.rect.x = sol.rect.width
    sol.rect.y = 0
    grupo_cenario.add(sol)
    # pontuacao do jogador
    score = Score()
    
    cor = (255, 255, 255)  # Verde

# Posição e raio do círculo
    centro = (400, 400)
    raio = 100
    
    #casa_pixel = pygame.image.load('imagens/casa_pixel.png')
    #house_pixel = Cenario(casa_pixel)
    #_posicao_x = random.randint(screen_rect.centerx, 1200)
    #_posicao_y = random.randint(20, 800)
    #house_pixel.rect.center = _posicao_x, _posicao_y
    #grupo_cenario.add(house_pixel)

    global imagem_atual
    imagem_atual = my_personagem.parado_frente
    # boolenas de movimento do personagem
    mover_cima = False
    mover_baixo = False
    mover_esquerda = False
    mover_direita = False   
    # boolenas de disparo 
    #atirar = False
       
    #fundo  = Fundo(screen_rect)

    # boleana para alternar as imagens e dar a impressao que o bone esta dando passos
    alternar_imagem = False
    
    # calcula o tempo para alternar as imagens
    # pega o tempo quando o jogo inicia
    tempo_inicio_game = pygame.time.get_ticks()
    # tempo para alternar as imagens em milisegundos
    tempo_para_alterna_imagens = 100
    # criar o delta time para movimentacao das balas
    last_time = time.time()    
    # pega o tempo quando de quando o jogo iniciou
    tempo_parado = pygame.time.get_ticks()
    # tempo para criar os inimigos
    time_inimigo = 7
    # pegar tempo inicio jogo para calcular o delta time
    tempo_inicial = pygame.time.get_ticks()
       
    #create_inimigo(Inimigo, screen_rect, grupo_inimigo, my_personagem.rect)
    # desenha o surface que representa o ceu 
    ceu_game = pygame.Surface((1280, 200))
    ceu_game.fill((52, 235, 235))
    # desenha o rect que vai a base do inimigo
    #base_inimigo = pygame.Rect(440, 300, 900, 490)
    #color_base = (57, 41, 110)

    # boolena para verificar se o jogo deve pausar ou nao
    # definir ela como global para poder mudar seu valor em outro arquivo
    global game_activate
    game_activate = True
    # butao play da tela de inicio do jogo
    button_play_inicio = Button_play(screen_rect)
    
    # tela de inicio do jogo
    Tela_inicio(screen, screen_rect, button_play_inicio, ceu_game, grupo_cenario, my_personagem)           
  
    while True:
        
        arma = Arma(imagem_arma, my_personagem.rect)
        # pega o delta time para mover os projeteis de acordo com a velocidade do frame
        current_time = time.time()
        delta_time = current_time - last_time
        last_time = current_time
        # trocar imagem do personagem de acordo pra onde esta a mira 
        mover_por_angulo = False
        # pegar o tempo atual para calcular o delta time
        tempo_atualmente = pygame.time.get_ticks()
        delta_time = (tempo_atualmente - tempo_inicial) / 1000.0
        tempo_inicial = tempo_atualmente
                        
        # pega o tempo atual desde o inicio do jogo
        tempo_atual = pygame.time.get_ticks()
        
        # logica de movimento do personagem
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()

            elif event.type == pygame.KEYDOWN:
                # se o jogador apertar spaço o jogo pausa
                if event.key == pygame.K_SPACE:
                    game_activate = False

                if event.key == pygame.K_w :
                    mover_cima = True
                
                elif event.key == pygame.K_s :
                    mover_baixo = True
                
                elif event.key == pygame.K_a :
                    mover_esquerda = True
                

                elif event.key == pygame.K_d:
                    mover_direita = True
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button.rect.collidepoint(mouse_x, mouse_y):
                    game_activate = True
                    Inimigo.time_up_velo = time.time()
                new_bullet = Bullet(imagem_bala, mira.rect, arma.rect)
                
                new_bullet.rect.center = arma.rect.center
                new_bullet.pos_mira_atual_x, new_bullet.pos_mira_atual_y = mira.rect.center
                new_bullet.pos_inicial_bala_x, new_bullet.pos_inicial_bala_y = new_bullet.rect.center
                grupo_bullet.add(new_bullet)
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    imagem_atual = my_personagem.parado_costa
                    mover_cima = False
                                        
                elif event.key == pygame.K_s:
                    imagem_atual = my_personagem.parado_frente
                    mover_baixo = False                   
                
                elif event.key == pygame.K_a:
                    imagem_atual = my_personagem.parado_esquerda
                    mover_esquerda = False                    

                elif event.key == pygame.K_d:
                    imagem_atual = my_personagem.parado_direita                  
                    mover_direita = False

        if  not game_activate:
            # se o jogo for pausado
            # escode o cursor do mouse
            # desenha o butao de pause e a mensagem
            pygame.mouse.set_visible(True)
            pygame.draw.rect(screen, color_button, button.rect)
            screen.blit(button.prep_msg, button.msg_rect)
            # tempo para criar os inimigos recebe o tempo atual para nao criar inimigos assim que o jogo for despausado
            tempo_parado = time.time()

        if game_activate:
            pygame.mouse.set_visible(False)

            # pega o tempo atual
            tempo_agora = time.time()
            # cria inimigos a cada  determinada quantidade de segundos
            if (tempo_agora - tempo_parado) >= time_inimigo: 
                create_inimigo(Inimigo, screen_rect, grupo_inimigo, my_personagem.rect)
                tempo_parado = tempo_agora

            if  mover_cima and my_personagem.rect.top >= screen_rect.top:                  
                my_personagem.rect.top -= my_personagem.speed
                imagem_atual = my_personagem.andando_costa_direito
                alternar_imagem = True

            if mover_baixo and my_personagem.rect.bottom <= screen_rect.bottom:
                    my_personagem.rect.bottom += my_personagem.speed
                    imagem_atual = my_personagem.andando_frente_direito
                    alternar_imagem = True

            if mover_esquerda and my_personagem.rect.left >= 0:
                my_personagem.rect.x -= my_personagem.speed
                imagem_atual = my_personagem.andando_esquerda_direito
                alternar_imagem = True
                
            if  mover_direita and my_personagem.rect.right <= screen_rect.right:                        
                my_personagem.rect.x += my_personagem.speed
                imagem_atual = my_personagem.andando_direita_direito
                alternar_imagem = True

            # se o personagem nao tiver em movimento, permite que ele vira para o lado que esta a mira 
            if mover_cima == False and mover_baixo == False:
                if mover_esquerda == False and mover_direita == False:
                    mover_por_angulo = True

            # se o personagem colidir com alguma casa ele é impedido de andar
            if pygame.sprite.spritecollideany(my_personagem, grupo_cenario):
                mover_baixo = False
                mover_cima = False
                mover_direita = False
                mover_esquerda =  False

            # calcula se ta na hora de alternar as imagens, para dar impressao que o personagem esta dando passos
            if alternar_imagem and (tempo_atual -  tempo_inicio_game >= tempo_para_alterna_imagens):
                if mover_cima:
                    imagem_atual = my_personagem.andando_costa_esquerdo              

                elif mover_baixo:
                    imagem_atual = my_personagem.andando_frente_esquerdo
                                
                elif mover_esquerda:
                    imagem_atual = my_personagem.andando_esquerda_esquerdo
                                    
                elif mover_direita:
                    imagem_atual = my_personagem.andando_direita_esquerdo


                tempo_inicio_game = tempo_atual  # Atualiza o tempo da última mudança de imagem
                alternar_imagem = False
                        
            
            pygame.draw.circle(screen, cor, centro, raio)
            # "pinta" a tela a cada passadgem pelo laço 
            screen.fill((52, 235, 88))
            screen.blit(teste, (screen_rect.left, screen_rect.bottom - 100))
            # desenha o ceu 
            screen.blit(ceu_game, (screen_rect.left, screen_rect.top))
            #pygame.draw.rect(screen, color_base, base_inimigo)
            #fundo.draw_fundo(screen)       

            # verifica se acabaram as vidas e reinicia o jogo          
            vida.check_died(grupo_inimigo, grupo_bullet, my_personagem.rect, screen_rect, score, Inimigo)
            # quando o personagem colidir com o inimigo terá alguns segundos imortal
            vida.check_vida(grupo_personagem, grupo_inimigo, screen)
            # desenha a imagem que representa a vida
            vida.draw_vida(screen)
            # desenha a arma do personagem
            #arma = Arma(imagem_arma, my_personagem.rect)                 
            # gira a arma para acompanhar o movimento da mira 
            imagem_arma, angulo_graus = girar_imagem_arma2(my_personagem.rect, mira.rect, imagem_arma_para_gira, arma.rect)
            #imagem_arma = check_arma_angulo(arma, my_personagem.rect, angulo_graus)
            #print(my_personagem.rect.top)            
            # desenha as balas presentes no grupo de sprite
            grupo_bullet.draw(screen)
            # atualiza a posicao da bala a cada frame
            bullet.update_bullets(grupo_bullet, screen_rect, delta_time, angulo_graus)
            #print(len(grupo_bullet))
            mira.draw_mira(screen)
            update_inimigo(grupo_inimigo, my_personagem.rect, delta_time)
            #Inimigo.up_velo_inimigo()
            #update_imagem_boneco(my_personagem, angulo_graus, alternar_imagem)
            # criar um dicionario com a bala que atingiu o inimigo(chave) e uma lista dos inimigos atingidos por ela(valor)
            # ambos desaparecem ao colidirem
            collisions = pygame.sprite.groupcollide(grupo_bullet, grupo_inimigo, True, True)
            #desenha a pontuacao do jogador na tela
            score.draw_score(screen, collisions, screen_rect)
            # desenha a pontuacao maxima(record) do jogador
            score.draw_max_score(screen, screen_rect)
            # desenha o nivel do jogador
            draw_nivel_player(screen, screen_rect)
            # so será verificado se o jogador alcançou um novo record quando ele perder todas as vidas
            if vida.total_vidas == 0:     
                score.check_max_score()      
            # se todos as booleanas de movimento de personagem for false "mover_por_angulo" será True
            if mover_por_angulo:
                imagem_atual = update_imagem_boneco(my_personagem, angulo_graus)
            
            # aqui verifica se mira/arma esta em algum angulo a direita do personagem        
            if angulo_graus >= -100 and angulo_graus <= 100:
                #se a mira/arma estiverem a direita ela será desenhada por cima do personagem 
                screen.blit(imagem_atual, my_personagem.rect)
                arma.draw_arma(screen)
            
            else:    
                # se nao tiver a direita a arma sera desenhada por traz do personagem        
                arma.draw_arma(screen)
                screen.blit(imagem_atual, my_personagem.rect)

            # desenha todos os inimigos que estao no grupo de sprites
            grupo_inimigo.draw(screen)       
            # desenha todas as casas que estao no grupo de casas
            grupo_cenario.draw(screen)
            # se todos os inimigos forem mortos outros sao criados imediatamente
            #if len(grupo_inimigo) == 0:
                #create_inimigo(Inimigo, screen_rect, grupo_inimigo, my_personagem.rect)
            
            # se o projetil atingir uma casa ele desaparece
            colisao = pygame.sprite.groupcollide(grupo_bullet, grupo_cenario, True, False)           
        
        pygame.display.flip()
        clock.tick(30) # define o quanto frames por segundo terá o game

            
run_game()
