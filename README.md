# PYGAMING-JP-JP-LUCAS

## Autores
- João Paulo Canato
- João Pedro Marrar
- Lucas Santana

## Descrição do Projeto

Jogo de tênis desenvolvido em Python utilizando a biblioteca Pygame. O jogo apresenta uma experiência completa de tênis com diferentes personagens, tipos de quadra e mecânicas realistas.

### Características Principais:
- **5 Personagens Jogáveis**: Djokovic, Federer, Nadal, João Fonseca e Mr. Resina
- **3 Tipos de Quadra**: Grama, Saibro e Rápida
- **Sistema de Pontuação Real do Tênis**: 0, 15, 30, 40, Vantagem
- **Mecânicas Especiais**: Estrelas que aceleram a bola durante o jogo
- **Interface Completa**: Menus, seleção de personagens e instruções

### Funcionalidades:
- Jogo para 2 jogadores local
- Física realista da bola com aceleração progressiva
- Sistema de games (melhor de 3)
- Countdown entre pontos
- Personagens espelhados para melhor visualização
- Música de fundo

## Como Executar o Jogo

### Pré-requisitos:
- Python 3.x instalado
- Biblioteca Pygame instalada (`pip install pygame`)

### Execução:
1. Navegue até a pasta do projeto
2. Execute o arquivo principal:
   ```
   python jogo.py
   ```


### Controles:
- **Player 1 (Esquerda)**: W/A/S/D
- **Player 2 (Direita)**: Setas do teclado
- **ESC**: Voltar ao menu anterior
- **ESPAÇO**: Reiniciar após vitória

### Estrutura do Projeto:
- `jogo.py` - Arquivo principal (EXECUTE ESTE ARQUIVO)
- `imports.py` - Constantes e configurações
- `funçoes.py` - Classes e funções do jogo
- `imagens/` - Recursos gráficos
- `run.bat` - Executável sem cache