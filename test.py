from array import *

adj_matrix = [[0,1,0],
            [1,0,1],
            [0,1,0]]

def draw_lines():
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if(adj_matrix[i][j] == 1):
                print(f"I:{i}, J:{j}")

colors = ["red", "blue", "yellow", "purple", "green", "cyan"]
color_i = [x for x in colors]

print(color_i)
draw_lines()
print((1,2) == (1, 2))
