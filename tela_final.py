import pygame
import random
from os import path
from assets import load_assets, SCORE_FONT
from config import BLACK, FPS, GAME, INIT, QUIT, TELA_FINAL, YELLOW, WIDTH



def tela_final(screen, score):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()
    # Carrega o fundo da tela inicial
    tela_final = assets['tela_final']
    tela_final_rect = tela_final.get_rect()

    running = True
    state = TELA_FINAL
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYDOWN and event.key != pygame.K_RETURN:
                state = QUIT
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                state = GAME
                running = False
                

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(tela_final, tela_final_rect)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  480)
        screen.blit(text_surface, text_rect)


        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
