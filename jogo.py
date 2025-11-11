from imports import *
from funçoes import carregar_recursos, renderizar_tela, renderizar_jogo, Jogador, Bola, Estrela

pygame.init()
pygame.mixer.init()

# Música de fundo
pygame.mixer.music.load("The Watcher (Instrumental) - Dr. Dre (youtube).mp3")
pygame.mixer.music.play(-1)  # Loop infinito
pygame.mixer.music.set_volume(1)

# Configuração da tela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DESOFT-ATP")
clock = pygame.time.Clock()

estado_atual = TELA_INICIO

# Variáveis de seleção dos jogadores
personagem_player1 = None
personagem_player2 = None
tipo_quadra = None

# Variáveis do countdown inicial
contador = 3
tempo_countdown = 0
font_countdown = pygame.font.Font(None, 300)

recursos = carregar_recursos()
fonte = pygame.font.Font(None, 22)

jogador1 = None
jogador2 = None
bola = None
estrelas = []

# Variáveis de pontuação
pontos_player1 = 0
pontos_player2 = 0
games_player1 = 0
games_player2 = 0
vencedor = None

tempo_estrela = 0
contador_ponto = 3
tempo_ponto = 0
aguardando_ponto = False

# Loop principal do jogo
rodando = True
while rodando:
    # Processamento de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        # Eventos de teclado
        if evento.type == pygame.KEYDOWN:
            # Tecla ESC para navegação entre telas
            if evento.key == pygame.K_ESCAPE:
                if estado_atual == TELA_MODO_JOGO:
                    estado_atual = TELA_INICIO
                elif estado_atual == TELA_PERSONAGENS:
                    estado_atual = TELA_MODO_JOGO
                    personagem_player1 = None
                    personagem_player2 = None
                elif estado_atual == TELA_INSTRUCOES:
                    estado_atual = TELA_INICIO
                elif estado_atual == TELA_JOGO and not vencedor:
                    estado_atual = TELA_INICIO
                    jogador1 = None
                    jogador2 = None
                    bola = None
            # Tecla ESPAÇO que reinicia o jogo após vitória
            elif evento.key == pygame.K_SPACE:
                if estado_atual == TELA_JOGO and vencedor:
                    estado_atual = TELA_INICIO
                    personagem_player1 = None
                    personagem_player2 = None
                    tipo_quadra = None
                    jogador1 = None
                    jogador2 = None
                    bola = None
                    pontos_player1 = 0
                    pontos_player2 = 0
                    games_player1 = 0
                    games_player2 = 0
                    vencedor = None
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Tela inicial 
            if estado_atual == TELA_INICIO:
                if recursos['botao_jogar_rect'].collidepoint(evento.pos):
                    estado_atual = TELA_MODO_JOGO
                elif recursos['botao_instrucoes_rect'].collidepoint(evento.pos):
                    estado_atual = TELA_INSTRUCOES
            # Tela de instruções 
            elif estado_atual == TELA_INSTRUCOES:
                if recursos['botao_voltar_rect'].collidepoint(evento.pos):
                    estado_atual = TELA_MODO_JOGO
            # Tela de seleção de quadra
            elif estado_atual == TELA_MODO_JOGO:
                if recursos['grama_rect'].collidepoint(evento.pos):
                    tipo_quadra = "grama"
                    estado_atual = TELA_PERSONAGENS
                elif recursos['saibro_rect'].collidepoint(evento.pos):
                    tipo_quadra = "saibro"
                    estado_atual = TELA_PERSONAGENS
                elif recursos['rapida_rect'].collidepoint(evento.pos):
                    tipo_quadra = "rapida"
                    estado_atual = TELA_PERSONAGENS
            # Tela de seleção de personagens
            elif estado_atual == TELA_PERSONAGENS:
                # Seleção do Player 1
                if recursos['djoko_p1_rect'].collidepoint(evento.pos):
                    personagem_player1 = "Djokovic"
                elif recursos['federer_p1_rect'].collidepoint(evento.pos):
                    personagem_player1 = "Federer"
                elif recursos['nadal_p1_rect'].collidepoint(evento.pos):
                    personagem_player1 = "Nadal"
                elif recursos['joao_p1_rect'].collidepoint(evento.pos):
                    personagem_player1 = "João Fonseca"
                elif recursos['resina_p1_rect'].collidepoint(evento.pos):
                    personagem_player1 = "Resina"
                # Seleção do Player 2
                elif recursos['djoko_p2_rect'].collidepoint(evento.pos):
                    personagem_player2 = "Djokovic"
                elif recursos['federer_p2_rect'].collidepoint(evento.pos):
                    personagem_player2 = "Federer"
                elif recursos['nadal_p2_rect'].collidepoint(evento.pos):
                    personagem_player2 = "Nadal"
                elif recursos['joao_p2_rect'].collidepoint(evento.pos):
                    personagem_player2 = "João Fonseca"
                elif recursos['resina_p2_rect'].collidepoint(evento.pos):
                    personagem_player2 = "Resina"
                # Botão para iniciar jogo
                elif recursos['iniciar_jogo_rect'].collidepoint(evento.pos):
                    if personagem_player1 and personagem_player2:
                        estado_atual = TELA_COUNTDOWN
                        contador = 3
                        tempo_countdown = pygame.time.get_ticks()
        

    # countdown antes do jogo começar
    if estado_atual == TELA_COUNTDOWN:
        if pygame.time.get_ticks() - tempo_countdown >= 1000:  # A cada 1 segundo
            contador -= 1
            tempo_countdown = pygame.time.get_ticks()
            if contador < 1:  # Quando countdown chega a zero
                # Inicia o jogo
                estado_atual = TELA_JOGO
                # Cria os objetos do jogo
                jogador1 = Jogador(120, SCREEN_HEIGHT//2, personagem_player1, "esquerda")
                jogador2 = Jogador(SCREEN_WIDTH-120, SCREEN_HEIGHT//2, personagem_player2, "direita")
                bola = Bola()
                estrelas = []
                # Reinicia pontuações
                pontos_player1 = 0
                pontos_player2 = 0
                games_player1 = 0
                games_player2 = 0
                vencedor = None
                tempo_estrela = pygame.time.get_ticks()
    
# Auxílio do chat gpt
    # Lógica principal do jogo
    if estado_atual == TELA_JOGO:
        # Countdown entre pontos
        if aguardando_ponto:
            if pygame.time.get_ticks() - tempo_ponto >= 1000:  # A cada 1 segundo
                contador_ponto -= 1
                tempo_ponto = pygame.time.get_ticks()
                if contador_ponto < 1:  # Fim do countdown
                    aguardando_ponto = False
                    # Reposiciona os jogadores
                    jogador1.x = 120
                    jogador1.y = SCREEN_HEIGHT//2
                    jogador1.rect.center = (jogador1.x, jogador1.y)
                    jogador2.x = SCREEN_WIDTH-120
                    jogador2.y = SCREEN_HEIGHT//2
                    jogador2.rect.center = (jogador2.x, jogador2.y)
                    # Reseta bola e estrelas
                    bola.resetar()
                    estrelas = []
                    tempo_estrela = pygame.time.get_ticks()
        # Jogo em andamento 
        elif not vencedor:
            # Captura teclas pressionadas
            keys = pygame.key.get_pressed()
            # Move os jogadores
            jogador1.mover(keys)
            jogador2.mover(keys)
            
            # Move a bola e verifica as batidas 
            bola.mover()
            bola.rebater(jogador1)
            bola.rebater(jogador2)
            
            # Gera estrelas a cada 5 segundos (máximo 3)
            if pygame.time.get_ticks() - tempo_estrela > 5000 and len(estrelas) < 3:
                estrelas.append(Estrela())
                tempo_estrela = pygame.time.get_ticks()
            
            # Verifica batidas da bola com estrelas
            for estrela in estrelas:
                if estrela.coletar(bola):
                    break
            
            # Verifica se bola saiu pela esquerda 
            if bola.x < 0:
                pontos_player2 += 1
                # Verifica se Player 2 ganhou o game
                if pontos_player2 >= 4 and pontos_player2 - pontos_player1 >= 2:
                    games_player2 += 1
                    pontos_player1 = 0
                    pontos_player2 = 0
                    # Verifica vitória (2 games)
                    if games_player2 >= 2:
                        vencedor = "Player 2"
                        aguardando_ponto = False  # Para o countdown quando há vencedor
                # Sistema de deuce (40-40)
                elif pontos_player1 >= 4 and pontos_player2 >= 4 and pontos_player1 > pontos_player2:
                    pontos_player1 = 3
                    pontos_player2 = 3
                if not vencedor:  # Só inicia countdown se não há vencedor
                    aguardando_ponto = True
                    contador_ponto = 3
                    tempo_ponto = pygame.time.get_ticks()
            # Verifica se bola saiu pela direita
            elif bola.x > SCREEN_WIDTH:
                pontos_player1 += 1
                # Verifica se Player 1 ganhou o game
                if pontos_player1 >= 4 and pontos_player1 - pontos_player2 >= 2:
                    games_player1 += 1
                    pontos_player1 = 0
                    pontos_player2 = 0
                    # Verifica vitória (2 games)
                    if games_player1 >= 2:
                        vencedor = "Player 1"
                        aguardando_ponto = False  # Para o countdown quando há vencedor
                # Sistema de deuce (40-40)
                elif pontos_player2 >= 4 and pontos_player1 >= 4 and pontos_player2 > pontos_player1:
                    pontos_player1 = 3
                    pontos_player2 = 3
                if not vencedor:  # Só inicia countdown se não há vencedor
                    aguardando_ponto = True
                    contador_ponto = 3
                    tempo_ponto = pygame.time.get_ticks()
    
    # Renderização das telas
    if estado_atual == TELA_JOGO:
        # Renderiza a tela do jogo
        renderizar_jogo(screen, recursos, tipo_quadra, jogador1, jogador2, bola, estrelas, pontos_player1, pontos_player2, games_player1, games_player2, vencedor, aguardando_ponto, contador_ponto)
    else:
        # menu, seleção, e outras
        renderizar_tela(screen, estado_atual, recursos, tipo_quadra, personagem_player1, personagem_player2, contador, font_countdown)
    
    # Atualiza a tela e controla FPS
    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
sys.exit()