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
TELA_PERSONAGENS = 2
estado_atual = TELA_INICIO

# Variáveis dos jogadores
personagem_player1 = None
personagem_player2 = None
tipo_quadra = None

# Carregar imagens - Tela Início
tela_inicio = pygame.image.load("imagens/Tela_inicio.png")
tela_inicio = pygame.transform.scale(tela_inicio, (SCREEN_WIDTH, SCREEN_HEIGHT))

botao_jogar = pygame.image.load("imagens/jogar.bottão.png")
botao_jogar_scaled = pygame.transform.scale(botao_jogar, (300, 100))
botao_jogar_rect = botao_jogar_scaled.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-80))

# Carregar imagens - Tela Modo de Jogo
fundo_segunda_tela = pygame.image.load("imagens/fundosegundatela.png")
fundo_segunda_tela = pygame.transform.scale(fundo_segunda_tela, (SCREEN_WIDTH, SCREEN_HEIGHT))

modo_jogo_img = pygame.image.load("imagens/mododejogo.png")
modo_jogo_scaled = pygame.transform.scale(modo_jogo_img, (300, 80))
modo_jogo_rect = modo_jogo_scaled.get_rect(center=(SCREEN_WIDTH/2, 150))

grama_img = pygame.image.load("imagens/grama.png")
grama_scaled = pygame.transform.scale(grama_img, (200, 60))
grama_rect = grama_scaled.get_rect(center=(SCREEN_WIDTH/2, 280))

rapida_img = pygame.image.load("imagens/rápida.png")
rapida_scaled = pygame.transform.scale(rapida_img, (200, 60))
rapida_rect = rapida_scaled.get_rect(center=(SCREEN_WIDTH/2, 420))

saibro_img = pygame.image.load("imagens/saibro.png")
saibro_scaled = pygame.transform.scale(saibro_img, (200, 60))
saibro_rect = saibro_scaled.get_rect(center=(SCREEN_WIDTH/2, 350))

# Carregar imagens - Tela Personagens
fundo_grama = pygame.image.load("imagens/fundograma.png")
fundo_grama = pygame.transform.scale(fundo_grama, (SCREEN_WIDTH, SCREEN_HEIGHT))
fundo_saibro = pygame.image.load("imagens/Fundo_personagens.png")
fundo_saibro = pygame.transform.scale(fundo_saibro, (SCREEN_WIDTH, SCREEN_HEIGHT))
fundo_rapida = pygame.image.load("imagens/fundorapida.png")
fundo_rapida = pygame.transform.scale(fundo_rapida, (SCREEN_WIDTH, SCREEN_HEIGHT))

djoko_img = pygame.image.load("imagens/djoko.png")
federer_img = pygame.image.load("imagens/federer.png")
nadal_img = pygame.image.load("imagens/nadal.png")
joao_img = pygame.image.load("imagens/jfonseca.png")
resina_img = pygame.image.load("imagens/resina.png")

# Player 1 (lado esquerdo)
djoko_p1 = pygame.transform.scale(djoko_img, (100, 100))
djoko_p1_rect = djoko_p1.get_rect(center=(120, 250))
federer_p1 = pygame.transform.scale(federer_img, (100, 100))
federer_p1_rect = federer_p1.get_rect(center=(220, 250))
nadal_p1 = pygame.transform.scale(nadal_img, (100, 100))
nadal_p1_rect = nadal_p1.get_rect(center=(120, 350))
joao_p1 = pygame.transform.scale(joao_img, (100, 100))
joao_p1_rect = joao_p1.get_rect(center=(220, 350))
resina_p1 = pygame.transform.scale(resina_img, (100, 100))
resina_p1_rect = resina_p1.get_rect(center=(170, 450))

