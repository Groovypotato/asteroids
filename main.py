import pygame
from constants import *
from circleshape import *
from player import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    dt = 0 
    g_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        g_color = (12,12,12)
        screen.fill(g_color)
        player.draw(screen)
        player.update(dt)
        pygame.display.flip() 
        dt = (g_clock.tick(60) / 1000)
        

if __name__ == "__main__":

    main()