import math
import pygame
import random
import copy

X_RES = 1600
Y_RES = 900  

NODE_COUNT = 12
NODE_RADIUS = 30
RANDOM_PATH_LENGTH = 12

NODES_FILE_NAME_PATH = "saves\\SAVED_NODES.csv"
ADJ_MATRIX_FILE_NAME_PATH = "saves\\SAVED_MAT.csv"

SAVED_NODES_FILE_PATH = "saves\\SAVED_NODES.csv"
SAVED_ADJ_MAT_FILE_PATH = "saves\\SAVED_MAT.csv"

COLORS = ["black", "blue", "cyan", "gold", "gray", "green", 
          "orange", "purple", "red", "violet", "yellow", "white"]

PATH_COLOR = "red"
EDGE_COLOR = "white"