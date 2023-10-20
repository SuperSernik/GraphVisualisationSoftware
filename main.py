import pygame
import time
from App import App

MOUSE_IN_USE = False

X_RES = 1600
Y_RES = 900  

pygame.init()

myapp = App()
myapp.Load()


screen = pygame.display.set_mode((X_RES, Y_RES))
clock = pygame.time.Clock()
running = True
dt = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    myapp.Update(dt)
    myapp.Draw(screen)


    pygame.display.flip()


    dt = clock.tick() / 1000
    pygame.display.set_caption(f"FPS: {clock.get_fps():.2f}")
    
    

pygame.quit()

