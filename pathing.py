import json
import graph_data
import global_game_data
from numpy import random
from collections import deque
from heapq import heapify, heappush, heappop
import math

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    # Assert Pre-Condition
    assert graph_data.graph_data is not None, "No Graph Data"
    assert graph_data.graph_data[global_game_data.current_graph_index] is not None, "No Graph at index"

    visited = False #Target Visted
    current_graph_data = graph_data.graph_data[global_game_data.current_graph_index]
    start_node = current_graph_data[0]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = current_graph_data[len(current_graph_data) - 1]
    return_path = []
    current_node = start_node
    current_index = 0
    
    while ((current_node != exit_node)):
        current_ajacency_list = current_graph_data[current_index][1]
      
        #Next Node index
        current_index = random.choice(current_ajacency_list)

        #Set visited
        if(current_index == target_node):
            visited = True
  
        #If we have visited the target find the exit -- if not the last one needs to not be the exit.
        if (visited or not visited and current_index != len(current_graph_data) - 1):
            current_node = current_graph_data[current_index]
            return_path.append(current_index)

    # Post-Condition Asserts
    assert visited is True, "Did not hit the target"
    assert current_node is exit_node, "Did not end at the Exit"

    # Returning a list of nodes as the path
    return return_path

def get_dfs_path(graph=None, target=None): #Had to set NONE for unit test purposes
    #Debth first - find all nodes below then move to a different layer
    #Function Varibles
    if graph is not None:
        current_graph_data = graph
    else:
        current_graph_data = graph_data.graph_data[global_game_data.current_graph_index]
    start_node = 0
    if target is not None:
        target_node = target
    else:
        target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(current_graph_data) - 1
    return_path = []

    #Pre-Conditional Asserts 
    assert graph_data.graph_data is not None, "No Graph Data"
    assert target_node is not None, "No Target in graph"
    
    #Subfunction handling start to end.
    def dfs(graph, start, end, visited, path):

        #Pre-Conditional Asserts Cont.
        assert len(graph) > end, "Exit is out of bounds of graph."

        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(start)
        path.append(start)

        if start == end:
            return path

        for neighbor in current_graph_data[start][1]:
            if neighbor not in visited:
                new_path = dfs(graph, neighbor, end, visited, path)
                if new_path:
                    return new_path  

        path.pop()
        return None  

    return_path = dfs(current_graph_data, start_node, target_node, None, None)
    return_path = dfs(current_graph_data, target_node, exit_node, None, return_path[:-1]) #Avoiding duplicates with the middle target
    
    #Post conditional asserts
    assert start_node in return_path, "start is not in the path"
    assert exit_node in return_path, "Exit is not in the path"
    assert target_node in return_path, "Target is not included in path"
    assert isinstance(return_path, list), "Return path is not a list of nodes"
    assert is_path_valid(current_graph_data, return_path), "Path is invalid."

    return return_path


def get_bfs_path(graph=None, target=None): #Had to set NONE for unit test purposes
    #Breath first - search all on the layer before moving down the tree
    #Function Varibles
    if graph is not None:
        current_graph_data = graph
    else:
        current_graph_data = graph_data.graph_data[global_game_data.current_graph_index]
    start_node = 0
    if target is not None:
        target_node = target
    else:
        target_node = global_game_data.target_node[global_game_data.current_graph_index]

    exit_node = len(current_graph_data) - 1
    return_path = []
    
    #Pre-Conditional Asserts 
    assert graph_data.graph_data is not None, "No Graph Data"
    assert target_node is not None, "No Target in graph"

    def bfs(graph, start, end):

        #Pre-Conditional Asserts Cont.
        assert len(graph) > end, "Exit is out of bounds of graph."
        
        visited = set()
        queue = deque([(start, [start])])

        #To avoid duplicates we set this trigger if its the second iteration
        empty_path = False
        if not return_path:
            empty_path = True

        #Go through the Deque as a queue and process them in order
        while queue:
            node, path = queue.popleft()
            visited.add(node)

            #Check if were at the end
            if node == end:
                if empty_path:
                    return_path.extend(path)
                else:
                    return_path.extend(path[1:]) #Avoiding duplicates
                return path
            
            #Loop through neighbors
            for neighbor in graph[node][1]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))

        return []
    
    #Breath-First-Search from start to target and then target to end.
    bfs(current_graph_data, start_node, target_node)
    bfs(current_graph_data, target_node, exit_node)

    #Post conditional asserts
    assert start_node in return_path, "start is not in the path"
    assert exit_node in return_path, "Exit is not in the path"
    assert target_node in return_path, "Target is not included in path"
    assert isinstance(return_path, list), "Return path is not a list of nodes"
    assert is_path_valid(current_graph_data, return_path), "Path is invalid."
    
    return return_path


