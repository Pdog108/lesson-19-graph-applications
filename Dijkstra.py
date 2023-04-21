# Single-Source Shortest Path (Dijkstra's Algorithm)
# import libaries
import matplotlib.pyplot as plt
import networkx as nx
# import pandas as pd

def main():
    with open("Campus.csv") as data_file:
        lines = data_file.readlines()
    
    G=nx.Graph()

    for line in lines:
        start, end, weight = line.strip("\n").split(",")
        weight=float(weight)
        G.add_edge(start, end, cost=weight)

    # airport_col = ["Origin", "Destination", "Flight Time"]
    # airport_df = pd.read_csv("Flights.csv", names = airport_col, index_col = 0)

    # index = 0
    # while index<airport_df.shape[0]:
    #     start = airport_df.iloc[index, "Origin"]
    #     end = airport_df.iloc[index, "Destination"]
    #     weight = airport_df.iloc[index, "Flight Time"]
    #     G.add_edge(start, end, weight = weight)
    #     index = index+1

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

    # print('G.nodes(data=True)', G.nodes(data=True))
    # print("Compute shortest paths in the graph: ", nx.shortest_path(G, "Smith Hall", weight="cost"))
    routes = nx.shortest_path(G, "Smith Hall", weight="cost")
    for key in routes:
        print("The shortest path from Smith Hall to", key, ":", routes[key])


main()