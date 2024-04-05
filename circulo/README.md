#El circulo con ia
#María Juliana Alzate Saavedra 20232020082

- prompt 1: crea un codigo de python en pygame con un circulo dibujado de 50x50 dentro de una pantalla de 900 x 700, haz que el circulo se mueva al presionar las teclas up, right, left, down

Resultado:  
    Aquí tienes un código en Python utilizando Pygame que crea una ventana de 900x700 píxeles con un círculo de 50x50 píxeles. El círculo se puede mover utilizando las teclas de dirección:

python
Copy code
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

# Definir dimensiones y posición inicial del círculo
CIRCLE_SIZE = 50
circle_x = (SCREEN_WIDTH - CIRCLE_SIZE) // 2
circle_y = (SCREEN_HEIGHT - CIRCLE_SIZE) // 2

# Configurar la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movimiento de círculo con Pygame")

clock = pygame.time.Clock()

# Loop principal
running = True
while running:
    screen.fill(WHITE)  # Limpiar la pantalla con color blanco

    # Dibujar el círculo
    pygame.draw.circle(screen, BLACK, (circle_x, circle_y), CIRCLE_SIZE // 2)

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Mover el círculo según las teclas presionadas
            if event.key == pygame.K_UP:
                circle_y -= 10
            elif event.key == pygame.K_DOWN:
                circle_y += 10
            elif event.key == pygame.K_LEFT:
                circle_x -= 10
            elif event.key == pygame.K_RIGHT:
                circle_x += 10

    # Limitar la velocidad del bucle
    clock.tick(30)

pygame.quit()
sys.exit()
Este código crea una ventana de Pygame de 900x700 píxeles y dibuja un círculo negro de 50x50 píxeles en el centro de la ventana. El círculo puede moverse hacia arriba, abajo, izquierda y derecha usando las teclas de dirección.


- prompt 2: ahora haz que se mueva el circulo constantemente si dejo presionada alguna de las teclas

Resultado: import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

# Definir dimensiones y posición inicial del círculo
CIRCLE_SIZE = 50
circle_x = (SCREEN_WIDTH - CIRCLE_SIZE) // 2
circle_y = (SCREEN_HEIGHT - CIRCLE_SIZE) // 2

# Configurar la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movimiento de círculo con Pygame")

clock = pygame.time.Clock()

# Diccionario para rastrear el estado de las teclas
keys_pressed = {pygame.K_UP: False, pygame.K_DOWN: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}

# Loop principal
running = True
while running:
    screen.fill(WHITE)  # Limpiar la pantalla con color blanco

    # Actualizar la posición del círculo si se presiona alguna tecla
    if keys_pressed[pygame.K_UP]:
        circle_y -= 5
    if keys_pressed[pygame.K_DOWN]:
        circle_y += 5
    if keys_pressed[pygame.K_LEFT]:
        circle_x -= 5
    if keys_pressed[pygame.K_RIGHT]:
        circle_x += 5

    # Dibujar el círculo
    pygame.draw.circle(screen, BLACK, (circle_x, circle_y), CIRCLE_SIZE // 2)

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Registrar las teclas presionadas
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            # Registrar las teclas liberadas
            if event.key in keys_pressed:
                keys_pressed[event.key] = False

    # Limitar la velocidad del bucle
    clock.tick(30)

pygame.quit()
sys.exit()


- prompt 3: Ahora haz que  el círculo excede los bordes de la pantalla por arriba, abajo, izquierda o derecha, aparecerá en el lado opuesto de la pantalla en la misma posición de x o y según corresponda.

resultado:
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

# Definir dimensiones y posición inicial del círculo
CIRCLE_SIZE = 50
circle_x = (SCREEN_WIDTH - CIRCLE_SIZE) // 2
circle_y = (SCREEN_HEIGHT - CIRCLE_SIZE) // 2

# Configurar la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movimiento de círculo con Pygame")

clock = pygame.time.Clock()

# Diccionario para rastrear el estado de las teclas
keys_pressed = {pygame.K_UP: False, pygame.K_DOWN: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}

# Loop principal
running = True
while running:
    screen.fill(WHITE)  # Limpiar la pantalla con color blanco

    # Actualizar la posición del círculo si se presiona alguna tecla
    if keys_pressed[pygame.K_UP]:
        circle_y -= 5
        if circle_y < 0:  # Si excede por arriba, aparece abajo en la misma posición de x
            circle_y = SCREEN_HEIGHT - CIRCLE_SIZE
    if keys_pressed[pygame.K_DOWN]:
        circle_y += 5
        if circle_y > SCREEN_HEIGHT - CIRCLE_SIZE:  # Si excede por abajo, aparece arriba en la misma posición de x
            circle_y = 0
    if keys_pressed[pygame.K_LEFT]:
        circle_x -= 5
        if circle_x < 0:  # Si excede por la izquierda, aparece por la derecha en la misma posición de y
            circle_x = SCREEN_WIDTH - CIRCLE_SIZE
    if keys_pressed[pygame.K_RIGHT]:
        circle_x += 5
        if circle_x > SCREEN_WIDTH - CIRCLE_SIZE:  # Si excede por la derecha, aparece por la izquierda en la misma posición de y
            circle_x = 0

    # Dibujar el círculo
    pygame.draw.circle(screen, BLACK, (circle_x, circle_y), CIRCLE_SIZE // 2)

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Registrar las teclas presionadas
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            # Registrar las teclas liberadas
            if event.key in keys_pressed:
                keys_pressed[event.key] = False

    # Limitar la velocidad del bucle
    clock.tick(30)

pygame.quit()
sys.exit()

- promt 4: no me sale el circulo al lado opuesto cuando excede la pantalla, modifica el codigo para que cuando salga de la pantalla por un lado salga por el lado opuesto

resultado 
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

# Definir dimensiones y posición inicial del círculo
CIRCLE_SIZE = 50
circle_x = (SCREEN_WIDTH - CIRCLE_SIZE) // 2
circle_y = (SCREEN_HEIGHT - CIRCLE_SIZE) // 2

# Configurar la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movimiento de círculo con Pygame")

clock = pygame.time.Clock()

# Diccionario para rastrear el estado de las teclas
keys_pressed = {pygame.K_UP: False, pygame.K_DOWN: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}

# Loop principal
running = True
while running:
    screen.fill(WHITE)  # Limpiar la pantalla con color blanco

    # Actualizar la posición del círculo si se presiona alguna tecla
    if keys_pressed[pygame.K_UP]:
        circle_y -= 5
        if circle_y < -CIRCLE_SIZE:  # Si el círculo excede por arriba, aparece abajo en la misma posición de x
            circle_y = SCREEN_HEIGHT
    if keys_pressed[pygame.K_DOWN]:
        circle_y += 5
        if circle_y > SCREEN_HEIGHT:  # Si el círculo excede por abajo, aparece arriba en la misma posición de x
            circle_y = -CIRCLE_SIZE
    if keys_pressed[pygame.K_LEFT]:
        circle_x -= 5
        if circle_x < -CIRCLE_SIZE:  # Si el círculo excede por la izquierda, aparece por la derecha en la misma posición de y
            circle_x = SCREEN_WIDTH
    if keys_pressed[pygame.K_RIGHT]:
        circle_x += 5
        if circle_x > SCREEN_WIDTH:  # Si el círculo excede por la derecha, aparece por la izquierda en la misma posición de y
            circle_x = -CIRCLE_SIZE

    # Dibujar el círculo
    pygame.draw.circle(screen, BLACK, (circle_x, circle_y), CIRCLE_SIZE // 2)

    # Actualizar la pantalla
    pygame.display.flip()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Registrar las teclas presionadas
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            # Registrar las teclas liberadas
            if event.key in keys_pressed:
                keys_pressed[event.key] = False

    # Limitar la velocidad del bucle
    clock.tick(30)

pygame.quit()
sys.exit()
