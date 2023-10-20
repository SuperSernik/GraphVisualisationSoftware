from array import *
import os

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

def read_adj_matrix_from_file(filename):
        out_mat = []
        f = open(filename)
        data = f.readlines()
        for i in range(0, len(data)):
            line = data[i]
            line = line.replace("\n", "")
            arr = line.split("\t")
            new_arr = []
            for x in arr:
                 new_arr.append(int(x))
            out_mat.append(new_arr)
            new_arr = []
        f.close()
        return out_mat

mat = [[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]



print(read_adj_matrix_from_file("adj_matrix.csv"))
