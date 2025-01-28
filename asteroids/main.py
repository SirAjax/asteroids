from constants import *
import pygame


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0,0,0)
    game_clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black, rect=None, special_flags=0) 
        pygame.display.flip()

        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
          main()

