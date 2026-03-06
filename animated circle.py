import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Circle with Keyboard Control")

# Circle properties
x, y = WIDTH // 2, HEIGHT // 2
radius = 30
speed = 5

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Keep circle inside window
    x = max(radius, min(WIDTH - radius, x))
    y = max(radius, min(HEIGHT - radius, y))

    # Drawing
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), radius)

    pygame.display.flip()

pygame.quit()
sys.exit()