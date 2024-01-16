[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11971026&assignment_repo_type=AssignmentRepo)

# Pathfinding Software Engineering III

## Homework 7 - Floyd-Warshall Algorithm

Customer Requirements
1. Implement Floyd-Warshall algorithm to generate all-pairs shortest paths for a graph.
2. Build a function to convert adjacency lists into 2D arrays as input for the algorithm.
3. Implement a separate function to build paths between start and end nodes using a parent matrix.
5. Write unit tests to verify the correctness of the Floyd-Warshall implementation.
6. Adhere to good software engineering practices for code organization and documentation.

Code Implementations
1. I Implemented Floyd-Warshall Algorith.
2. I tested the algrothim.
3. I met the specs for the assigment. 

## Homework 6 - Dijkstra's Algorithm and A*

Customer Requirements

1. Implement Dijkstra's algorithm to find the shortest paths in a weighted graph.
2. Define inline assertions as postconditions for paths to ensure the correctness of the algorithm.
3. Develop unit tests to verify the accuracy of the Dijkstra's algorithm.
4. Adhere to good software engineering practices for code organization and documentation.
5. Implement either heapq or PriorityQueue with methods for properly updating item priorities in the priority queue.
6. Implement A* using any admissible heuristic for enhanced pathfinding.

Code Implementations
1. I Implemented Dijkstras algorith to find the shortest paths using the cumulative distance. (SPEC)
2. I Implemented A* to track the Euclidean distance using graph data. (EXTRA CREDIT 1)
3. I Implemented a heapq to update items priorities instead of searching or sorting. (EXTRA CREDIT 2)
4. Wrote unit tests and assert statments.

## Homework 5 - Permutations
Customer Requirements

1. Implement the Steinhaus–Johnson–Trotter (SJT) algorithm to generate all permutations of natural numbers.
2. The Hamiltonian cycle should be checked from node 1 to n-1 for each graph.
3. Report valid Hamiltonian cycles, i.e., sequences of nodes. Return -1 or False if no valid Hamiltonian cycle exists.
4. Write unit tests to verify the SJT algorithm and detection of Hamiltonian cycles.

Code Implementations

1. Created a new Python file called permutation.py in the project.
2. Implemented the Steinhaus–Johnson–Trotter (SJT) algorithm to generate permutations.
3. Checked for Hamiltonian cycles from node 1 to n-1 in each graph in graph_data.
4. Reported valid Hamiltonian cycles and returned -1 or False if no valid cycle was found.
5. Implemented unit tests to verify the correctness of the SJT algorithm and Hamiltonian cycle detection.

This homework assignment focuses on implementing the SJT algorithm to generate permutations and checking for Hamiltonian cycles in graphs. Unit tests were created to ensure the correctness of the code.

## Homework 4 - DFS & BFS

Customer Requierments

1. Implement Debth first searching algo. 
2. Implement Breath first searching algo.
3. Implement 'winner' functionality
4. Unit and assert testing.

Code Implementations:

1. Per Spec I was able to implement a DFS and BFS algorithms and tested them accordingly. 


## Homework 3 - Random Path

Customer Requierments

1. Player should randomly generate path from start to exit.
2. Player should hit the target at some point along the path.
3. Player will be allowed to backtrack and get "stuck" between two nodes. (If randomness allows)
4. Score board should additionaly show more indebth statistics. 

Code Implementations:

1. I implemented a random path function that generates a list of nodes for the path.
    1. This method grabs all the relavent graph information such as start, target, and exit from graph_data.py
    2. Then, it randomly selects a node from the adjacency list and checks if it is the target.
    3. It will set a trigger based on if the target has been hit and move to that next node. 
    4. If the target has been hit and the exit node is next then the player will exit. Otherwise it coninues. 
2. Next I added a time elasped statistic to the players score board.
    1. This keeps track of the players time exausted traveling the current path. This will be helpful in comparing the effectiveness of each transveral path. 
3. Per spec, I also added inline asserts and more graphs to the graph_data.py for further testing. 

