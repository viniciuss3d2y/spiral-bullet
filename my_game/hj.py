import pygame

pygame.init()
pygame.mixer.init()

# Carrega e toca o efeito sonoro
try:
    sound = pygame.mixer.Sound("sons_jogo/music.wav")
    sound.play()
except pygame.error as e:
    print(f"Erro ao carregar ou tocar o efeito sonoro: {e}")

# Mantém o programa em execução para ouvir o efeito sonoro
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print('mey')
            print('huej')
pygame.quit()
