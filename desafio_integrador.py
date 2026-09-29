import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *


# Desenha um triângulo com uma cor diferente em cada vértice
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


# Desenha um quadrado usando dois triângulos
def desenhar_quadrado_com_triangulos():
    glBegin(GL_TRIANGLES)

    glColor3f(1.0, 0.8, 0.0)

    # Primeiro triângulo
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)

    # Segundo triângulo
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)

    glEnd()


def executar_desafio():
    pygame.init()

    pygame.display.set_mode(
        (800, 600),
        DOUBLEBUF | OPENGL
    )

    pygame.display.set_caption("Desafio Integrador - OpenGL")

    # Cor de fundo personalizada
    glClearColor(0.05, 0.08, 0.15, 1.0)

    relogio = pygame.time.Clock()

    # Posição do objeto controlado pelo teclado
    x = 0.0
    y = -0.35

    # Ângulo do objeto que ficará girando
    angulo = 0.0

    executando = True

    while executando:

        # Controla o tempo entre os frames
        delta = relogio.tick(60) / 1000.0

        # Eventos do teclado e da janela
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                executando = False

            # R volta o objeto para a posição inicial
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    x = 0.0
                    y = -0.35

        # Verifica as teclas pressionadas
        teclas = pygame.key.get_pressed()

        velocidade = 0.8 * delta

        # Controle do triângulo pelas setas
        if teclas[pygame.K_LEFT]:
            x -= velocidade

        if teclas[pygame.K_RIGHT]:
            x += velocidade

        if teclas[pygame.K_UP]:
            y += velocidade

        if teclas[pygame.K_DOWN]:
            y -= velocidade

        # Limita o movimento dentro da tela
        x = max(-0.65, min(0.65, x))
        y = max(-0.65, min(0.65, y))

        # Rotação contínua
        angulo = (angulo + 60.0 * delta) % 360.0

        # Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT)

        # =========================
        # OBJETO 1 - QUADRADO
        # =========================
        glPushMatrix()

        # Move o quadrado para a esquerda
        glTranslatef(-0.55, 0.25, 0.0)

        # Diminui o tamanho
        glScalef(0.4, 0.4, 1.0)

        desenhar_quadrado_com_triangulos()

        glPopMatrix()


        # =========================
        # OBJETO 2 - TRIÂNGULO GIRANDO
        # =========================
        glPushMatrix()

        # Move o triângulo para a direita
        glTranslatef(0.45, 0.25, 0.0)

        # Faz o triângulo girar
        glRotatef(angulo, 0.0, 0.0, 1.0)

        # Diminui o tamanho
        glScalef(0.4, 0.4, 1.0)

        desenhar_triangulo()

        glPopMatrix()


        # =========================
        # OBJETO 3 - TRIÂNGULO CONTROLADO
        # =========================
        glPushMatrix()

        # Move conforme as teclas pressionadas
        glTranslatef(x, y, 0.0)

        # Altera o tamanho
        glScalef(0.35, 0.35, 1.0)

        desenhar_triangulo()

        glPopMatrix()


        # Mostra a cena na tela
        pygame.display.flip()

    pygame.quit()


executar_desafio()