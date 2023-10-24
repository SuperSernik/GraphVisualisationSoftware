import pygame 

class Button:

    font_color = (255,255,255) 
    color_light = (170,170,170)
    color_dark = (100,100,100)

    width = 150
    height = 50 

    text_x_offset = 10
    text_y_offset = 10

    def __init__(self, id, pos: pygame.Vector2, text="None") -> None:
        self.id = id
        self.x, self.y = pos.xy
        self.smallfont = pygame.font.SysFont('Corbel',35) 
        self.text = self.smallfont.render(text, True, self.font_color)     

    def Update(self, dt):
        pass

    def Draw(self, screen):
        self.change_color_on_hover(screen)
        screen.blit(self.text , (self.x + self.text_x_offset, self.y + self.text_y_offset)) 

    def has_collided(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()      
        if(mouse_x >= self.x and mouse_x <= self.x + self.width and
           mouse_y >= self.y and mouse_y <= self.y + self.height):
            return True
        return False
    
    def change_color_on_hover(self, screen):
        if self.has_collided(): pygame.draw.rect(screen, self.color_light, [self.x, self.y, self.width, self.height])       
        else:                   pygame.draw.rect(screen, self.color_dark, [self.x, self.y, self.width, self.height]) 

    def clicked_button(self):
        left, mid, right = pygame.mouse.get_pressed(num_buttons=3)
        if(left):
            if self.has_collided(): 
                return True
        return False

  
