import pygame
import sys

pygame.init()

# Configurações
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DESOFT-ATP")
clock = pygame.time.Clock()

# Estados do jogo
TELA_INICIO = 0
TELA_MODO_JOGO = 1
estado_atual = TELA_INICIO

# Carregar imagens - Tela Início
tela_inicio = pygame.image.load("imagens/Tela_inicio.png")
tela_inicio = pygame.transform.scale(tela_inicio, (SCREEN_WIDTH, SCREEN_HEIGHT))

botao_jogar = pygame.image.load("imagens/jogar.bottão.png")
botao_jogar_scaled = pygame.transform.scale(botao_jogar, (300, 100))
botao_jogar_rect = botao_jogar_scaled.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-80))

# Carregar imagens - Tela Modo de Jogo
modo_jogo_img = pygame.image.load("imagens/mododejogo.png")
modo_jogo_scaled = pygame.transform.scale(modo_jogo_img, (300, 80))
modo_jogo_rect = modo_jogo_scaled.get_rect(center=(SCREEN_WIDTH/2, 150))

grama_img = pygame.image.load("imagens/grama.png")
grama_scaled = pygame.transform.scale(grama_img, (200, 60))
grama_rect = grama_scaled.get_rect(center=(SCREEN_WIDTH/2, 280))

rapida_img = pygame.image.load("imagens/rápida.png")
rapida_scaled = pygame.transform.scale(rapida_img, (200, 60))
rapida_rect = rapida_scaled.get_rect(center=(SCREEN_WIDTH/2, 350))

saibro_img = pygame.image.load("imagens/saibro.png")
saibro_scaled = pygame.transform.scale(saibro_img, (200, 60))
saibro_rect = saibro_scaled.get_rect(center=(SCREEN_WIDTH/2, 420))

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if estado_atual == TELA_INICIO:
                if botao_jogar_rect.collidepoint(evento.pos):
                    estado_atual = TELA_MODO_JOGO
            elif estado_atual == TELA_MODO_JOGO:
                if grama_rect.collidepoint(evento.pos):
                    print("Grama selecionada!")
                elif rapida_rect.collidepoint(evento.pos):
                    print("Rápida selecionada!")
                elif saibro_rect.collidepoint(evento.pos):
                    print("Saibro selecionado!")
    
    screen.fill((0, 0, 0))
    
    if estado_atual == TELA_INICIO:
        screen.blit(tela_inicio, (0, 0))
        screen.blit(botao_jogar_scaled, botao_jogar_rect)
    elif estado_atual == TELA_MODO_JOGO:
        screen.blit(modo_jogo_scaled, modo_jogo_rect)
        screen.blit(grama_scaled, grama_rect)
        screen.blit(rapida_scaled, rapida_rect)
        screen.blit(saibro_scaled, saibro_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()