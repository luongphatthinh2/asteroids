# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # create group
    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # create AsteroidField 
    asteroid_field = AsteroidField()
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # define behavior of player , asteroids, and asteroid field
        updatable.update(dt)

        # check collision
        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")
        
        # draw player and asteroids
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() 

        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()