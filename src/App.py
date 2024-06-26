from Globals import *
from Node import Node
from copy import deepcopy
from Util import Queue

class App:

    nodes: list = []
    node_ids: list = []
    adj_matrix = [[]]
    path_matrix = [[]]
    map_path = ["a", "e", "i", "j", "h", "l"]
    circle_path = ["a", "b", "c", "e"]
    tree_path = ["a", "c", "h", "k", "j"]
    path = []

    def _init_(self):
        pass
            
    def Load(self):
        self.nodes = self.read_nodes_from_file(NODES_FILE_NAME_PATH)
        self.adj_matrix = self.read_adj_matrix_from_file(ADJ_MATRIX_FILE_NAME_PATH)
        self.path_matrix = self.apply_path_to_path_matrix(self.path)
        
    def Update(self, dt):
        for node in self.nodes: node.Update(dt)
        self.input_manager()
        
    def Draw(self, screen):
        self.draw_edges(screen)
        for node in self.nodes: node.Draw(screen)

    def draw_edges(self, screen):
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                if(self.adj_matrix[i][j] != 0):
                    if(i == j):
                        self.draw_self_loop(screen, i, j)
                        self.draw_weights_for_self_loops(screen, i, j)
                    else:
                        line_color = self.get_edge_color_for_path(i, j)
                        pygame.draw.line(screen, line_color, self.nodes[i].pos, self.nodes[j].pos, width=3)
                        self.draw_weights_for_edges(screen, i, j)

    def draw_self_loop(self, screen, i, j):
        rect_h = 90
        rect_w = 80
        node_rect = pygame.Rect(self.nodes[i].pos.x-(rect_w/2), 
                                self.nodes[i].pos.y-(rect_h/2)-40, 
                                rect_w, rect_h)
        pygame.draw.ellipse(screen, "white", node_rect, width=3)

    def draw_weights_for_edges(self, screen, i, j):
        font = pygame.font.SysFont("Arial", 30)
        mid_line_pos = pygame.Vector2((self.nodes[i].pos.x + self.nodes[j].pos.x)/2,
                                      (self.nodes[i].pos.y + self.nodes[j].pos.y)/2)

        txtsurf = font.render(str(self.adj_matrix[i][j]), True, "grey")
        screen.blit(txtsurf, mid_line_pos)

    def draw_weights_for_self_loops(self, screen, i, j):
        x_offset = 10
        y_offset = 105
        font = pygame.font.SysFont("Arial", 30)
        txtsurf = font.render(str(self.adj_matrix[i][j]), True, "grey")
        mid_loop_pos = pygame.Vector2(self.nodes[i].pos.x-x_offset,
                                      self.nodes[i].pos.y-y_offset)
        screen.blit(txtsurf, mid_loop_pos)

    def get_edge_color_for_path(self, i, j):
        if(self.path_matrix[i][j] == 1):
            return PATH_COLOR
        else:
            return EDGE_COLOR

    def apply_path_to_path_matrix(self, path):
        '''
        TODO: The path matrix will still draw to the screen patchy
                even if the nodes arent connected. Fix this.
        '''
        out_path_matrix = [[0 for i in range(0, NODE_COUNT)] for i in range(0, NODE_COUNT)]
        for i in range(1, len(path)):
            start, end = path[i-1], path[i]
            x = self.node_ids.index(start)
            y = self.node_ids.index(end)
            out_path_matrix[x][y] = 1
            out_path_matrix[y][x] = 1
        return out_path_matrix


    def input_manager(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.adj_matrix = self.create_random_adj_matrix(NODE_COUNT)
        
        if keys[pygame.K_s]:
            print("Saving")
            self.save_nodes_to_file()

        if keys[pygame.K_l]:
            self.nodes = self.read_nodes_from_file(SAVED_NODES_FILE_PATH)

        if keys[pygame.K_r]:
            self.path = self.create_random_path(RANDOM_PATH_LENGTH)
            self.path_matrix = self.apply_path_to_path_matrix(self.path)


    
    def create_random_adj_matrix(self, number_of_nodes):
        out_matrix = [[0 for x in range(number_of_nodes)] for y in range(number_of_nodes)] 
        for i in range(number_of_nodes):
            for j in range(number_of_nodes):
                if(out_matrix[i][j] == 0):
                    out_matrix[i][j] = random.randint(0, 2)
        return out_matrix
    
    def create_random_path(self, lenght):
        ids: list = deepcopy(self.node_ids)
        out_path: list = []
        
        for i in range(0, lenght):
           random_step = random.choice(ids)
           ids.remove(random_step)
           out_path.append(random_step)

        return out_path

    
    def read_nodes_from_file(self, filename):
        self.node_ids = [] # otherwise it duplicates itself
        out_nodes = []
        f = open(filename)
        data = f.readlines()
        for i in range(1, len(data)):
            line = data[i]
            line = line.replace("\n", "")
            arr = line.split(",")
            new_node = Node(id=arr[0], color=arr[1], pos=pygame.Vector2(int(arr[2]),int(arr[3])))
            self.node_ids.append(arr[0])
            out_nodes.append(new_node)
        f.close()
        return out_nodes
    
    def read_adj_matrix_from_file(self, filename):
        out_mat = []
        f = open(filename)
        data = f.readlines()
        for i in range(0, len(data)):
            line = data[i]
            line = line.replace("\n", "")
            arr = line.split(",")
            new_arr = []
            for x in arr:
                 new_arr.append(int(x))
            out_mat.append(new_arr)
            new_arr = []
        f.close()
        return out_mat
    
    def save_nodes_to_file(self):
        f = open(SAVED_NODES_FILE_PATH, "w")
        lines = []
        lines.append("ID,color,xpos,ypos\n")

        for node in self.nodes:
            line = f"{node.id},{node.color},{int(node.pos.x)},{int(node.pos.y)}\n"
            lines.append(line)

        f.writelines(lines)
        f.close()

    def save_adj_mat_to_file(self):
        f = open(SAVED_ADJ_MAT_FILE_PATH, "w")
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                if(j == len(self.adj_matrix)-1):
                    f.write(str(self.adj_matrix[i][j]))
                else:
                    f.write(str(self.adj_matrix[i][j]) + ",")
            f.write("\n")
        f.close()

    def load_from_saves(self):
        self.nodes = self.read_nodes_from_file(SAVED_NODES_FILE_PATH)
        self.adj_matrix = self.read_adj_matrix_from_file(SAVED_ADJ_MAT_FILE_PATH)

    def load_node_and_mat_templates(self, template):
        if template == "circle":
            self.nodes = self.read_nodes_from_file("saves\\nodes_circle.csv")
            self.adj_matrix = self.read_adj_matrix_from_file("saves\\adj_matrix_circle.csv")
            self.apply_path_to_path_matrix(self.path)

        if template == "map":
            self.nodes = self.read_nodes_from_file("saves\\nodes_map.csv")
            self.adj_matrix = self.read_adj_matrix_from_file("saves\\adj_matrix_map.csv")
            self.apply_path_to_path_matrix(self.path)

        if template == "tree":
            self.nodes = self.read_nodes_from_file("saves\\nodes_tree.csv")
            self.adj_matrix = self.read_adj_matrix_from_file("saves\\adj_matrix_tree.csv")
            self.apply_path_to_path_matrix(self.path)
    
    # Function below help with pathfinding

    def dijkstra_pathfind(self, startnode, endnode):
        out_path = []
        dist_from_startnode = [9999 for i in range(len(self.nodes))]
        prev_node = ["" for i in range(len(self.nodes))]
        node_queue = Queue()
        for node in self.node_ids:
            Queue.enQ(node)



        return out_path
    
    def get_weight_by_ids(self, start, end):
        out_weight = 9999
        row = self.node_ids.index(start)
        col = self.node_ids.index(end)
        if(self.adj_matrix[row][col] == 0):
            return out_weight
        else:
            return self.adj_matrix[row][col]
        

    def get_nodes_connected_to_a_node(self, root_node):
        out_nodes = []
        row = self.node_ids.index(root_node)
        for i in range(len(self.adj_matrix[row])):
            if(self.adj_matrix[row][i] != 0):
                out_nodes.append(self.node_ids[i])
        return out_nodes

        
    

        

if __name__ == "__main__":
    app = App()
    app.Load()
    print(app.get_nodes_connected_to_a_node("g"))
    print(["" for i in range(len(app.nodes))])
    