import networkx as nx
import matplotlib.pyplot as plt

# สร้างกราฟ
G = nx.Graph()

# เพิ่มเส้นเชื่อมต่อ (เพื่อสร้างกราฟ)
G.add_edge(1, 2, weight=4)
G.add_edge(1, 3, weight=2)
G.add_edge(2, 3, weight=1)
G.add_edge(2, 4, weight=3)
G.add_edge(3, 4, weight=5)

# หาเส้นทางที่สั้นที่สุดระหว่าง Node โดยใช้ Dijkstra's algorithm
shortest_path = nx.shortest_path(G, source=1, target=4, weight='weight')
plt.show()
print("เส้นทางที่สั้นที่สุด:", shortest_path)
