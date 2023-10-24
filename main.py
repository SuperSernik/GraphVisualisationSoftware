from src.Globals import *
from src.App import App
from src.Button import Button
from src.Menu import Menu

pygame.init()

pygame_icon = pygame.image.load("icon.png")
pygame.display.set_icon(pygame_icon)

myapp = App()
myapp.Load()

mymenu = Menu()

screen = pygame.display.set_mode((X_RES, Y_RES), pygame.RESIZABLE, pygame.SCALED)
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
    pygame.display.set_caption(f"GraphVisSoft  FPS: {clock.get_fps():.2f}  NODES: {NODE_COUNT}")
    
pygame.quit()

