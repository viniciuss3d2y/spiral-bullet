import pygame


class Score():
    def __init__(self):

        self.font = pygame.font.SysFont('Pixel Emulator', 15)
        self.score = 0     
        self.color_msg = (137, 135, 140)

        self.nivel_player = float(0)


    def draw_score(self, screen, collisions, screen_rect):
        # itera sobre cada inimigo atingido dentro da lista aninhada 
        for valor in collisions.values():
            for inimigo in valor:
                # pra cada inimigo atingido o jogador soma +25 na sua pontuacao
                self.score += 25
                # pra cada inimigo atingido o jogador ganha xp 
                self.nivel_player += 0.01
                

        # transforma o valor de self.score em string para poder desenhalo na tela
        msg = "{:,}".format(self.score)

        prep_msg = self.font.render(msg, True, self.color_msg)
        rect = prep_msg.get_rect()

        rect.top = screen_rect.top
        rect.centerx = screen_rect.centerx

        screen.blit(prep_msg, rect)

        

    def draw_max_score(self,screen, screen_rect):
        # pega a pontuacao maxima do jogador presente no arquivo 'max_score.py'
        with open('max_score.py', 'r') as arquivo:
            conteudo = arquivo.read()
        # formata a pontuacao em string para poder desenhala na tela
        msg = f'record : {"{:,}".format(int(float(conteudo)))}'
        prep_msg = self.font.render(msg, True, self.color_msg)

        rect = prep_msg.get_rect()
        rect.top = screen_rect.top
        rect.right = screen_rect.right - 5

        screen.blit(prep_msg, rect)


    def check_max_score(self):
         # de novo pega a pontuacao maxima do jogador presente no arquivo 'max_score.py'
        with open('max_score.py', 'r') as arquivo :
            conteudo = arquivo.read()
        # verifica se a pontuacao feita pelo jogador nesta partida foi maior que seu antigo record
        if self.score > int(float(conteudo)):
            # se sua pontucao feita agora foi maior que o seu entao record; o seu antigo record da lugar ao seu novo record
            with open('max_score.py', 'w') as arquivao:
                arquivao.write(str(self.score))
    




def draw_nivel_player(screen, screen_rect):
    # pega seu nivel atual presente no arquivo 'nivel_player.py'
    with open('nivel_player.py', 'r') as arquivo:
        conteudo = arquivo.read()
    
    font = pygame.font.SysFont('Pixel Emulator', 7)
    msg =f'nivel = {"{:,}".format(int(float(conteudo)))}'
    color_msg = 0, 0 , 0
    prep_msg = font.render(msg, True, color_msg)
    prep_msg_rect = prep_msg.get_rect()
    prep_msg_rect.bottom = screen_rect.bottom
    prep_msg_rect.left = screen_rect.left + 50
    # desenha seu atual nivel na tela 
    screen.blit(prep_msg, prep_msg_rect)


        
    