def get_dijkstra_path(graph=None, target=None):
    if graph is not None:
        current_graph = graph
    else:
        current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    if target is not None:
        target_node = target
    else:
        target_node = global_game_data.target_node[global_game_data.current_graph_index]

    #Get all global data
    positive_infinity = float('inf')
    start_node = current_graph[0]
    start_node_value = 0
    exit_node_value = len(current_graph) - 1
    exit_node = current_graph[exit_node_value]
    return_path = []
    target_hit = False

    #Pre-Conditional Asserts 
    assert graph_data.graph_data is not None, "No Graph Data"
    assert target_node is not None, "No Target in graph"

    #Create a 2d dictionary that hold the nodes
    #Node structure is {Index of node {Distance, Path}}
    node_data = {}
    for i in range(0, len(current_graph)):
        node_data[i] = {'Distance': positive_infinity, 'Path': []}
    node_data[0]['Distance'] = 0 #Set the start node to 0 

    #Setup
    distance_graph = get_distance_dictionary(current_graph)
    visited = []
    min_heap = []
    heappush(min_heap,(0, 0))

    #Main heap while loop to create the bath based on distance
    while min_heap:
        current_distance, current = heappop(min_heap) #Extra Credit: Pops the first one (already sorted with heapq based on distance)
        if current not in visited:
            visited.append(current)
            for j in distance_graph[current]: #Check all neighbors
                if j not in visited:
                    distance = node_data[current]["Distance"] + distance_graph[current][j]
                    if distance < node_data[j]["Distance"]:
                        path = node_data[current]["Path"] + [current]
                        node_data[j] = {'Distance': distance, 'Path': path} #Updates distance and path
                    heappush(min_heap,(node_data[j]["Distance"], j)) #Adds to the heap using distance as its 'priority'
            if current == target_node: 
                target_hit = True
                print("true", current, target_node)
            if(current == exit_node_value and target_hit): 
                return_path = str(node_data[exit_node_value]["Path"] + [exit_node_value])
                print("Shortest Path: " + return_path)
                print("Path Distance: " + str(node_data[exit_node_value]["Distance"]))
                break
        else:
            current = min_heap[0][1] #Distance based priority 
    
    #Fix path concatenation from str to int (I was origionally returning an array as a string this should fix)
    path_int = json.loads(return_path)
    path_int = [int(value) for value in path_int]

    #Post assert statements
    assert path_int[0] == start_node_value, "The result path should begin at the start node."
    assert path_int[-1] == exit_node_value, "The result path should end at the exit node."
    for i in range(len(path_int) - 1):
        assert path_int[i + 1] in distance_graph[path_int[i]], f"Edge missing between {path_int[i]} and {path_int[i + 1]} in the graph."

    return path_int

#Helper function to check the validity of paths following spec outlined 
#'Every pair of sequential vertices in each path are connected by an edge'
def is_path_valid(graph, path):
    for i in range(len(path) - 1):
        current_vertex = path[i]
        next_vertex = path[i + 1]
        if next_vertex not in graph[current_vertex][1]:
            return False
    return True

#Helper function to take in a graph data object and output a dictionary of 
#the calcualted distances between nodes.
def get_distance_dictionary(graph_data):
    result_dict = {}
    for  i,node_data in enumerate(graph_data):
        current_node = node_data[0]
        neighbors = node_data[1]

        neighbor_distances = {}
        for neighbor_index in neighbors:
            neighbor_data = graph_data[neighbor_index]
            neighbor_coord = neighbor_data[0]
            distance = calculate_distance(current_node, neighbor_coord)
            neighbor_distances[neighbor_index] = distance

        result_dict[i] = neighbor_distances
    
    #Distance Dictionary Ex: 
    # {0: {1: 282.842712474619}, 1: {0: 282.842712474619, 2: 200.0}, 2: {1: 200.0}}
    print(result_dict)
    return result_dict

#Helper function to determin the distance between two cordinates
def calculate_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)
