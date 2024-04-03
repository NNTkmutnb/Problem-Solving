import networkx as nx
import matplotlib.pyplot as plt
import sqlite3

sqlfile = 'ETO_DB.db'

# Code คำสั่งดึงข้อมูลระยะทางจาก Database
def get_node_distance():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT distance 
                                FROM ETO;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        distance  = []
        for i in record:
            for n in i :
                distance.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return (distance)
         

distance = get_node_distance()

# Code คำสั่งดึงข้อมูลระยะทางจาก Database
def get_node_source():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT from_node 
                                FROM ETO;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        source  = []
        for i in record:
            for n in i :
                source.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return (source)
         

source = get_node_source()

def get_node_desination():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = """SELECT to_node 
                                FROM ETO;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        desination  = []
        for i in record:
            for n in i :
                desination.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return (desination)
         

desination = get_node_desination()


network = nx.Graph()

network.add_nodes_from([1,2,3,4,5,6,7,8])
print(f"This network has now {network.number_of_nodes()} nodes.")

# ดึงขอมูลจาก Database มาทำการสร้าง Node
for s,d,w in zip(source,desination,distance):
   network.add_edge(s, d, weight = w) 
   

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
print(distance)


nx.draw_networkx(network,node_color=color_list, with_labels=True)

plt.show()
