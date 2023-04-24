import networkx as nx
import matplotlib.pyplot as plt

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
        path = [start, 0]
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
            # Add the weight of the edge to the new path list
            new_path.append(graph[start][vertex])
            dfs_result = flightsDFS(graph, vertex, end, visited, new_path)
            if dfs_result is not None:
                return dfs_result
    return None


Flights = {
    "NY": {"NJ": 4, "RI": 7, "NH": 3},
    "ME": {"NY": 3, "RI": 1, "OH": 7},
    "NJ": {"NY": 4, "CT": 6, "ME": 6},
    "RI": {"NY": 7, "CT": 1, "PA": 5, "MS": 16},
    "CT": {"NJ": 6, "RI": 1, "PA": 10, "VA": 7},
    "PA": {"RI": 5, "CT": 10, "AK": 55},
    "FL": {"TX": 14, "OK": 8},
    "CO": {"OH": 4, "PA": 8, "MS": 5},
    "TX": {"FL": 14, "OK": 4, "KY": 5, "CO": 8},
    "OK": {"FL": 8, "TX": 4, "MS": 5},
    "KY": {"TX": 5, "MN": 4, "LA": 4},
    "MN": {"KY": 4, "IL": 6, "OH": 8},
    "IL": {"MN": 6, "OH": 1, "TN": 50},
    "OH": {"MN": 8, "IL": 1, "CO": 60},
    "VA": {"CT": 7},
    "LA": {"KY": 4, "AK": 3, "MS": 5},
    "MS": {"RI": 16, "OK": 5, "LA": 5, "AK": 1},
    "AK": {"PA": 55, "TN": 10, "MS": 1},
    "TN": {"RI": 45, "KY": 5},
    "NH": {"NY": 3}
}

start = "NY"
end = "NH"
path = flightsDFS(Flights, start, end)


if path is not None:
    print(" -> ".join(str(path)))

# Create an undirected graph
G = nx.DiGraph(Flights)


# Draw the Graph
pos = nx.spring_layout(G, seed = 11, k = 2)
nx.draw_networkx(G, 
        pos, 
        node_color='#0091e6', 
        node_size=300,
        font_size=7,
        font_color='white',
        edge_color='black',
        font_weight='bold',
        width=3,
        with_labels=True)

nx.draw_networkx_edge_labels(G, pos, 
        label_pos=0.5, 
        font_size=4, 
        font_color='k', 
        font_family='sans-serif',
        font_weight='bold', 
        horizontalalignment='center', 
        verticalalignment="bottom",
        rotate=True, 
        clip_on=True)


plt.axis("off")
plt.savefig("DFS_graph.png")
plt.show()