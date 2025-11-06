from imports import *
from funçoes import carregar_recursos, renderizar_tela, renderizar_jogo, Jogador, Bola, Estrela

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("The Watcher (Instrumental) - Dr. Dre (youtube).mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DESOFT-ATP")
clock = pygame.time.Clock()

estado_atual = TELA_INICIO

personagem_player1 = None
personagem_player2 = None
tipo_quadra = None

contador = 3
tempo_countdown = 0
font_countdown = pygame.font.Font(None, 300)

recursos = carregar_recursos()
fonte = pygame.font.Font(None, 22)

jogador1 = None
jogador2 = None
bola = None
estrelas = []
pontos_player1 = 0
pontos_player2 = 0
tempo_estrela = 0
contador_ponto = 3
tempo_ponto = 0
aguardando_ponto = False

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
                elif estado_atual == TELA_JOGO:
                    estado_atual = TELA_INICIO
                    jogador1 = None
                    jogador2 = None
                    bola = None
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if estado_atual == TELA_INICIO:
                if recursos['botao_jogar_rect'].collidepoint(evento.pos):
                    estado_atual = TELA_MODO_JOGO
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
            elif estado_atual == TELA_PERSONAGENS:

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
                
                elif recursos['iniciar_jogo_rect'].collidepoint(evento.pos):
                    if personagem_player1 and personagem_player2:
                        estado_atual = TELA_COUNTDOWN
                        contador = 3
                        tempo_countdown = pygame.time.get_ticks()
        


    if estado_atual == TELA_COUNTDOWN:
        if pygame.time.get_ticks() - tempo_countdown >= 1000:
            contador -= 1
            tempo_countdown = pygame.time.get_ticks()
            if contador < 1:
                estado_atual = TELA_JOGO
                jogador1 = Jogador(120, SCREEN_HEIGHT//2, personagem_player1, "esquerda")
                jogador2 = Jogador(SCREEN_WIDTH-120, SCREEN_HEIGHT//2, personagem_player2, "direita")
                bola = Bola()
                estrelas = []
                pontos_player1 = 0
                pontos_player2 = 0
                tempo_estrela = pygame.time.get_ticks()
    
    if estado_atual == TELA_JOGO:
        if aguardando_ponto:
            if pygame.time.get_ticks() - tempo_ponto >= 1000:
                contador_ponto -= 1
                tempo_ponto = pygame.time.get_ticks()
                if contador_ponto < 1:
                    aguardando_ponto = False
                    jogador1.x = 120
                    jogador1.y = SCREEN_HEIGHT//2
                    jogador1.rect.center = (jogador1.x, jogador1.y)
                    jogador2.x = SCREEN_WIDTH-120
                    jogador2.y = SCREEN_HEIGHT//2
                    jogador2.rect.center = (jogador2.x, jogador2.y)
                    bola.resetar()
                    estrelas = []
                    tempo_estrela = pygame.time.get_ticks()
        else:
            keys = pygame.key.get_pressed()
            jogador1.mover(keys)
            jogador2.mover(keys)
            
            bola.mover()
            bola.rebater(jogador1)
            bola.rebater(jogador2)
            
            if pygame.time.get_ticks() - tempo_estrela > 5000 and len(estrelas) < 3:
                estrelas.append(Estrela())
                tempo_estrela = pygame.time.get_ticks()
            
            for estrela in estrelas:
                if estrela.coletar(bola):
                    break
            
            if bola.x < 0:
                pontos_player2 += 1
                aguardando_ponto = True
                contador_ponto = 3
                tempo_ponto = pygame.time.get_ticks()
            elif bola.x > SCREEN_WIDTH:
                pontos_player1 += 1
                aguardando_ponto = True
                contador_ponto = 3
                tempo_ponto = pygame.time.get_ticks()
    
    if estado_atual == TELA_JOGO:
        renderizar_jogo(screen, recursos, tipo_quadra, jogador1, jogador2, bola, estrelas, pontos_player1, pontos_player2, aguardando_ponto, contador_ponto)
    else:
        renderizar_tela(screen, estado_atual, recursos, tipo_quadra, personagem_player1, personagem_player2, contador, font_countdown)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()