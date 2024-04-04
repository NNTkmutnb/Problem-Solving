import networkx as nx
from folium.plugins import AntPath
import sqlite3
import marker

sqlfile = 'ETO_DB.db'

# Code คำสั่งดึงข้อมูลระยะทางจาก Database
def get_node_distance():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
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
            # print("The SQLite connection is closed")
            return (distance)
         

distance = get_node_distance()

# Code คำสั่งดึงข้อมูลระยะทางจาก Database
def get_node_source():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
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
            # print("The SQLite connection is closed")
            return (source)
         

source = get_node_source()

def get_node_desination():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
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
            # print("The SQLite connection is closed")
            return (desination)
         
desination = get_node_desination()

def get_marker_ID():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT marker_ID 
                                FROM marker;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        marker_ID  = []
        for i in record:
            for n in i :
                marker_ID.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (marker_ID)
         
marker_ID = get_marker_ID()
# print(marker_ID)

def get_latitude_longitude():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT marker.marker_ID,marker.latitude, marker.longitude
                                    FROM marker
                                    INNER JOIN ETO
                                    ON marker.marker_ID = ETO.marker_ID WHERE ETO.marker_ID;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        latitude_longitude  = []
        for i in record:
            latitude_longitude.append(i)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (latitude_longitude)
         
latitude_longitude = get_latitude_longitude()
# print(latitude_longitude)


network = nx.Graph()
network.add_nodes_from(marker_ID)

# ดึงขอมูลจาก Database มาทำการสร้าง Node
for s,d,w in zip(source,desination,distance):
   network.add_edge(s, d, weight = w) 
   

source = int(input("Enter in your current location information: "))
target = int(input("Enter the destination information where you want to go: "))


shortest_path = nx.shortest_path(network, source, target, weight='weight')


total_weight_decimal_shortest_path = sum(network[shortest_path[i]][shortest_path[i+1]]['weight'] 
                                         for i in range(len(shortest_path)-1) 
                                            if isinstance(network[shortest_path[i]][shortest_path[i+1]]['weight'], float))

format_total_weight = f"{total_weight_decimal_shortest_path:.1f}"

def dict_lat_long():

    data_dict = {}
    for key, value1, value2 in latitude_longitude:
        data_dict[key] = value1, value2
    
    return data_dict

dictionary_lat_long = dict_lat_long()
# print(dictionary_lat_long)


def compare_list_to_dict(data_list, data_dict):

    result_list = []
    a = False
    b = False
    for item in data_list:
        
        if item in data_dict:
            result_list.append(data_dict[item])
            
    return result_list

result = compare_list_to_dict(shortest_path, dictionary_lat_long)

print("Shortest Path:", shortest_path)
print(f"Total Weight (Decimal) in Shortest Path: {format_total_weight} km.")

AntPath(result, delay=2000, dash_array=[40,25], color="blue", weight=8).add_to(marker.mapOjp)

marker.mapOjp
marker.mapOjp.save("index.html")

