from Globals import *
from Button import Button
from App import App
import sys

BUTTON_COUNT = 6

class Menu:
    buttons = []

    def __init__(self) -> None:
        self.quit_b     = Button(0, pygame.Vector2(0, 0), text="Quit")
        self.save_b     = Button(1, pygame.Vector2(0, 50), text="Save")
        self.load_b     = Button(2, pygame.Vector2(0, 100), text="Load")
        self.circle_b   = Button(3, pygame.Vector2(0, 150), text="Circle")
        self.map_b      = Button(4, pygame.Vector2(0, 200), text="Map")
        self.tree_b     = Button(5, pygame.Vector2(0, 250), text="Tree")
            
        self.buttons.append(self.quit_b)
        self.buttons.append(self.save_b)
        self.buttons.append(self.load_b)
        self.buttons.append(self.circle_b)
        self.buttons.append(self.map_b)
        self.buttons.append(self.tree_b)



    def Update(self, dt, myapp: App):
    
        if (self.quit_b.clicked_button()):
            print("~Quitting~")
            sys.exit()
            
        if(self.save_b.clicked_button()): 
            print("~Saving~")
            myapp.save_nodes_to_file()
            myapp.save_adj_mat_to_file()

        if(self.load_b.clicked_button()):
            print("~Loading~")
            myapp.load_from_saves()

        if(self.circle_b.clicked_button()):
            print("~Loading Circle~")
            myapp.load_node_and_mat_templates("circle")

        if(self.map_b.clicked_button()):
            print("~Loading map~")
            myapp.load_node_and_mat_templates("map")

        if(self.tree_b.clicked_button()):
            print("~Loading Tree~")
            myapp.load_node_and_mat_templates("tree")


    def Draw(self, screen):
        for button in self.buttons: button.Draw(screen)