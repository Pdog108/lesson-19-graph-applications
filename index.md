# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Nick Lago (nlago@udel.edu)
* Hongbo Wang (frankw@udel.edu)
* Patrick Harris (pdharris@udel.edu)
* John Henry Cooper (jhcoop@udel.edu)

Description of project

## Installation Code

```sh
$> pip install networkx
$> pip install matplotlib
```

## Python Environment Setup

```python
import networkx as nx
import matplotlib.pyplot as plt
```

# First Problem Title

**Informal Description**: 
Campus.csv contains information about how far different neighbor buildings are from each other on a college campus. It then uses this information to draw a campus map, with buildings shown as circles and paths between them shown as lines. The map is color-coded to make it easier to read. The code then figures out the shortest way to get from one building to any other building on the map, and prints out those directions so that people can find the quickest route from Computer Department Headquarters, Smith Hall, to their destination.

> **Formal Description**:
>  * Input: Campus.csv
            The input of the program is a file named "Campus.csv" which contains a list of edges with their corresponding weights. Each line in the file represents an edge, and the format of each line is "start, end, weight". For example, "Smith Hall,Ewing Hall,53" represents an edge from "Smith Hall" to "Ewing Hall" with a weight of 53.
>  * Output: 
            The output of the program is the shortest path from the starting node "Smith Hall" to all other nodes in the graph, where the shortest path is defined as the path with the minimum total weight.
            Additionally, the program displays a visualization of the graph using the networkx and matplotlib libraries, which shows the nodes and edges of the graph, as well as their corresponding weights.

**Graph Problem/Algorithm**: [SSSP] 


**Setup code**:

import matplotlib.pyplot as plt 
import networkx as nx

**Visualization**:

![Image goes here](Campus_Map.png)

**Solution code:**

def main():
    with open("Campus.csv") as data_file:
        lines = data_file.readlines()

    G=nx.Graph()

    for line in lines:
        start, end, weight = line.strip("\n").split(",")
        weight=float(weight)
        G.add_edge(start, end, cost=weight)

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, node_color="orange", node_size=300,
                     font_size=8,
                     font_color="black",
                     edge_color="blue",
                     width=1,
                     with_labels=True)
    
    nx.draw_networkx_edges(G, pos, edge_color="blue",
        style="solid", 
        width=1)

    distance = nx.get_edge_attributes(G,"cost")

    nx.draw_networkx_edge_labels(G, pos, edge_labels=distance,
        label_pos=0.5, 
        font_size=7,
        font_color="red",
        font_weight="normal",
        horizontalalignment="center", 
        verticalalignment="top",
        rotate=True, 
        clip_on=True)
    
    plt.show()

    routes = nx.shortest_path(G, "Smith Hall", weight="cost")
    for key in routes:
        distance = nx.shortest_path_length(G, "Smith Hall", key, weight="cost")
        print("The shortest path from Smith Hall to", key, ":", routes[key], "with the distance of", distance, "meters")
        # print("\n")


main()

**Output**

