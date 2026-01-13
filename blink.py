import pygame
import sys
import time
import mss

# ---------- INIT ----------
pygame.init()

info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h

# ---------- SCREEN CAPTURE BEFORE FULLSCREEN ----------
sct = mss.mss()
monitor = sct.monitors[1]  # primary monitor
shot = sct.grab(monitor)
desktop_image = pygame.image.frombuffer(
    shot.rgb,
    (shot.width, shot.height),
    "RGB"
)

# ---------- OPEN FULLSCREEN ----------
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
blink_speed = 40        # pixels per frame
pause_closed = 0.08     # seconds

# ---------- BLINK FUNCTION ----------
def blink_once():
    height = 0

    # ---- CLOSING ----
    while height < HEIGHT // 2:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        screen.blit(desktop_image, (0, 0))
        pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, height))
        pygame.draw.rect(screen, BLACK, (0, HEIGHT - height, WIDTH, height))

        pygame.display.flip()
        height += blink_speed
        clock.tick(60)

    time.sleep(pause_closed)

    # ---- OPENING ----
    while height > 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        screen.blit(desktop_image, (0, 0))
        pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, height))
        pygame.draw.rect(screen, BLACK, (0, HEIGHT - height, WIDTH, height))

        pygame.display.flip()
        height -= blink_speed
        clock.tick(60)


# ---------- RUN ----------
blink_once()
pygame.quit()
sys.exit()
