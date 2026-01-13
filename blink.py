import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Get display info
display_info = pygame.display.Info()
SCREEN_WIDTH = display_info.current_w
SCREEN_HEIGHT = display_info.current_h

# Create fullscreen window
screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT),
    pygame.FULLSCREEN
)

pygame.display.set_caption("Blink Simulator")

clock = pygame.time.Clock()

# Blink configuration
blink_speed = 40          # pixels per frame
pause_closed = 0.08       # seconds eyes stay closed
pause_open = 1.2          # seconds between blinks

black = (0, 0, 0)

def blink():
    # Closing
    height = 0
    while height < SCREEN_HEIGHT // 2:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        pygame.draw.rect(
            screen, black,
            (0, 0, SCREEN_WIDTH, height)
        )
        pygame.draw.rect(
            screen, black,
            (0, SCREEN_HEIGHT - height, SCREEN_WIDTH, height)
        )

        pygame.display.flip()
        height += blink_speed
        clock.tick(60)

    time.sleep(pause_closed)

    # Opening
    while height > 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        pygame.draw.rect(
            screen, black,
            (0, 0, SCREEN_WIDTH, height)
        )
        pygame.draw.rect(
            screen, black,
            (0, SCREEN_HEIGHT - height, SCREEN_WIDTH, height)
        )

        pygame.display.flip()
        height -= blink_speed
        clock.tick(60)

# Main loop
while True:
    blink()
    time.sleep(pause_open)