The shortest path from Smith Hall to Smith Hall : ['Smith Hall'] with the distance of 0 meters
The shortest path from Smith Hall to Ewing Hall : ['Smith Hall', 'Ewing Hall'] with the distance of 53.0 meters
The shortest path from Smith Hall to Kirkbride Lecture Hall : ['Smith Hall', 'Kirkbride Lecture Hall'] with the distance of 26.0 meters
The shortest path from Smith Hall to Purnell Hall : ['Smith Hall', 'Purnell Hall'] with the distance of 77.0 meters
The shortest path from Smith Hall to Gore Hall : ['Smith Hall', 'Gore Hall'] with the distance of 38.0 meters
The shortest path from Smith Hall to Sharp Lab : ['Smith Hall', 'Gore Hall', 'Sharp Lab'] with the distance of 77.0 meters
The shortest path from Smith Hall to Mitchell Hall : ['Smith Hall', 'Gore Hall', 'Mitchell Hall'] with the distance of 65.0 meters
The shortest path from Smith Hall to Du Pont Hall : ['Smith Hall', 'Gore Hall', 'Du Pont Hall'] with the distance of 94.0 meters
The shortest path from Smith Hall to Hullihen Hall : ['Smith Hall', 'Gore Hall', 'Mitchell Hall', 'Hullihen Hall'] with the distance of 137.0 meters
The shortest path from Smith Hall to Alfred Lerner Hall : ['Smith Hall', 'Purnell Hall', 'Alfred Lerner Hall'] with the distance of 132.0 meters
The shortest path from Smith Hall to Amy du Pont Music Building : ['Smith Hall', 'Purnell Hall', 'Amy du Pont Music Building'] with the distance of 157.0 meters
The shortest path from Smith Hall to Wolf Hall : ['Smith Hall', 'Gore Hall', 'Du Pont Hall', 'Wolf Hall'] with the distance of 112.0 meters
The shortest path from Smith Hall to Evans Hall : ['Smith Hall', 'Gore Hall', 'Du Pont Hall', 'Evans Hall'] with the distance of 110.0 meters
The shortest path from Smith Hall to Spencer Lab : ['Smith Hall', 'Gore Hall', 'Du Pont Hall', 'Spencer Lab'] with the distance of 174.0 meters
The shortest path from Smith Hall to Life Sciences Research Facility : ['Smith Hall', 'Gore Hall', 'Du Pont Hall', 'Spencer Lab', 'Life Sciences Research Facility'] with the distance of 229.0 meters
The shortest path from Smith Hall to Memorial Hall : ['Smith Hall', 'Gore Hall', 'Mitchell Hall', 'Hullihen Hall', 'Memorial Hall'] with the distance of 182.0 meters
The shortest path from Smith Hall to Brown Lab : ['Smith Hall', 'Gore Hall', 'Mitchell Hall', 'Hullihen Hall', 'Brown Lab'] with the distance of 181.0 meters   
The shortest path from Smith Hall to Roselle Center for the Arts : ['Smith Hall', 'Purnell Hall', 'Amy du Pont Music Building', 'Roselle Center for the Arts'] with the distance of 236.0 meters
The shortest path from Smith Hall to East Hall : ['Smith Hall', 'Gore Hall', 'Du Pont Hall', 'Spencer Lab', 'East Hall'] with the distance of 233.0 meters      
The shortest path from Smith Hall to Colburn Lab : ['Smith Hall', 'Gore Hall', 'Du Pont Hall', 'Spencer Lab', 'Colburn Lab'] with the distance of 197.0 meters  
The shortest path from Smith Hall to Graham Hall : ['Smith Hall', 'Gore Hall', 'Du Pont Hall', 'Spencer Lab', 'Graham Hall'] with the distance of 232.0 meters  
The shortest path from Smith Hall to Lammot du Pont Lab : ['Smith Hall', 'Gore Hall', 'Mitchell Hall', 'Hullihen Hall', 'Brown Lab', 'Lammot du Pont Lab'] with the distance of 190.0 meters
The shortest path from Smith Hall to Drake Hall : ['Smith Hall', 'Gore Hall', 'Mitchell Hall', 'Hullihen Hall', 'Brown Lab', 'Drake Hall'] with the distance of 215.0 meters
The shortest path from Smith Hall to Morris Library : ['Smith Hall', 'Gore Hall', 'Mitchell Hall', 'Hullihen Hall', 'Memorial Hall', 'Morris Library'] with the distance of 302.0 meters
The shortest path from Smith Hall to Pearson Lab : ['Smith Hall', 'Gore Hall', 'Du Pont Hall', 'Spencer Lab', 'Colburn Lab', 'Pearson Lab'] with the distance of 239.0 meters


**Interpretation of Results**:
    The program prints the shortest path for each node in the graph in the format "The shortest path from Smith Hall to [node]: [path]", where [node] is the name of the destination node and [path] is a list of nodes representing the shortest path from "Smith Hall" to the destination node.