# Player 2 (lado direito)
djoko_p2 = pygame.transform.scale(djoko_img, (100, 100))
djoko_p2_rect = djoko_p2.get_rect(center=(630, 250))
federer_p2 = pygame.transform.scale(federer_img, (100, 100))
federer_p2_rect = federer_p2.get_rect(center=(730, 250))
nadal_p2 = pygame.transform.scale(nadal_img, (100, 100))
nadal_p2_rect = nadal_p2.get_rect(center=(630, 350))
joao_p2 = pygame.transform.scale(joao_img, (100, 100))
joao_p2_rect = joao_p2.get_rect(center=(730, 350))
resina_p2 = pygame.transform.scale(resina_img, (100, 100))
resina_p2_rect = resina_p2.get_rect(center=(680, 450))

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                if estado_atual == TELA_MODO_JOGO:
                    estado_atual = TELA_INICIO
                elif estado_atual == TELA_PERSONAGENS:
                    estado_atual = TELA_MODO_JOGO
                    personagem_player1 = None
                    personagem_player2 = None
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if estado_atual == TELA_INICIO:
                if botao_jogar_rect.collidepoint(evento.pos):
                    estado_atual = TELA_MODO_JOGO
            elif estado_atual == TELA_MODO_JOGO:
                if grama_rect.collidepoint(evento.pos):
                    tipo_quadra = "grama"
                    estado_atual = TELA_PERSONAGENS
                elif saibro_rect.collidepoint(evento.pos):
                    tipo_quadra = "saibro"
                    estado_atual = TELA_PERSONAGENS
                elif rapida_rect.collidepoint(evento.pos):
                    tipo_quadra = "rapida"
                    estado_atual = TELA_PERSONAGENS
            elif estado_atual == TELA_PERSONAGENS:
                # Player 1 seleções
                if djoko_p1_rect.collidepoint(evento.pos):
                    personagem_player1 = "Djokovic"
                elif federer_p1_rect.collidepoint(evento.pos):
                    personagem_player1 = "Federer"
                elif nadal_p1_rect.collidepoint(evento.pos):
                    personagem_player1 = "Nadal"
                elif joao_p1_rect.collidepoint(evento.pos):
                    personagem_player1 = "João Fonseca"
                elif resina_p1_rect.collidepoint(evento.pos):
                    personagem_player1 = "Resina"
                # Player 2 seleções
                elif djoko_p2_rect.collidepoint(evento.pos):
                    personagem_player2 = "Djokovic"
                elif federer_p2_rect.collidepoint(evento.pos):
                    personagem_player2 = "Federer"
                elif nadal_p2_rect.collidepoint(evento.pos):
                    personagem_player2 = "Nadal"
                elif joao_p2_rect.collidepoint(evento.pos):
                    personagem_player2 = "João Fonseca"
                elif resina_p2_rect.collidepoint(evento.pos):
                    personagem_player2 = "Resina"
                
                # Verificar se ambos escolheram
                if personagem_player1 and personagem_player2:
                    print(f"Player 1: {personagem_player1}, Player 2: {personagem_player2}")
                    print("Jogo pode começar!")
        

    screen.fill((0, 0, 0))
    
    if estado_atual == TELA_INICIO:
        screen.blit(tela_inicio, (0, 0))
        screen.blit(botao_jogar_scaled, botao_jogar_rect)
    elif estado_atual == TELA_MODO_JOGO:
        screen.blit(fundo_segunda_tela, (0, 0))
        screen.blit(modo_jogo_scaled, modo_jogo_rect)
        screen.blit(grama_scaled, grama_rect)
        screen.blit(rapida_scaled, rapida_rect)
        screen.blit(saibro_scaled, saibro_rect)
    elif estado_atual == TELA_PERSONAGENS:
        if tipo_quadra == "grama":
            screen.blit(fundo_grama, (0, 0))
        elif tipo_quadra == "saibro":
            screen.blit(fundo_saibro, (0, 0))
        elif tipo_quadra == "rapida":
            screen.blit(fundo_rapida, (0, 0))
        # Player 1 personagens
        screen.blit(djoko_p1, djoko_p1_rect)
        screen.blit(federer_p1, federer_p1_rect)
        screen.blit(nadal_p1, nadal_p1_rect)
        screen.blit(joao_p1, joao_p1_rect)
        screen.blit(resina_p1, resina_p1_rect)
        # Player 2 personagens
        screen.blit(djoko_p2, djoko_p2_rect)
        screen.blit(federer_p2, federer_p2_rect)
        screen.blit(nadal_p2, nadal_p2_rect)
        screen.blit(joao_p2, joao_p2_rect)
        screen.blit(resina_p2, resina_p2_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()