from Node import Node
import pygame
import random

NODE_COUNT = 5

class App:
    nodes = []

    Xadj_matrix = [[0,0,1,0,0,0],
                  [1,0,0,0,0,0],
                  [0,0,0,0,0,0],
                  [0,1,0,0,0,0],
                  [0,1,0,0,0,0],
                  [0,0,0,1,0,0]]
    
    adj_matrix = [[]]

    def _init_(self):
        self.nodes = []
        
    def Load(self):
        for i in range(NODE_COUNT):
            node = Node(id=str(i))
            self.nodes.append(node) 

        self.adj_matrix = self.create_adj_matrix(NODE_COUNT)

    def Update(self, dt):
        for node in self.nodes:
            node.Update(dt)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.adj_matrix = self.create_adj_matrix(NODE_COUNT)



    def Draw(self, screen):
        self.draw_lines(screen)

        for i in range(len(self.nodes)):
            self.nodes[i].Draw(screen)  

            

    def draw_lines(self, screen):
        font = pygame.font.SysFont("Arial", 30)

        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                if(self.adj_matrix[i][j] != 0):
                    if(i == j):
                        rect_h = 90
                        rect_w = 80
                        node_rect = pygame.Rect(self.nodes[i].pos.x-(rect_w/2), 
                                                self.nodes[i].pos.y-(rect_h/2)-40, 
                                                rect_w, rect_h)
                        pygame.draw.ellipse(screen, "white", node_rect, width=3)
                        
                        txtsurf = font.render(str(self.adj_matrix[i][j]), True, "grey")
                        mid_loop_pos = pygame.Vector2(self.nodes[i].pos.x-10,
                                                      self.nodes[i].pos.y-rect_h+15)
                        screen.blit(txtsurf, mid_loop_pos)

                    else:
                        pygame.draw.line(screen, "white", self.nodes[i].pos, self.nodes[j].pos, width=3)

                        mid_line_pos = pygame.Vector2((self.nodes[i].pos.x + self.nodes[j].pos.x)/2,
                                                    (self.nodes[i].pos.y + self.nodes[j].pos.y)/2)

                        txtsurf = font.render(str(self.adj_matrix[i][j]), True, "grey")
                        screen.blit(txtsurf, mid_line_pos)
    
    def create_adj_matrix(self, n):
        out_matrix = [[0 for x in range(n)] for y in range(n)] 
        print(out_matrix)
        for i in range(n):
            for j in range(n):
                if(out_matrix[i][j] == 0):
                    out_matrix[i][j] = random.randint(0, 1)
        return out_matrix

        
        

if __name__ == "__main__":
    ...