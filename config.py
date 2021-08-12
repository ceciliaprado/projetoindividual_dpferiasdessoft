from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets')
SND_DIR = path.join(path.dirname(__file__), 'assets')
FNT_DIR = path.join(path.dirname(__file__), 'assets')

# Dados gerais do jogo.
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo


METEOR_WIDTH = 50
METEOR_HEIGHT = 50
SHIP_WIDTH = 150
SHIP_HEIGHT = 150

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
TELA_FINAL= 3