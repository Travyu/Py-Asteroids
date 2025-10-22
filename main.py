import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    # creating groups for the player
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # creating a player container for the groups
    Player.containers = (updatable, drawable)

    # instantiate the player object after the container to group players
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # creating group for asteroids
    asteroids = pygame.sprite.Group()

    # creating a asteroid container for the group
    Asteroid.containers = (asteroids, updatable, drawable)

    # creating a asteroidfield container
    AsteroidField.containers = (updatable)

    # instantiate a asteroidfield object
    AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        
if __name__ == "__main__":
    main()
