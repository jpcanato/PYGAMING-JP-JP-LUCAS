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
TELA_COUNTDOWN = 3
estado_atual = TELA_INICIO

# Variáveis dos jogadores
personagem_player1 = None
personagem_player2 = None
tipo_quadra = None

# Variáveis do countdown
contador = 3
tempo_countdown = 0
font_countdown = pygame.font.Font(None, 200)

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

# Carregar imagens - Fundos Countdown
quadra_grama = pygame.image.load("imagens/quadra_1.png")
quadra_grama = pygame.transform.scale(quadra_grama, (SCREEN_WIDTH, SCREEN_HEIGHT))
quadra_saibro = pygame.image.load("imagens/quadra_2.png")
quadra_saibro = pygame.transform.scale(quadra_saibro, (SCREEN_WIDTH, SCREEN_HEIGHT))
quadra_rapida = pygame.image.load("imagens/quadra_3.png")
quadra_rapida = pygame.transform.scale(quadra_rapida, (SCREEN_WIDTH, SCREEN_HEIGHT))

djoko_img = pygame.image.load("imagens/djoko.png")
federer_img = pygame.image.load("imagens/federer.png")
nadal_img = pygame.image.load("imagens/nadal.png")
joao_img = pygame.image.load("imagens/jfonseca.png")
resina_img = pygame.image.load("imagens/resina.png")

# Player 1 (lado esquerdo) - 3 na primeira linha, 2 na segunda
djoko_p1 = pygame.transform.scale(djoko_img, (80, 80))
djoko_p1_rect = djoko_p1.get_rect(center=(80, 240))
federer_p1 = pygame.transform.scale(federer_img, (80, 80))
federer_p1_rect = federer_p1.get_rect(center=(210, 240))
nadal_p1 = pygame.transform.scale(nadal_img, (80, 80))
nadal_p1_rect = nadal_p1.get_rect(center=(340, 240))
joao_p1 = pygame.transform.scale(joao_img, (80, 80))
joao_p1_rect = joao_p1.get_rect(center=(135, 360))
resina_p1 = pygame.transform.scale(resina_img, (80, 80))
resina_p1_rect = resina_p1.get_rect(center=(265, 360))

# Player 2 (lado direito) - 3 na primeira linha, 2 na segunda
djoko_p2 = pygame.transform.scale(djoko_img, (80, 80))
djoko_p2_rect = djoko_p2.get_rect(center=(510, 240))
federer_p2 = pygame.transform.scale(federer_img, (80, 80))
federer_p2_rect = federer_p2.get_rect(center=(640, 240))
nadal_p2 = pygame.transform.scale(nadal_img, (80, 80))
nadal_p2_rect = nadal_p2.get_rect(center=(770, 240))
joao_p2 = pygame.transform.scale(joao_img, (80, 80))
joao_p2_rect = joao_p2.get_rect(center=(575, 360))
resina_p2 = pygame.transform.scale(resina_img, (80, 80))
resina_p2_rect = resina_p2.get_rect(center=(705, 360))

# Botão iniciar jogo
iniciar_jogo_img = pygame.image.load("imagens/iniciarjogo.png")
iniciar_jogo_scaled = pygame.transform.scale(iniciar_jogo_img, (120, 40))
iniciar_jogo_rect = iniciar_jogo_scaled.get_rect(center=(SCREEN_WIDTH/2, 470))

# Fonte para nomes
fonte = pygame.font.Font(None, 22)

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
                
                elif iniciar_jogo_rect.collidepoint(evento.pos):
                    if personagem_player1 and personagem_player2:
                        estado_atual = TELA_COUNTDOWN
                        contador = 3
                        tempo_countdown = pygame.time.get_ticks()
        

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
        
        # Sinalização Player 1 quando ele for selecionado
        if personagem_player1 == "Djokovic":
            pygame.draw.rect(screen, (0, 255, 0), djoko_p1_rect, 3)
        elif personagem_player1 == "Federer":
            pygame.draw.rect(screen, (0, 255, 0), federer_p1_rect, 3)
        elif personagem_player1 == "Nadal":
            pygame.draw.rect(screen, (0, 255, 0), nadal_p1_rect, 3)
        elif personagem_player1 == "João Fonseca":
            pygame.draw.rect(screen, (0, 255, 0), joao_p1_rect, 3)
        elif personagem_player1 == "Resina":
            pygame.draw.rect(screen, (0, 255, 0), resina_p1_rect, 3)
            
        # Sinalização Player 2 quando for selecionado
        if personagem_player2 == "Djokovic":
            pygame.draw.rect(screen, (255, 0, 0), djoko_p2_rect, 3)
        elif personagem_player2 == "Federer":
            pygame.draw.rect(screen, (255, 0, 0), federer_p2_rect, 3)
        elif personagem_player2 == "Nadal":
            pygame.draw.rect(screen, (255, 0, 0), nadal_p2_rect, 3)
        elif personagem_player2 == "João Fonseca":
            pygame.draw.rect(screen, (255, 0, 0), joao_p2_rect, 3)
        elif personagem_player2 == "Resina":
            pygame.draw.rect(screen, (255, 0, 0), resina_p2_rect, 3)
        
        # Nomes Player 1
        nome_djoko_p1 = fonte.render("Novak Djokovic", True, (255, 255, 255))
        screen.blit(nome_djoko_p1, (15, 285))
        nome_federer_p1 = fonte.render("Roger Federer", True, (255, 255, 255))
        screen.blit(nome_federer_p1, (155, 285))
        nome_nadal_p1 = fonte.render("Rafael Nadal", True, (255, 255, 255))
        screen.blit(nome_nadal_p1, (285, 285))
        nome_joao_p1 = fonte.render("João Fonseca", True, (255, 255, 255))
        screen.blit(nome_joao_p1, (75, 405))
        nome_resina_p1 = fonte.render("Resina", True, (255, 255, 255))
        screen.blit(nome_resina_p1, (240, 405))
        
        # Nomes Player 2
        nome_djoko_p2 = fonte.render("Novak Djokovic", True, (255, 255, 255))
        screen.blit(nome_djoko_p2, (445, 285))
        nome_federer_p2 = fonte.render("Roger Federer", True, (255, 255, 255))
        screen.blit(nome_federer_p2, (585, 285))
        nome_nadal_p2 = fonte.render("Rafael Nadal", True, (255, 255, 255))
        screen.blit(nome_nadal_p2, (715, 285))
        nome_joao_p2 = fonte.render("João Fonseca", True, (255, 255, 255))
        screen.blit(nome_joao_p2, (515, 405))
        nome_resina_p2 = fonte.render("Resina", True, (255, 255, 255))
        screen.blit(nome_resina_p2, (680, 405))
        
        # Botão iniciar jogo (só aparece se ambos escolheram)
        if personagem_player1 and personagem_player2:
            screen.blit(iniciar_jogo_scaled, iniciar_jogo_rect)
    elif estado_atual == TELA_COUNTDOWN:
        if tipo_quadra == "grama":
            screen.blit(quadra_grama, (0, 0))
        elif tipo_quadra == "saibro":
            screen.blit(quadra_saibro, (0, 0))
        elif tipo_quadra == "rapida":
            screen.blit(quadra_rapida, (0, 0))
        
        if pygame.time.get_ticks() - tempo_countdown >= 1000:
            contador -= 1
            tempo_countdown = pygame.time.get_ticks()
            if contador < 1:
                print("Jogo iniciado!")
        
        if contador > 0:
            texto = font_countdown.render(str(contador), True, (255, 255, 255))
            texto_rect = texto.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            screen.blit(texto, texto_rect) 

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()