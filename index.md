# Team Dragon

**CISC320 Spring 2023 Lesson 19 - Graph Applications**

Group Members:
* Nick Lago (nlago@udel.edu)
* Hongbo Wang (frankw@udel.edu)
* Patrick Harris (pdharris@udel.edu)
* John Henry Cooper (jhcoop@udel.edu)

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# First Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: [SSSP(Djikstras)]


**Setup code**:

```python
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:

# Minimum Distance Path (Kruskals)

**Informal Description**: Kruskals Algorithm finds the minimum spanning tree of a given weighted undirected graph. In this case, the algorithm finds the flight path with the minimum distance covered in order to still reach every location/airport.

> **Formal Description**:
>  * Input: Flights.csv:  
NY,NJ,4
NY,RI,7
NJ,CT,6
RI,CT,1
CT,PA,10
RI,PA,5
FL,TX,14
FL,OK,8
OK,TX,4
TX,KY,5
KY,MN,4
MN,IL,6
MN,OH,8
IL,OH,1
CT,VA,7
KY,LO,4
LO,AK,3
LO,MS,5
MS,AK,1
NJ,ME,6
NY,NH,3
TX,CO,8
TN,AK,10
NH,TX,45
RI,MS,16
ME,FL,20
OK,MS,5
IL,TN,50
OH,CO,60
AK,PA,55  

>  * Output: Graph with 20 nodes and 19 edges
('RI', 'CT', {'d': 1.0})
('IL', 'OH', {'d': 1.0})
('AK', 'MS', {'d': 1.0})
('NY', 'NH', {'d': 3.0})
('LO', 'AK', {'d': 3.0})
('NY', 'NJ', {'d': 4.0})
('TX', 'OK', {'d': 4.0})
('KY', 'MN', {'d': 4.0})
('KY', 'LO', {'d': 4.0})
('RI', 'PA', {'d': 5.0})
('TX', 'KY', {'d': 5.0})
('NJ', 'CT', {'d': 6.0})
('NJ', 'ME', {'d': 6.0})
('MN', 'IL', {'d': 6.0})
('CT', 'VA', {'d': 7.0})
('FL', 'OK', {'d': 8.0})
('TX', 'CO', {'d': 8.0})
('AK', 'TN', {'d': 10.0})
('RI', 'MS', {'d': 16.0})

**Graph Problem/Algorithm**: [MST (Kruskals)]


**Setup code**:

import matplotlib.pyplot as plt  
import networkx as nx

**Visualization**:

![https://i.ibb.co/FnvVfKj/prims.png](https://i.ibb.co/FnvVfKj/prims.png)  
Minimum spanning tree is shown in blue dashed lines over the edges.

**Solution code:**

```
    def main():
    with open("Flights.csv") as data_file:
        lines = data_file.readlines()
    
    G=nx.Graph()

    for line in lines:
        start, end, weight = line.strip("\n").split(",")
        weight=float(weight)
        G.add_edge(start, end, d=weight)

    MST = nx.minimum_spanning_tree(G, weight="d", algorithm="kruskal")
    
    pos = nx.spring_layout(G)

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

    nx.draw_networkx_edges(MST, 
        pos, 
        edge_color='#0091e6',
        style='dashed', 
        width=3)

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
        
    plt.axis('off')
    plt.show()
    print(nx.minimum_spanning_tree(G, weight="d", algorithm="kruskal"))
    
main()
```

**Output**

```
    Graph with 20 nodes and 19 edges
