import networkx as nx

# สร้างกราฟ
G = nx.Graph()
G.add_edge(1, 2, weight=3.5)
G.add_edge(2, 3, weight=4.2)
G.add_edge(3, 4, weight=2.7)
G.add_edge(1, 3, weight=1.8)

# เลือกโหนดเริ่มต้นและโหนดปลาย
source_node = 1
target_node = 4

# หาเส้นทางที่สั้นที่สุด
shortest_path = nx.shortest_path(G, source_node, target_node, weight='weight')

# หาผลรวมของน้ำหนักที่เป็นเลขทศนิยมใน shortest path
total_weight_decimal_shortest_path = sum(G[shortest_path[i]][shortest_path[i+1]]['weight'] for i in range(len(shortest_path)-1) if isinstance(G[shortest_path[i]][shortest_path[i+1]]['weight'], float))

print("Shortest Path:", shortest_path)
print("Total Weight (Decimal) in Shortest Path:", total_weight_decimal_shortest_path)
