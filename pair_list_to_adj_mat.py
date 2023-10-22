NODE_COUNT = 12
node_ids = ["a", "b", "c", "d", "e", "f", "g", "h", "i" ,"j", "k", "l"]


def from_connections_to_adj_matrix(connections):
    out_path_matrix = [[0 for i in range(0, NODE_COUNT)] for i in range(0, NODE_COUNT)]
    for i in range(0, len(connections)):
        start, end = connections[i][0], connections[i][1]
        x = node_ids.index(start)
        y = node_ids.index(end)
        out_path_matrix[x][y] = 1
        out_path_matrix[y][x] = 1
    return out_path_matrix

def write_mat_to_file(mat):
    f = open("saved_mat.csv", "w")
    for i in range(len(mat)):
        for j in range(len(mat)):
            if(j == len(mat)-1):
                f.write(str(mat[i][j]))
            else:
                f.write(str(mat[i][j]) + ",")
        f.write("\n")
    f.close()



def main():
    inputting = True
    connections = []
    while(inputting):
        data = input("Input a pair: ")

        if(data == "done"):
            matX = from_connections_to_adj_matrix(connections)
            write_mat_to_file(matX)
            print("Saved file!")
            inputting = False
        else:  
            conn = [data[0], data[1]]
            connections.append(conn)
            print(f"start: {conn[0]}, end: {conn[1]}")
            

main()