(‘RI’, ‘CT’, {‘d’: 1.0})
(‘IL’, ‘OH’, {‘d’: 1.0})
(‘AK’, ‘MS’, {‘d’: 1.0})
(‘NY’, ‘NH’, {‘d’: 3.0})
(‘LO’, ‘AK’, {‘d’: 3.0})
(‘NY’, ‘NJ’, {‘d’: 4.0})
(‘TX’, ‘OK’, {‘d’: 4.0})
(‘KY’, ‘MN’, {‘d’: 4.0})
(‘KY’, ‘LO’, {‘d’: 4.0})
(‘RI’, ‘PA’, {‘d’: 5.0})
(‘TX’, ‘KY’, {‘d’: 5.0})
(‘NJ’, ‘CT’, {‘d’: 6.0})
(‘NJ’, ‘ME’, {‘d’: 6.0})
(‘MN’, ‘IL’, {‘d’: 6.0})
(‘CT’, ‘VA’, {‘d’: 7.0})
(‘FL’, ‘OK’, {‘d’: 8.0})
(‘TX’, ‘CO’, {‘d’: 8.0})
(‘AK’, ‘TN’, {‘d’: 10.0})
(‘RI’, ‘MS’, {‘d’: 16.0})
```

**Interpretation of Results**: These results tell the traveler the path that connects all states' airports in the least distance covered. This can be useful for anyone who is looking to travel to multiple destinations, and wants to be time efficient in doing so. A minimum spanning tree can also be a helpful visual for airlines when choosing optimal routes to fly.

# Determining if there are enough pilots to fly every flight (Breadth First Search)

**Informal Description**: 
The airport has a list of available pilots and a list of flights in need of a pilot. The problem is that each pilot has 
certain flights that conflict with their schedule or location, meaning that they are not able to pilot these flights.
Additionally, some flights conflict with other flights. Given the list of pilots, flights, and conflicts per flight, 
the airport wants a simple algorithm to tell them if they have enough pilots to fly each plane.
> **Formal Description**:
>  * Input: An undirected, unweighted graph. Each vertex either represents a pilot or a flight. Each edge connects
>  * a pilot to a flight that conflicts with their schedule (one that they can not pilot) or two flights that conflict.
>  * 
>  * Output: A printed output, saying either "The graph is bipartite. 
>  * There are enough pilots to fly each flight without conflict" if the graph is bipartite or "The graph is not
>  * bipartite. More "More pilots are needed or modifications need to be made to their schedules." if the graph is not 
>  * bipartite
>  * 
>  * The methodology behind determining if the available pilots can fly every available flight revolves around 
>  * determining if the input graph, which contains all flights (vertex), pilots (vertex), and conflicts (edge), is
>  * bipartite, meaning that edges only connect pilots to flights, and not pilots to pilots or flights to flights. If
>  * the graph is bipartite, this tells us that it is possible to assign the pilots to the flights in a way that avoids 
>  * any conflicts. This is because the bipartite structure implies that there are no conflicts between pilots or 
>  * between flights, and therefore any conflict can only occur between a pilot and a flight. In other words, if the 
>  * graph is bipartite, it means that it is possible to schedule all the flights without any pilot having a conflict 
>  * with their schedule, assuming that each flight requires a single pilot. This is accomplished by utilizing the 
>  * built-in networkx function is_bipartite(), which takes a graph as an input and returns a boolean representing if 
>  * the graph is bipartite or not. is_bipartite's source code  is based on BFS. It starts by arbitrarily selecting a 
>  * node and assigning it to one of the two groups. It then adds all the neighbors of that node to group B. It then 
>  * continues the process, alternately adding nodes to group A and group B, until all nodes have been assigned a group. 
>  * At each step of the process, the algorithm checks whether there are any edges connecting nodes in the same group. 
>  * If any such edges are found, the graph is not bipartite. Otherwise, the graph is bipartite.

**Graph Problem/Algorithm**: [BFS]


**Setup code**:

```
import networkx as nx
import matplotlib.pyplot as plt

# create a new undirected graph
G = nx.Graph()

# add 10 pilot nodes
for i in range(1, 11):
    G.add_node("P" + str(i), node_type="pilot")

# add 10 flight nodes
for i in range(1, 11):
    G.add_node("F" + str(i), node_type="flight")

# add edges between pilots and flights
# assuming that Pilot P1 conflicts with Flight F2, F5, F9
G.add_edge("P1", "F2")
G.add_edge("P1", "F5")
G.add_edge("P1", "F9")

# assuming that Pilot P2 conflicts with Flight F1, F3, F6
G.add_edge("P2", "F1")
G.add_edge("P2", "F3")
G.add_edge("P2", "F6")

# assuming that Pilot P3 conflicts with Flight F2, F4, F7
G.add_edge("P3", "F2")
G.add_edge("P3", "F4")
G.add_edge("P3", "F7")

# assuming that Pilot P4 conflicts with Flight F1, F5, F8
G.add_edge("P4", "F1")
G.add_edge("P4", "F5")
G.add_edge("P4", "F8")

# assuming that Pilot P5 conflicts with Flight F3, F6, F9
G.add_edge("P5", "F3")
G.add_edge("P5", "F6")
G.add_edge("P5", "F9")

# assuming that Pilot P6 conflicts with Flight F4, F7, F10
G.add_edge("P6", "F4")
G.add_edge("P6", "F7")
G.add_edge("P6", "F10")

# assuming that Pilot P7 conflicts with Flight F1, F8, F10
G.add_edge("P7", "F1")
G.add_edge("P7", "F8")
G.add_edge("P7", "F10")

# assuming that Pilot P8 conflicts with Flight F2, F6, F10
G.add_edge("P8", "F2")
G.add_edge("P8", "F6")
G.add_edge("P8", "F10")

# assuming that Pilot P9 conflicts with Flight F3, F7, F9
G.add_edge("P9", "F3")
G.add_edge("P9", "F7")
G.add_edge("P9", "F9")

# assuming that Pilot P10 conflicts with Flight F4, F5, F10
G.add_edge("P10", "F4")
G.add_edge("P10", "F5")
G.add_edge("P10", "F10")

# create a layout for the graph and draw it
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=["red" if n[1]["node_type"] == "pilot" else "lightblue" for n in G.nodes(data=True)])

# show the graph on screen
plt.show()
plt.savefig("BFS_graph.png")

```

**Visualization**:

![Image goes here]("./BFS_graph.png")

**Solution code:**

```
# check if the graph is bipartite
is_bipartite = nx.is_bipartite(G)
if is_bipartite:
    print("The graph is bipartite.")
    print("There are enough pilots to fly each flight without conflict.")
else:
    print("The graph is not bipartite.")
     print("More pilots are needed or modifications need to be made to their scheduling.")
```

**Output**

```
The graph is bipartite.
There are enough pilots to fly each flight without conflict.
```

**Interpretation of Results**:
Given the set of pilots, flights, and conflicts that construct the input graph, there is a possible pilot-flight
allocation such that each pilot can fly a flight that does not conflict with their schedule and each flight has a pilot.

# Fourth Problem Title

**Informal Description**: 

> **Formal Description**:
>  * Input:
>  * Output:

**Graph Problem/Algorithm**: [BFS]


**Setup code**:

```python
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**: