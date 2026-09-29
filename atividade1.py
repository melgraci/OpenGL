import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *

print("Pygame:", pygame.version.ver)
print("Bibliotecas carregadas com sucesso!")


def abrir_janela_basica():
    pygame.init()

    # Cria a janela com resolução de 1024x700
    pygame.display.set_mode((1024, 700), DOUBLEBUF | OPENGL)

    # Define o título da janela
    pygame.display.set_caption("Minha Primeira Cena OpenGL")

    # Define a cor de fundo usando RGBA
    glClearColor(0.15, 0.20, 0.30, 1.0)

   

    relogio = pygame.time.Clock()
    executando = True

    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        glClear(GL_COLOR_BUFFER_BIT)
        pygame.display.flip()
        relogio.tick(30)

    pygame.quit()


abrir_janela_basica()