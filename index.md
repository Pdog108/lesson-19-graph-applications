# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* First member (email)
* Second member (email)
* Third member (email)
* Fourth member (email)

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

**Graph Problem/Algorithm**: [DFS/BFS/SSSP/APSP/MST]


**Setup code**:

```python
```

**Visualization**:

![Image goes here](Campus_Map.png)

**Solution code:**

```python
```

**Output**

```
```

**Interpretation of Results**:

