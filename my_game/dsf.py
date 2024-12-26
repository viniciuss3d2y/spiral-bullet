import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((234, 121))

# Carrega e toca a música
try:
   sound = pygame.mixer.Sound('sons_jogo/music.wav')
   sound.play()
except pygame.error as e:
    print(f"Erro ao carregar ou tocar a música: {e}")

# Mantém o programa em execução para ouvir a música
running = True
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0 , 0))
    pygame.display.flip()
pygame.quit()
