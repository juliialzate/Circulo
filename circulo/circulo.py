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
