myfile = open('Graph', 'r')
graph = {}
for line in myfile:
    key, value = line.strip().split(':')
    graph[key.strip()] = value.strip().split(',')
myfile.close()

print(' text file to dictionary =\n ', graph)


visited = [] # List for visited nodes.
queue = [] # Initialize a queue

def bfs(visited, graph, node):  # function for BFS
    visited.append(node)
    queue.append(node)

    while queue: # Creating loop to visit each node
         m = queue.pop(0)
         print(m, end=" ")
         for neighbour in graph:
             if neighbour not in visited:
                 visited.append(neighbour)
                 queue.append(neighbour)


# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5') # function calling
