from random import randint

import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_rect = mole_image.get_rect(topleft=(0,0))  # Set mole's position on the screen
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
                    mouse_x, mouse_y = event.pos
                    if mole_rect.collidepoint(mouse_x, mouse_y):  # Check if click is inside mole image
                        new_x = random.randint(0, 20)  # Random x position within screen width
                        new_y = random.randint(0, 16)  # Random y position within screen height
                        mole_rect.topleft = (new_x * 32, new_y * 32)  # Update mole's position
            screen.fill("light green")
            pygame.draw.line(screen, (0, 0, 0), (32, 0), (32, 512))
            for i in range(20):
                pygame.draw.line(screen, (0, 0, 0), (32*i, 0), (32*i, 512))
            for i in range(16):
                pygame.draw.line(screen, (0, 0, 0), (0, 32*i), (640,32 * i))

            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
