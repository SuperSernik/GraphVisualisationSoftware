from Globals import *
from App import App
from Button import Button
from Menu import Menu

pygame.init()

myapp = App()
myapp.Load()

mymenu = Menu()

screen = pygame.display.set_mode((X_RES, Y_RES))
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill("black")

    myapp.Update(dt)
    myapp.Draw(screen)

    mymenu.Update(dt, myapp)
    mymenu.Draw(screen)


    pygame.display.flip()

    dt = clock.tick() / 1000
    pygame.display.set_caption(f"FPS: {clock.get_fps():.2f}")
    
pygame.quit()

