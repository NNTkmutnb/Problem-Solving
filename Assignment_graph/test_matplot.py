import networkx as nx
import matplotlib.pyplot as plt

network = nx.Graph()

network.add_nodes_from([1,2,3,4,5,6,7,8])
print(f"This network has now {network.number_of_nodes()} nodes.")

network.add_edge(1, 2, weight = 1.4)
network.add_edge(1, 3, weight = 1.5)
network.add_edge(3, 4, weight = 0.28)
network.add_edge(1, 5, weight = 1.8)
network.add_edge(5, 6, weight = 2.8)
network.add_edge(6, 7, weight = 0.65)
network.add_edge(7, 8, weight = 1.5)

color_list = ["gold", "red", "violet", "blue", "green", "purple", "orange", "gray"]

plt.figure(figsize=(8, 6))
plt.title('Example of Graph Representation', size=10)

source = int(input("Enter in your current location information: "))
target = int(input("Enter the destination information where you want to go: "))


shortest_path = nx.shortest_path(network, source, target, weight='weight')

total_weight_decimal_shortest_path = sum(network[shortest_path[i]][shortest_path[i+1]]['weight'] 
                                         for i in range(len(shortest_path)-1) 
                                            if isinstance(network[shortest_path[i]][shortest_path[i+1]]['weight'], float))

format_total_weight = f"{total_weight_decimal_shortest_path:.1f}"

print("Shortest Path:", shortest_path)
print(f"Total Weight (Decimal) in Shortest Path: {format_total_weight} km.")


nx.draw_networkx(network,node_color=color_list, with_labels=True)
# print(f"เส้นทางที่สั้นที่สุด: {shortest_path} ระยะทางรวมทั้งหมด: {weight}")
plt.show()
