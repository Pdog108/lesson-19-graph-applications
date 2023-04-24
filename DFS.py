import networkx as nx

import matplotlib.pyplot as plt

Flights = {
    "NY,NJ": ["4"],
    "NY,RI": ["7"],
    "NJ,CT": ["6"],
    "RI,CT": ["1"],
    "CT,PA": ["10"],
    "RI,PA": ["5"],
    "FL,TX": ["14"],
    "FL,OK": ["8"],
    "OK,TX": ["4"],
    "TX,KY": ["5"],
    "KY,MN": ["4"],
    "MN,IL": ["6"],
    "MN,OH":["8"],
    "IL,OH": ["1"], 
    "CT,VA":["7"],
    "KY,LO":["4"],
    "LO,AK":["3"],
    "LO,MS":["5"],
    "MS,AK":["1"],
    "NJ,ME":["6"],
    "NY,NH":["3"],
    "TX,CO":["8"],
    "TN,AK":["10"],
    "NH,TX": ["45"],
    "RI,MS":["16"],
    "ME,FL":["20"],
    "OK,MS":["5"],
    "IL,TN":["50"],
    "OH,CO":["60"],
    "AK,PA": ["55"]
}

# Create an undirected graph
G = nx.Graph()

#Add the edges to the graph
G.add_nodes_from(Flights)

# Draw the Graph
pos = nx.spring_layout(G)
nx.draw(G, pos)
print(G)
plt.show()

'''
Function: DFS (Depth-First-Search)
Parameters: Graph: dictionary representing the graph
            Start: the starting vertex for the search
            End: "the goal" vertex for the search
            Visited: a set containing the vertices that have already been visited
            Path: a list containing the vertices visited so far
Returns: None, if the function finishes looping through all the neighbors of the starting vertex without finding a path to the goal vertex
'''
def flightsDFS(graph, start, end, visited=None, path=None):
    # If visited is None, set to an empty list
    if visited is None:
        visited = set()
    # If path is none, then set path to a list containing only the starting vertex
    if path is None:
        path = [start]
    # If the starting vertex is equal to the "goal" vertex, then return the path
    if start == end:
        return path
    # Add the starting vertex to the set of visited vertices
    visited.add(start)
    for vertex in graph[start]:
        # If the vertex has not been visited
        if vertex not in visited:
            # Create a new copy of the path list
            new_path = list(path)
            # Add the vertex to the new path list
            new_path.append(vertex)
            dfs_result = flightsDFS(graph, vertex, end, visited, new_path)
            if dfs_result is not None:
                return dfs_result
    return None
