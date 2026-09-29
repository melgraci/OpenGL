import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *


# Desenha um triângulo colorido
def desenhar_triangulo():
    glBegin(GL_TRIANGLES)

    # Vértice 1 - vermelho
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.45, -0.35)

    # Vértice 2 - verde
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.45, -0.35)

    # Vértice 3 - azul
    glColor3f(0.0, 0.3, 1.0)
    glVertex2f(0.0, 0.45)

    glEnd()


def executar_transformacoes():
    pygame.init()

    pygame.display.set_mode(
        (800, 600),
        DOUBLEBUF | OPENGL
    )

    pygame.display.set_caption("Exercício 4 - Transformações")

    # Cor de fundo
    glClearColor(0.08, 0.12, 0.22, 1.0)

    relogio = pygame.time.Clock()

    angulo = 0.0

    executando = True

    while executando:

        # Controla o tempo da animação
        delta = relogio.tick(60) / 1000.0

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                executando = False

        # ==========================================
        # 1. ROTAÇÃO
        # ==========================================

        # Valor negativo = gira no sentido contrário
        angulo = (angulo - 120.0 * delta) % 360.0

        # Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT)

        # ==========================================
        # 2. TRANSFORMAÇÕES
        # ==========================================

        glPushMatrix()

        # Primeiro fazemos a translação
        glTranslatef(0.25, 0.0, 0.0)

        # Depois fazemos a rotação
        glRotatef(angulo, 0.0, 0.0, 1.0)

        # Escala diferente da versão anterior
        glScalef(0.60, 0.60, 1.0)

        desenhar_triangulo()

        glPopMatrix()

        # Mostra a cena
        pygame.display.flip()

    pygame.quit()


executar_transformacoes()