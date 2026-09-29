import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *



def desenhar_triangulo():
    glBegin(GL_TRIANGLES)

    # Vermelho
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.45, -0.35)

    # Verde
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.45, -0.35)

    # Azul
    glColor3f(0.0, 0.3, 1.0)
    glVertex2f(0.0, 0.45)

    glEnd()


def executar_teclado():
    pygame.init()

    pygame.display.set_mode(
        (800, 600),
        DOUBLEBUF | OPENGL
    )

    pygame.display.set_caption("Exercício 5 - Controle pelo Teclado")

    # Cor de fundo
    glClearColor(0.08, 0.12, 0.22, 1.0)

    relogio = pygame.time.Clock()

    # Posição do triângulo
    x = 0.0
    y = 0.0

    # Rotação inicial
    angulo = 0.0

    # Escala inicial
    escala = 1.0

    executando = True

    while executando:

        # Tempo entre os frames
        delta = relogio.tick(60) / 1000.0

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                executando = False

            # R restaura os valores iniciais
            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_r:
                    x = 0.0
                    y = 0.0
                    angulo = 0.0
                    escala = 1.0

        # Verifica as teclas pressionadas
        teclas = pygame.key.get_pressed()

        # ==========================================
        # MOVIMENTO
        # ==========================================

        # Velocidade aumentada
        velocidade = 1.0 * delta

        if teclas[pygame.K_LEFT]:
            x -= velocidade

        if teclas[pygame.K_RIGHT]:
            x += velocidade

        if teclas[pygame.K_UP]:
            y += velocidade

        if teclas[pygame.K_DOWN]:
            y -= velocidade


        # ==========================================
        # ROTAÇÃO COM A E D
        # ==========================================

        velocidade_rotacao = 120.0 * delta

        if teclas[pygame.K_a]:
            angulo += velocidade_rotacao

        if teclas[pygame.K_d]:
            angulo -= velocidade_rotacao


        # ==========================================
        # ESCALA COM W E S
        # ==========================================

        velocidade_escala = 0.8 * delta

        if teclas[pygame.K_w]:
            escala += velocidade_escala

        if teclas[pygame.K_s]:
            escala -= velocidade_escala


        # ==========================================
        # LIMITE DA ESCALA
        # ==========================================

        # A escala não pode ser menor que 0.2
        # nem maior que 2.0
        escala = max(0.2, min(2.0, escala))


        # Limita o movimento do triângulo
        x = max(-0.65, min(0.65, x))
        y = max(-0.65, min(0.65, y))


        # Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT)


        # ==========================================
        # APLICA AS TRANSFORMAÇÕES
        # ==========================================

        glPushMatrix()

        # Movimento
        glTranslatef(x, y, 0.0)

        # Rotação
        glRotatef(angulo, 0.0, 0.0, 1.0)

        # Escala
        glScalef(escala, escala, 1.0)

        # Desenha o triângulo
        desenhar_triangulo()

        glPopMatrix()


        # Atualiza a tela
        pygame.display.flip()

    pygame.quit()


executar_teclado()