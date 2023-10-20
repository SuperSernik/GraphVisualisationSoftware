import pygame
import random
import math

NODE_RADIUS = 30

class Node:

    def __init__(self, id = "x", color="white", pos=pygame.Vector2(100, 100)):
        self.id = "ID: " + id
        self.radius = NODE_RADIUS
        self.pos = pos
        self.color = color
             

    def Update(self, dt):
        self.drag_and_move()
            

    def Draw(self, screen): 
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        self.write_text(screen)

    def has_collided(self):
        x, y = pygame.mouse.get_pos()
        dist = math.sqrt((x-self.pos.x)**2+(y-self.pos.y)**2)
        if(dist < self.radius): return True
        return False
        
    def write_text(self, screen):
        font = pygame.font.SysFont("Arial", 20)
        txtsurf = font.render(self.id, True, "black")
        screen.blit(txtsurf, (self.pos.x - 20, self.pos.y - 10))

    def drag_and_move(self):
        left, mid, right = pygame.mouse.get_pressed(num_buttons=3)
        if(self.has_collided() and left):         
            self.pos.xy = pygame.mouse.get_pos()

