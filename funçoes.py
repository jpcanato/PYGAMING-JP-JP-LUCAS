import pygame
import random
import math
from imports import SCREEN_WIDTH, SCREEN_HEIGHT

class Jogador:
    def __init__(self, x, y, personagem, lado):
        self.x = x
        self.y = y
        self.personagem = personagem
        self.lado = lado
        self.velocidade = 7
        self.rect = pygame.Rect(x-60, y-60, 120, 120)
        
    def mover(self, keys):
        if self.lado == "esquerda":
            if keys[pygame.K_w] and self.y > 237:
                self.y -= self.velocidade
            if keys[pygame.K_s] and self.y < SCREEN_HEIGHT - 165:
                self.y += self.velocidade
            if keys[pygame.K_a] and self.x > 120:
                self.x -= self.velocidade
            if keys[pygame.K_d] and self.x < SCREEN_WIDTH//2 - 120:
                self.x += self.velocidade
        else:
            if keys[pygame.K_UP] and self.y > 237:
                self.y -= self.velocidade
            if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - 165:
                self.y += self.velocidade
            if keys[pygame.K_LEFT] and self.x > SCREEN_WIDTH//2 + 120:
                self.x -= self.velocidade
            if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - 120:
                self.x += self.velocidade
        
        self.rect.center = (self.x, self.y)

