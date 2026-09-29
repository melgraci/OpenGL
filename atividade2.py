import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *


def executar_primitivas():
    pygame.init()

    
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Exercício 2 - Primitivas")

    
    glClearColor(0.08, 0.12, 0.22, 1.0)

    relogio = pygame.time.Clock()
    executando = True

    while executando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

        
        glClear(GL_COLOR_BUFFER_BIT)


        
        glPointSize(15.0)

        glBegin(GL_POINTS)

        # Cor amarela
        glColor3f(1.0, 1.0, 0.0)

        # Posição do ponto
        glVertex2f(-0.70, 0.65)

        glEnd()


        
        glLineWidth(5.0)

        glBegin(GL_LINES)

        # Primeiro ponto da linha
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(-0.70, 0.45)

        # Segundo ponto da linha
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(0.20, -0.20)

        glEnd()



        glBegin(GL_TRIANGLES)

        # Vértice 1 - verde
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(-0.60, -0.60)

        # Vértice 2 - azul
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(-0.10, -0.60)

        # Vértice 3 - vermelho
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(-0.35, -0.10)

        glEnd()


       
        glBegin(GL_TRIANGLES)

        # Vértice 1 - azul
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(0.25, -0.60)

        # Vértice 2 - vermelho
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(0.75, -0.60)

        # Vértice 3 - verde
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(0.50, -0.10)

        glEnd()


        # Atualiza a tela
        pygame.display.flip()

        relogio.tick(60)

    pygame.quit()


executar_primitivas()