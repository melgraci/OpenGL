# Atividade OpenGL

## 1. Exercício 1 — Fundo e janela

### 1

Foi utilizada a função `glClearColor(0.15, 0.20, 0.30, 1.0)`.

Valores RGBA:

* R = 0.15
* G = 0.20
* B = 0.30
* A = 1.0

### 2

O canal alfa representa a transparência ou opacidade da cor. O valor `0.0` representa transparência total, enquanto `1.0` representa uma cor totalmente opaca.

### 3

A resolução foi alterada para `1024 × 700` e o título da janela para **"Minha Primeira Cena OpenGL"**.

---

## 2. Exercício 2 — Primitivas

### 1

A posição do ponto foi alterada para `(-0.70, 0.65)` e seu tamanho foi aumentado utilizando `glPointSize(15.0)`.

### 2

A linha foi transformada em diagonal alterando as coordenadas de seus pontos inicial e final.

### 3

As cores dos vértices do triângulo foram alteradas, utilizando vermelho, verde e azul em posições diferentes.

### 4

Foi adicionado um segundo triângulo utilizando `GL_TRIANGLES`, também com cores diferentes em seus vértices.

### 5

As cores aparecem misturadas porque o OpenGL interpola as cores entre os diferentes vértices do triângulo, criando cores intermediárias.

---

## 3. Exercício 3 — Composição

### 1

O quadrado foi formado por dois triângulos, sendo um vermelho e o outro azul.

### 2

Foi utilizada uma escala diferente nos eixos horizontal e vertical com `glScalef()`, transformando o quadrado em um retângulo.

### 3

Foi criada uma casa utilizando dois triângulos para formar o corpo e um terceiro triângulo para formar o telhado.

---

## 4. Exercício 4 — Transformações

### 1

O sentido da rotação foi invertido utilizando um valor negativo para a velocidade angular.

### 2

A velocidade da rotação foi aumentada de `60` para `120` graus por segundo.

### 3

Foi utilizada a escala `0.60` nos eixos X e Y, alterando o tamanho original do triângulo.

### 4

A ordem entre translação e rotação foi alterada para observar a diferença no movimento do objeto.

### 5

A ordem das transformações altera o resultado visual, pois elas são aplicadas sequencialmente. A troca da ordem entre translação e rotação pode alterar a posição e o centro de rotação do objeto.

---

## 5. Exercício 5 — Controle pelo teclado

### 1

A velocidade de movimentação foi alterada para `1.0 * delta`.

### 2

As teclas **A** e **D** foram utilizadas para controlar a rotação do triângulo.

### 3

As teclas **W** e **S** foram utilizadas para aumentar e diminuir a escala do objeto.

### 4

A escala foi limitada entre `0.2` e `2.0` utilizando:

`escala = max(0.2, min(2.0, escala))`

---

## 6. Desafio Integrador

Foi desenvolvida uma cena interativa contendo três objetos:

* um quadrado formado por dois triângulos;
* um triângulo com rotação contínua;
* um triângulo controlado pelo teclado.

A cena possui uma cor de fundo personalizada, cores diferentes nos vértices e utiliza translação, rotação e escala.

O triângulo controlado pode ser movimentado pelas setas direcionais e a tecla **R** restaura sua posição inicial.

---

## 7. Relatório

Foram utilizadas as primitivas `GL_POINTS`, `GL_LINES` e `GL_TRIANGLES`. Os triângulos também foram utilizados para formar quadrados, retângulos e a casa.

Os objetos foram definidos utilizando coordenadas 2D nos eixos X e Y. Os vértices foram definidos por meio da função `glVertex2f(x, y)`.

Foram utilizadas três transformações principais: translação com `glTranslatef()`, rotação com `glRotatef()` e escala com `glScalef()`.

O buffer duplo utiliza dois buffers. Enquanto um é exibido, o outro é utilizado para desenhar a próxima imagem. A troca ocorre com `pygame.display.flip()`, reduzindo a cintilação e deixando a animação mais suave.

A GPU realiza o processamento gráfico, incluindo o desenho das primitivas, aplicação das cores e processamento das transformações, permitindo que os objetos e animações sejam exibidos na tela.