class Bola:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.vel_x = random.choice([-6, 6])
        self.vel_y = random.choice([-4, 4])
        self.velocidade_base = 6
        self.rect = pygame.Rect(self.x-15, self.y-15, 30, 30)
        
    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y
        
        if self.y <= 237 or self.y >= SCREEN_HEIGHT - 165:
            self.vel_y = -self.vel_y
            
        self.rect.center = (self.x, self.y)
        
    def rebater(self, jogador):
        if self.rect.colliderect(jogador.rect):
            self.vel_x = -self.vel_x
            if jogador.lado == "esquerda":
                self.x = jogador.x + 75
            else:
                self.x = jogador.x - 75
            
            velocidade_atual = math.sqrt(self.vel_x**2 + self.vel_y**2)
            nova_velocidade = min(velocidade_atual * 1.1, 18)
            fator = nova_velocidade / velocidade_atual
            self.vel_x *= fator
            self.vel_y *= fator
            
            return True
        return False
        
    def resetar(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.vel_x = random.choice([-6, 6])
        self.vel_y = random.choice([-4, 4])
        
class Estrela:
    def __init__(self):
        self.x = random.randint(150, SCREEN_WIDTH-150)
        self.y = random.randint(312, SCREEN_HEIGHT-240)
        self.rect = pygame.Rect(self.x-22, self.y-22, 45, 45)
        self.ativa = True
        
    def coletar(self, bola):
        if self.ativa and self.rect.colliderect(bola.rect):
            self.ativa = False
            velocidade_atual = math.sqrt(bola.vel_x**2 + bola.vel_y**2)
            nova_velocidade = min(velocidade_atual * 1.3, 22)
            fator = nova_velocidade / velocidade_atual
            bola.vel_x *= fator
            bola.vel_y *= fator
            return True
        return False

def carregar_recursos():
    tela_inicio = pygame.image.load("imagens/Tela_inicio.png")
    tela_inicio = pygame.transform.scale(tela_inicio, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    botao_jogar = pygame.image.load("imagens/jogar.bottão.png")
    botao_jogar_scaled = pygame.transform.scale(botao_jogar, (450, 150))
    botao_jogar_rect = botao_jogar_scaled.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-120))
    
    fundo_segunda_tela = pygame.image.load("imagens/fundosegundatela.png")
    fundo_segunda_tela = pygame.transform.scale(fundo_segunda_tela, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    grama_img = pygame.image.load("imagens/grama.png")
    grama_scaled = pygame.transform.scale(grama_img, (300, 90))
    grama_rect = grama_scaled.get_rect(center=(SCREEN_WIDTH/2, 120))
    
    rapida_img = pygame.image.load("imagens/rápida.png")
    rapida_scaled = pygame.transform.scale(rapida_img, (300, 90))
    rapida_rect = rapida_scaled.get_rect(center=(SCREEN_WIDTH/2, 630))
    
    saibro_img = pygame.image.load("imagens/saibro.png")
    saibro_scaled = pygame.transform.scale(saibro_img, (300, 90))
    saibro_rect = saibro_scaled.get_rect(center=(SCREEN_WIDTH/2, 375))
    
    fundo_grama = pygame.image.load("imagens/fundograma.png")
    fundo_grama = pygame.transform.scale(fundo_grama, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fundo_saibro = pygame.image.load("imagens/Fundo_personagens.png")
    fundo_saibro = pygame.transform.scale(fundo_saibro, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fundo_rapida = pygame.image.load("imagens/fundorapida.png")
    fundo_rapida = pygame.transform.scale(fundo_rapida, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
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
    
    djoko_p1 = pygame.transform.scale(djoko_img, (120, 120))
    djoko_p1_rect = djoko_p1.get_rect(center=(120, 360))
    federer_p1 = pygame.transform.scale(federer_img, (120, 120))
    federer_p1_rect = federer_p1.get_rect(center=(315, 360))
    nadal_p1 = pygame.transform.scale(nadal_img, (120, 120))
    nadal_p1_rect = nadal_p1.get_rect(center=(510, 360))
    joao_p1 = pygame.transform.scale(joao_img, (120, 120))
    joao_p1_rect = joao_p1.get_rect(center=(202, 540))
    resina_p1 = pygame.transform.scale(resina_img, (120, 120))
    resina_p1_rect = resina_p1.get_rect(center=(397, 540))
    
    djoko_p2 = pygame.transform.scale(djoko_img, (120, 120))
    djoko_p2_rect = djoko_p2.get_rect(center=(765, 360))
    federer_p2 = pygame.transform.scale(federer_img, (120, 120))
    federer_p2_rect = federer_p2.get_rect(center=(960, 360))
    nadal_p2 = pygame.transform.scale(nadal_img, (120, 120))
    nadal_p2_rect = nadal_p2.get_rect(center=(1155, 360))
    joao_p2 = pygame.transform.scale(joao_img, (120, 120))
    joao_p2_rect = joao_p2.get_rect(center=(862, 540))
    resina_p2 = pygame.transform.scale(resina_img, (120, 120))
    resina_p2_rect = resina_p2.get_rect(center=(1057, 540))
    
    iniciar_jogo_img = pygame.image.load("imagens/iniciarjogo.png")
    iniciar_jogo_scaled = pygame.transform.scale(iniciar_jogo_img, (180, 60))
    iniciar_jogo_rect = iniciar_jogo_scaled.get_rect(center=(SCREEN_WIDTH/2, 705))
    
    bolinha_img = pygame.image.load("imagens/bolinha.png")
    bolinha_scaled = pygame.transform.scale(bolinha_img, (30, 30))
    
    personagens = {
        'Djokovic': djoko_img,
        'Federer': federer_img,
        'Nadal': nadal_img,
        'João Fonseca': joao_img,
        'Resina': resina_img
    }
    
    return {
        'tela_inicio': tela_inicio,
        'bolinha': bolinha_scaled,
        'personagens': personagens,
        'botao_jogar_scaled': botao_jogar_scaled,
        'botao_jogar_rect': botao_jogar_rect,
        'fundo_segunda_tela': fundo_segunda_tela,
        'grama_scaled': grama_scaled,
        'grama_rect': grama_rect,
        'rapida_scaled': rapida_scaled,
        'rapida_rect': rapida_rect,
        'saibro_scaled': saibro_scaled,
        'saibro_rect': saibro_rect,
        'fundo_grama': fundo_grama,
        'fundo_saibro': fundo_saibro,
        'fundo_rapida': fundo_rapida,
        'quadra_grama': quadra_grama,
        'quadra_saibro': quadra_saibro,
        'quadra_rapida': quadra_rapida,
        'djoko_p1': djoko_p1,
        'djoko_p1_rect': djoko_p1_rect,
        'federer_p1': federer_p1,
        'federer_p1_rect': federer_p1_rect,
        'nadal_p1': nadal_p1,
        'nadal_p1_rect': nadal_p1_rect,
        'joao_p1': joao_p1,
        'joao_p1_rect': joao_p1_rect,
        'resina_p1': resina_p1,
        'resina_p1_rect': resina_p1_rect,
        'djoko_p2': djoko_p2,
        'djoko_p2_rect': djoko_p2_rect,
        'federer_p2': federer_p2,
        'federer_p2_rect': federer_p2_rect,
        'nadal_p2': nadal_p2,
        'nadal_p2_rect': nadal_p2_rect,
        'joao_p2': joao_p2,
        'joao_p2_rect': joao_p2_rect,
        'resina_p2': resina_p2,
        'resina_p2_rect': resina_p2_rect,
        'iniciar_jogo_scaled': iniciar_jogo_scaled,
        'iniciar_jogo_rect': iniciar_jogo_rect
    }

def renderizar_tela(screen, estado_atual, recursos, tipo_quadra, personagem_player1, personagem_player2, contador=0, font_countdown=None):
    screen.fill((0, 0, 0))
    
    if estado_atual == 0:
        screen.blit(recursos['tela_inicio'], (0, 0))
        screen.blit(recursos['botao_jogar_scaled'], recursos['botao_jogar_rect'])
    elif estado_atual == 1:
        screen.blit(recursos['fundo_segunda_tela'], (0, 0))
        screen.blit(recursos['grama_scaled'], recursos['grama_rect'])
        screen.blit(recursos['rapida_scaled'], recursos['rapida_rect'])
        screen.blit(recursos['saibro_scaled'], recursos['saibro_rect'])
    elif estado_atual == 2:
        if tipo_quadra == "grama":
            screen.blit(recursos['fundo_grama'], (0, 0))
        elif tipo_quadra == "saibro":
            screen.blit(recursos['fundo_saibro'], (0, 0))
        elif tipo_quadra == "rapida":
            screen.blit(recursos['fundo_rapida'], (0, 0))
        
        screen.blit(recursos['djoko_p1'], recursos['djoko_p1_rect'])
        screen.blit(recursos['federer_p1'], recursos['federer_p1_rect'])
        screen.blit(recursos['nadal_p1'], recursos['nadal_p1_rect'])
        screen.blit(recursos['joao_p1'], recursos['joao_p1_rect'])
        screen.blit(recursos['resina_p1'], recursos['resina_p1_rect'])
        
        screen.blit(recursos['djoko_p2'], recursos['djoko_p2_rect'])
        screen.blit(recursos['federer_p2'], recursos['federer_p2_rect'])
        screen.blit(recursos['nadal_p2'], recursos['nadal_p2_rect'])
        screen.blit(recursos['joao_p2'], recursos['joao_p2_rect'])
        screen.blit(recursos['resina_p2'], recursos['resina_p2_rect'])
        
        if personagem_player1 == "Djokovic":
            pygame.draw.rect(screen, (0, 255, 0), recursos['djoko_p1_rect'], 3)
        elif personagem_player1 == "Federer":
            pygame.draw.rect(screen, (0, 255, 0), recursos['federer_p1_rect'], 3)
        elif personagem_player1 == "Nadal":
            pygame.draw.rect(screen, (0, 255, 0), recursos['nadal_p1_rect'], 3)
        elif personagem_player1 == "João Fonseca":
            pygame.draw.rect(screen, (0, 255, 0), recursos['joao_p1_rect'], 3)
        elif personagem_player1 == "Resina":
            pygame.draw.rect(screen, (0, 255, 0), recursos['resina_p1_rect'], 3)
            
        if personagem_player2 == "Djokovic":
            pygame.draw.rect(screen, (255, 0, 0), recursos['djoko_p2_rect'], 3)
        elif personagem_player2 == "Federer":
            pygame.draw.rect(screen, (255, 0, 0), recursos['federer_p2_rect'], 3)
        elif personagem_player2 == "Nadal":
            pygame.draw.rect(screen, (255, 0, 0), recursos['nadal_p2_rect'], 3)
        elif personagem_player2 == "João Fonseca":
            pygame.draw.rect(screen, (255, 0, 0), recursos['joao_p2_rect'], 3)
        elif personagem_player2 == "Resina":
            pygame.draw.rect(screen, (255, 0, 0), recursos['resina_p2_rect'], 3)
        
        fonte = pygame.font.Font(None, 32)
        nome_djoko_p1 = fonte.render("Novak Djokovic", True, (255, 255, 255))
        screen.blit(nome_djoko_p1, (20, 427))
        nome_federer_p1 = fonte.render("Roger Federer", True, (255, 255, 255))
        screen.blit(nome_federer_p1, (239, 427))
        nome_nadal_p1 = fonte.render("Rafael Nadal", True, (255, 255, 255))
        screen.blit(nome_nadal_p1, (452, 427))
        nome_joao_p1 = fonte.render("João Fonseca", True, (255, 255, 255))
        screen.blit(nome_joao_p1, (125, 607))
        nome_resina_p1 = fonte.render("Mr. Resina", True, (255, 255, 255))
        screen.blit(nome_resina_p1, (347, 607))
        
        nome_djoko_p2 = fonte.render("Novak Djokovic", True, (255, 255, 255))
        screen.blit(nome_djoko_p2, (660, 427))
        nome_federer_p2 = fonte.render("Roger Federer", True, (255, 255, 255))
        screen.blit(nome_federer_p2, (884, 427))
        nome_nadal_p2 = fonte.render("Rafael Nadal", True, (255, 255, 255))
        screen.blit(nome_nadal_p2, (1092, 427))
        nome_joao_p2 = fonte.render("João Fonseca", True, (255, 255, 255))
        screen.blit(nome_joao_p2, (786, 607))
        nome_resina_p2 = fonte.render("Mr. Resina", True, (255, 255, 255))
        screen.blit(nome_resina_p2, (1010, 607))
        
        if personagem_player1 and personagem_player2:
            screen.blit(recursos['iniciar_jogo_scaled'], recursos['iniciar_jogo_rect'])
    elif estado_atual == 3:
        if tipo_quadra == "grama":
            screen.blit(recursos['quadra_grama'], (0, 0))
        elif tipo_quadra == "saibro":
            screen.blit(recursos['quadra_saibro'], (0, 0))
        elif tipo_quadra == "rapida":
            screen.blit(recursos['quadra_rapida'], (0, 0))
        
        if contador > 0 and font_countdown:
            texto = font_countdown.render(str(contador), True, (255, 255, 255))
            texto_rect = texto.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            screen.blit(texto, texto_rect)
    elif estado_atual == 4:
        if tipo_quadra == "grama":
            screen.blit(recursos['quadra_grama'], (0, 0))
        elif tipo_quadra == "saibro":
            screen.blit(recursos['quadra_saibro'], (0, 0))
        elif tipo_quadra == "rapida":
            screen.blit(recursos['quadra_rapida'], (0, 0))

def obter_imagem_personagem(recursos, personagem):
    return recursos['personagens'].get(personagem)

def renderizar_jogo(screen, recursos, tipo_quadra, jogador1, jogador2, bola, estrelas, pontos1, pontos2, aguardando_ponto=False, contador_ponto=0):
    if tipo_quadra == "grama":
        screen.blit(recursos['quadra_grama'], (0, 0))
    elif tipo_quadra == "saibro":
        screen.blit(recursos['quadra_saibro'], (0, 0))
    elif tipo_quadra == "rapida":
        screen.blit(recursos['quadra_rapida'], (0, 0))
    
    pygame.draw.line(screen, (255, 255, 255), (SCREEN_WIDTH//2, 237), (SCREEN_WIDTH//2, SCREEN_HEIGHT-165), 4)
    
    img1 = obter_imagem_personagem(recursos, jogador1.personagem)
    img2 = obter_imagem_personagem(recursos, jogador2.personagem)
    
    if img1:
        img1_scaled = pygame.transform.scale(img1, (120, 120))
        screen.blit(img1_scaled, (jogador1.x-60, jogador1.y-60))
    
    if img2:
        img2_scaled = pygame.transform.scale(img2, (120, 120))
        screen.blit(img2_scaled, (jogador2.x-60, jogador2.y-60))
    
    screen.blit(recursos['bolinha'], (int(bola.x-15), int(bola.y-15)))
    
    for estrela in estrelas:
        if estrela.ativa:
            # Desenhar estrela
            pontos = []
            for i in range(10):
                angulo = i * math.pi / 5
                raio = 20 if i % 2 == 0 else 10
                x = estrela.x + raio * math.cos(angulo - math.pi/2)
                y = estrela.y + raio * math.sin(angulo - math.pi/2)
                pontos.append((x, y))
            pygame.draw.polygon(screen, (255, 255, 0), pontos)
    
    fonte = pygame.font.Font(None, 54)
    texto_pontos = fonte.render(f"{pontos1} - {pontos2}", True, (255, 255, 255))
    screen.blit(texto_pontos, (SCREEN_WIDTH//2 - 45, 30))
    
    if aguardando_ponto and contador_ponto > 0:
        font_countdown = pygame.font.Font(None, 225)
        texto_countdown = font_countdown.render(str(contador_ponto), True, (255, 255, 255))
        texto_rect = texto_countdown.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        screen.blit(texto_countdown, texto_rect)