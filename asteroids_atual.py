# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Asteroids')

# ----- Inicia assets
METEOR_WIDTH = 50
METEOR_HEIGHT = 50


background = pygame.image.load('assets/starfield2.jpg').convert()
meteor_img = pygame.image.load('assets/coroninha.png').convert_alpha()
meteor_img_small = pygame.transform.scale(meteor_img, (METEOR_WIDTH, METEOR_HEIGHT))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Definindo os novos tipos
class Meteor(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
        self.rect.y = random.randint(-100, - METEOR_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
            self.rect.y = random.randint(-100, -METEOR_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)


# ----- Inicia estruturas de dados
game = True

# Criando um grupo de meteoros
all_meteors = pygame.sprite.Group()
# Criando os meteoros
for i in range(8):
    meteor = Meteor(meteor_img)
    all_meteors.add(meteor)

    
#velocidade
clock = pygame.time.Clock()
FPS = 30

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
   # Atualizando a posição dos meteoros
    meteor1.update()
    meteor2.update()

  

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))

    window.blit(meteor1.image, meteor1.rect)
    window.blit(meteor2.image, meteor2.rect)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
