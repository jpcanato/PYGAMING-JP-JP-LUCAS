import pygame
import sys

pygame.init()

# Configurações
SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DESOFT-ATP")
clock = pygame.time.Clock()

# Carregar imagens
tela_inicio = pygame.image.load("imagens/Tela_inicio.png")
tela_inicio = pygame.transform.scale(tela_inicio, (SCREEN_WIDTH, SCREEN_HEIGHT))

botao_jogar = pygame.image.load("imagens/jogar.png")
botao_tamanho = pygame.transform.scale(botao_jogar, (100, 140))
botao_rect = botao_tamanho.get_rect(center=(850, 500))

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao_rect.collidepoint(evento.pos):
                print("Jogo iniciado!")
    
    screen.blit(tela_inicio, (0, 0))
    screen.blit(botao_tamanho, botao_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()