import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, Optional, Set, List


def flights_dfs(graph: Dict[str, List[str]], start: str, end: str, visited: Optional[Set[str]] = None, path: List[str] = None):
    """
        Function: DFS (Depth-First-Search)
        Parameters: Graph: dictionary where the keys represent the vertices in the graph
                    Start: the starting vertex for the search
                    End: "the goal" vertex for the search
                    Visited: an optional set containing the vertices that have already been visited so far during the search
                    Path: an optional list containing the vertices visited so far, initially set to None
        Returns: None, if the function finishes looping through all the neighbors of the starting vertex without finding a path to the goal vertex,
                 else if it exists, this will return the path (as a list of vertices from the starting vertex to the end)
    """
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
            # Add the weight of the edge to the new path list
            new_path.append(vertex)
            dfs_result = flights_dfs(graph, vertex, end, visited, new_path)
            if dfs_result is not None:
                return dfs_result
    return None


flights = {
    "NY": ["NJ", "RI", "NH"],
    "ME": ["NY", "RI", "OH"],
    "NJ": ["NY", "CT", "ME"],
    "RI": ["NY", "CT", "PA", "MS"],
    "CT": ["NJ", "RI", "PA", "VA"],
    "PA": ["RI", "CT", "AK"],
    "FL": ["TX", "OK"],
    "CO": ["OH", "PA", "MS"],
    "TX": ["FL", "OK", "KY", "CO"],
    "OK": ["FL", "TX", "MS"],
    "KY": ["TX", "MN", "LA"],
    "MN": ["KY", "IL", "OH"],
    "IL": ["MN", "OH", "TN"],
    "OH": ["MN", "IL", "CO"],
    "VA": ["CT"],
    "LA": ["KY", "AK", "MS"],
    "MS": ["RI", "OK", "LA", "AK"],
    "AK": ["PA", "TN", "MS"],
    "TN": ["RI", "KY"],
    "NH": ["NY"],
}

FLIGHT_START = "NY"
FLIGHT_END = "LA"
flight_path = flights_dfs(flights, FLIGHT_START, FLIGHT_END)


if flight_path is not None:
    print(" -> ".join(flight_path))

# Create an directed graph
G = nx.DiGraph(flights)

# construct list of tuples of edges of the graph of the form (vertex, connected node)
edges = [(key, value) for key in flights for value in flights[key]]

# all the edges the flight path takes
path_edges = []


for i in range(len(flight_path) - 1):
    current_flight = flight_path[i]
    future_flight = flight_path[i + 1]
    found_pair = list(
        # Filter the edges kist and keep only the edges where the first element is the current flight and the second element is the future flight
        # Converts the filtered list to a regular list and takes the first element
        filter(lambda x: x[0] == current_flight and x[1] == future_flight, edges))[0]
    # Append the selected edge
    path_edges.append(found_pair)


# Add edges to graph
G.add_edges_from(edges)

# Draw the Graph
pos = nx.spring_layout(G, seed=11, k=1)

# Draw the nodes that aren't included in the path
nx.draw_networkx_nodes(G, pos, nodelist=set(G.nodes) -
                       set(flight_path), node_color='#1f78b4')

# Draw the edges that aren't included in the path
nx.draw_networkx_edges(G, pos, edgelist=set(G.edges) -
                       set(path_edges))

# Draw the nodes in the path with a red color
nx.draw_networkx_nodes(G, pos, nodelist=flight_path, node_color='r')

# Draw the edges in the path with a red color
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r')

nx.draw_networkx_labels(G, pos)

plt.axis("off")
plt.savefig("DFS_graph.png")
plt.show()