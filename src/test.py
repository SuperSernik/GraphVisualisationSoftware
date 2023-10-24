from array import *
import os
from copy import deepcopy
import random

adj_matrix = [[0,1,0],
            [1,0,1],
            [0,1,0]]

def draw_lines():
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if(adj_matrix[i][j] == 1):
                #print(f"I:{i}, J:{j}")
                pass

colors = ["red", "blue", "yellow", "purple", "green", "cyan"]
color_i = [x for x in colors]

NODE_IDS = ["a", "b", "c", "d", "e", "f", "g", "h", "i" ,"j", "k", "l"]

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

path_matrix = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]]

NODE_COUNT = 12

matA = [0 for i in range(0, NODE_COUNT)]
matB = [matA for i in range(0, len(matA))]


matX =[[0 for i in range(0, NODE_COUNT)] for i in range(0, NODE_COUNT)]


def create_random_path(lenght):
    ids: list = deepcopy(NODE_IDS)
    out_path: list = []
    
    for i in range(0, lenght):
        random_step = random.choice(ids)
        ids.remove(random_step)
        out_path.append(random_step)

    return out_path

for i in range(20):
     print(create_random_path(8))
     print(set(create_random_path(8)))