import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *


# Desenha um quadrado formado por dois triângulos
def desenhar_quadrado():
    glBegin(GL_TRIANGLES)

    # Primeiro triângulo - vermelho
    glColor3f(1.0, 0.0, 0.0)

    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)

    # Segundo triângulo - azul
    glColor3f(0.0, 0.3, 1.0)

    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)

    glEnd()


# Desenha uma casa usando um retângulo e um triângulo
def desenhar_casa():
    # Corpo da casa
    glBegin(GL_TRIANGLES)

    glColor3f(0.8, 0.5, 0.2)

    # Primeiro triângulo do corpo
    glVertex2f(-0.4, -0.5)
    glVertex2f(0.4, -0.5)
    glVertex2f(0.4, 0.2)

    # Segundo triângulo do corpo
    glVertex2f(-0.4, -0.5)
    glVertex2f(0.4, 0.2)
    glVertex2f(-0.4, 0.2)

    glEnd()

    # Telhado da casa
    glBegin(GL_TRIANGLES)

    glColor3f(0.8, 0.1, 0.1)

    glVertex2f(-0.5, 0.2)
    glVertex2f(0.5, 0.2)
    glVertex2f(0.0, 0.7)

    glEnd()


def executar_composicao():
    pygame.init()

    pygame.display.set_mode(
        (800, 600),
        DOUBLEBUF | OPENGL
    )

    pygame.display.set_caption("Exercício 3 - Composição")

    # Fundo da tela
    glClearColor(0.08, 0.12, 0.22, 1.0)

    relogio = pygame.time.Clock()

    executando = True

    while executando:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                executando = False

        # Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT)

        
        glPushMatrix()

        # Move o quadrado para a esquerda
        glTranslatef(-0.55, 0.25, 0.0)

        # Mantém o tamanho do quadrado
        glScalef(0.45, 0.45, 1.0)

        desenhar_quadrado()

        glPopMatrix()


        
        glPushMatrix()

        # Move o retângulo para a direita
        glTranslatef(0.50, 0.35, 0.0)

        # Escala diferente na horizontal e vertical
        glScalef(0.55, 0.30, 1.0)

        desenhar_quadrado()

        glPopMatrix()



        glPushMatrix()

        # Coloca a casa no centro inferior
        glTranslatef(0.0, -0.35, 0.0)

        # Diminui a casa
        glScalef(0.45, 0.45, 1.0)

        desenhar_casa()

        glPopMatrix()


        # Atualiza a tela
        pygame.display.flip()

        relogio.tick(60)

    pygame.quit()


executar_composicao()