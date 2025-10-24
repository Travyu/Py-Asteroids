import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    # creating group for asteroids
    asteroids = pygame.sprite.Group()

    # creating group for shot
    shots = pygame.sprite.Group()

    # creating a player container for the groups
    Player.containers = (updatable, drawable)

    # creating a asteroid container for the group
    Asteroid.containers = (asteroids, updatable, drawable)

    # creating a asteroidfield container
    AsteroidField.containers = (updatable)

    #creating a shot container
    Shot.containers = (shots, updatable, drawable)

    # instantiate the player object after the container to group players
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # instantiate a asteroidfield object
    AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game Over!")
                sys.exit()
        
        # fill the game screen to black
        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        
if __name__ == "__main__":
    main()
