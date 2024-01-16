# Floyd Warshall Algorithm
import graph_data as gd
INF = 9999 #used for infinity purposes

#first step is to create the matrix of the origional distance based on the graph data
def create_graph_matrix(graph_index):
    graph_array = gd.graph_data[graph_index]
    num_vertices = len(graph_array)

    graph_matrix = []
    for _ in range(num_vertices):
        row = [INF] * num_vertices
        graph_matrix.append(row)

    for i in range(num_vertices):
        graph_matrix[i][i] = 0
        for neighbor in graph_array[i][1]:
            x1, y1 = graph_array[i][0]
            x2, y2 = graph_array[neighbor][0]
            distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 #getting distance between cordinates
            graph_matrix[i][neighbor] = distance #update matrix
    
    return graph_matrix, num_vertices

#update the matrix using flyd warshall to update the distance matrix
def floyd_warshall(matrix):
    distance = []

    for i in matrix:
        inner_list = []
        for j in i:
            inner_list.append(j)
        distance.append(inner_list)
    
    #triple for loops
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance

#print the array in a matrix form to the console
def print_solution(distance):
    for i in range(vertices):
        for j in range(vertices):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


def build_paths(distance):
    parent = [[-1] * vertices for _ in range(vertices)]

    for i in range(vertices):
        for j in range(vertices):
            if i != j and distance[i][j] != INF:
                parent[i][j] = i

    return parent

def print_paths(parent, start, end):
    if parent[start][end] == -1:
        print(f"No path from {start} to {end}")
        return

    path = [end]
    while parent[start][end] != start:
        path.append(parent[start][end])
        end = parent[start][end]

    path.append(start)
    path.reverse()
    print("Shortest path:", " -> ", (map(str, path)))

#Main -- Broken up into three different functions.
graph_index_to_use = 0  #Update this based on the graph data graph you want to use since we are not running the entire program. 
matrix, vertices = create_graph_matrix(graph_index_to_use)
updated_matrix = floyd_warshall(matrix)
print_solution(updated_matrix)

#build and print path taken with distances
parent_matrix = build_paths(updated_matrix)
print_paths(parent_matrix, 0, vertices - 1)