import pygame 
import sys 




class Button:

    font_color = (255,255,255) 
    color_light = (170,170,170)
    color_dark = (100,100,100)

    width = 100
    height = 50 

    def __init__(self, pos: pygame.Vector2) -> None:
        self.pos = pos
        self.smallfont = pygame.font.SysFont('Corbel',35) 
        self.text = self.smallfont.render('quit' , True , self.font_color)     


    def Update(dt):
        for ev in pygame.event.get():
             if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit()

    def Draw(screen):
        mouse = pygame.mouse.get_pos() 

        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
            pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
            
        else: 
            pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
        
        # superimposing the text onto our button 
        screen.blit(text , (width/2+50,height/2)) 





  
