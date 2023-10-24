import math
import pygame
import random

X_RES = 1600
Y_RES = 900  

NODE_COUNT = 12
NODE_RADIUS = 30

NODES_FILE_NAME_PATH = "saves\\nodes_map.csv"
ADJ_MATRIX_FILE_NAME_PATH = "saves\\adj_matrix_map.csv"

COLORS = ["black", "blue", "cyan", "gold", "gray", "green", 
          "orange", "purple", "red", "violet", "yellow", "white"]

PATH_COLOR = "red"
EDGE_COLOR = "white"