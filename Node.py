import pygame
import random
import math
from enum import Enum

X_RES = 1280
Y_RES = 720

NODE_RADIUS = 30

class Node:

    def __init__(self, id = "NODE"):
        colors = ["red", "blue", "yellow", "purple", "green", "cyan"]
        color_i = [x for x in colors]

        self.id = "No." + id
        self.radius = NODE_RADIUS
        self.color = colors[random.randint(0, len(colors)-1)]
        self.pos = pygame.Vector2(random.randint(50, X_RES-50), random.randint(50, Y_RES-50))
        

    def Update(self, dt):
        left, mid, right = pygame.mouse.get_pressed(num_buttons=3)
        if(self.has_collided() and left):         
            self.pos.xy = pygame.mouse.get_pos()
            

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
