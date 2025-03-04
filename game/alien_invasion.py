import sys

import pygame
from settings import Settings


def run_game():
    pygame.init()
    s = Settings()
    screen = pygame.display.set_mode((s.screen_width, s.screen_height))
    pygame.display.set_caption("Alien Invasion")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(s.bg_color)
        pygame.display.flip()


run_game()
