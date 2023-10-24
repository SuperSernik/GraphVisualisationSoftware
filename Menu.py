from Globals import *
from Button import Button
from App import App
import sys



class Menu:
    buttons = []

    def __init__(self) -> None:
        self.quit_button = Button(0, pygame.Vector2(0, 0), text="Quit")
        self.save_button = Button(1, pygame.Vector2(0, 50), text="Save")
        self.load_button = Button(2, pygame.Vector2(0, 100), text="Load")

        self.buttons.append(self.quit_button)
        self.buttons.append(self.save_button)
        self.buttons.append(self.load_button)


    def Update(self, dt, myapp: App):
    
        if (self.quit_button.clicked_button()):
            print("~Quitting~")
            sys.exit()
            
        if(self.save_button.clicked_button()): 
            print("~Saving~")
            myapp.save_nodes_to_file()

        if(self.load_button.clicked_button()):
            print("~Loading~")
            myapp.load_nodes_from_saves()


    def Draw(self, screen):
        for button in self.buttons: button.Draw(screen)