# Example file showing a circle moving on screen
import pygame
import time
from App import App

MOUSE_IN_USE = False

X_RES = 1280
Y_RES = 720

# pygame setup
pygame.init()

myapp = App()
myapp.Load()


screen = pygame.display.set_mode((X_RES, Y_RES))
clock = pygame.time.Clock()
running = True
dt = 0



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # My Logic

    myapp.Update(dt)
    myapp.Draw(screen)


    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick() / 1000
    pygame.display.set_caption(f"FPS: {clock.get_fps():.2f}")
    
    

pygame.quit()

