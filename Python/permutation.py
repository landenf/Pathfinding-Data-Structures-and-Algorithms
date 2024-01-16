# Homework 5 - Johnson and Trotter algorithm.
import graph_data
import math
import pathing

point_Right = True # >
point_Left = False # <

def findNum(Array, num, length):
	for i in range(length):
		if Array[i] == num:
			return i + 1

# Step 1 of the algo- Find Largest Mobile Number
def findMobile(NodeArray, DirectionArray, length):
	mobile_prev = 0
	mobile = 0
	for i in range(length):
		if DirectionArray[NodeArray[i] - 1] == point_Left and i != 0:
			if NodeArray[i] > NodeArray[i - 1] and NodeArray[i] > mobile_prev:
				mobile = NodeArray[i]
				mobile_prev = mobile
		if DirectionArray[NodeArray[i] - 1] == point_Right and i != length - 1:
			if NodeArray[i] > NodeArray[i + 1] and NodeArray[i] > mobile_prev:
				mobile = NodeArray[i]
				mobile_prev = mobile
	if mobile == 0 and mobile_prev == 0:
		return 0
	else:
		return mobile

def permuation(NodeArray, DirectionArray, length):
	mobile = findMobile(NodeArray, DirectionArray, length)
	index = findNum(NodeArray, mobile, length)
	if index is not None: 
		if DirectionArray[NodeArray[index - 1] - 1] == point_Left:
			temp = NodeArray[index - 1]
			NodeArray[index - 1] = NodeArray[index - 2]
			NodeArray[index - 2] = temp
		elif DirectionArray[NodeArray[index - 1] - 1] == point_Right:
			temp = NodeArray[index]
			NodeArray[index] = NodeArray[index - 1]
			NodeArray[index - 1] = temp
  
	for i in range(length):
		if NodeArray[i] > mobile: #Swap those greater than mobile
			if DirectionArray[NodeArray[i] - 1] == point_Right:
				DirectionArray[NodeArray[i] - 1] = point_Left
			elif DirectionArray[NodeArray[i] - 1] == point_Left:
				DirectionArray[NodeArray[i] - 1] = point_Right

	returnable = []
	for i in range(length):
		returnable.append(NodeArray[i])
	return returnable
	

def printPermutations(n):
	NodeArray = [i + 1 for i in range(n)] 
	DirectionArray = [point_Left for i in range(n)] 
	PermuationsArray = [] 

	#Find Factorial value
	factorial_of_N = 1
	for i in range(1, n + 1):
		factorial_of_N = factorial_of_N * i

	#First permutation 
	first_permuation = []
	for i in range(n):
		first_permuation.append(NodeArray[i])
	PermuationsArray.append(first_permuation)

	#Find all the permuation from 1 to the factorial 
	for i in range(1, factorial_of_N):
		PermuationsArray.append(permuation(NodeArray, DirectionArray, n))
	return PermuationsArray


#Function to meet spec: keep start and end node constant
def keep_First_last (permArray):
	returnable = []
	for i in range(0, len(permArray)):
		if permArray[i][0] == permArray[0][0]:
			if permArray[i][len(permArray[i]) - 1] == permArray[0][len(permArray[i]) - 1]:
				returnable.append(permArray[i])
	return returnable

def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(node_order, graph_index):
	total_distance = 0
	for i in range(len(node_order) - 1):
		node1 = node_order[i]
		node2 = node_order[i + 1]
		
		t = graph_data.graph_data[graph_index][node1 - 1][0]
		x1, y1 = t
		t2 = graph_data.graph_data[graph_index][node2 - 1][0]
		x2, y2 = t2
		distance = calc_distance(x1,y1,x2,y2)
		total_distance += distance
	
	return total_distance

def findOptimalPermutation(permArray, graph_index):
    smallest_distance = float('inf')
    optimal_permutation = None
    for path in permArray:
        total_distance = calculate_total_distance(path, graph_index)
        if total_distance < smallest_distance:
            smallest_distance = total_distance
            optimal_permutation = path
    return optimal_permutation, smallest_distance

		
def main(n, graph=-1):
	if graph == -1: #This means we did not pass in a graph index, use a normal sequencial num array
		if n < 3: #Intial check
			print("N smaller than 3, No permutations")
			return False
		permutations = printPermutations(n)
		relevantPermutations = keep_First_last(permutations)
		print(relevantPermutations)
		return relevantPermutations
	
	else: #Means we did pass in a graph index
		n = len(graph_data.graph_data[graph]) # reset n to the lengh of the used graph
		permutations = printPermutations(n)
		relevantPermutations = keep_First_last(permutations) #Only use ones that start and end with graph
		vaild_Permutations = []
		for i in range(0, len(relevantPermutations)): #Check Valid
			if(pathing.is_path_valid(graph_data.graph_data[graph], relevantPermutations[i])):
				vaild_Permutations.append(relevantPermutations[i])
		print(relevantPermutations)
		#Do extra credits
		OptimalPath = findOptimalPermutation(relevantPermutations, graph)
		print("Extra Credit (Optimal Path): ", OptimalPath)
		return relevantPermutations

if __name__ == "__main__":
    main(4, 1) 
