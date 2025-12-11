import pygame
import sys

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris Step 1 - Window")
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)  # FPS = 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
