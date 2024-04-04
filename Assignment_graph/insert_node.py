import sqlite3
import marker

sqlfile = 'ETO_DB.db'
def insert_Node_comman():
    def get_marker_name():
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            # print("Connected to SQLite")
            sqlite_select_query = """SELECT marker_ID, marker_name
                                        FROM marker;"""
            cursor.execute(sqlite_select_query)
            record = cursor.fetchall()
            marker_name  = []
            for i in record:
                marker_name.append(i)
        except sqlite3.Error as error:
            print("Failed to read single row from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                # print("The SQLite connection is closed")
                return (marker_name)
            
    marker_name = get_marker_name()
    # print(marker_name)

    marker_name_list = {}

    for key, value in marker_name:
        marker_name_list[key] = value

    def marker_list():
        print('== Marker ทั้งหมดในฐานข้อมูล ==')
        for i in marker_name_list.items():
            print(i)
    
    marker_list()

    def insert_New_Node(NodeID, from_node, to_node, distance, marker_ID):
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO 'ETO'
                            ('NodeID','from_node','to_node','distance','marker_ID') 
                            VALUES (?, ?, ?, ?, ?);"""

            data_tuple = (NodeID,from_node, to_node, distance, marker_ID)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("New node insert successfully \n")
            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")

    marker_ID = int(input('Node ที่คุณต้องการจะเพิ่มระยะทางคือ: '))
    from_node = int(input('จาก Node ที่: '))
    to_node = int(input('ไป Node ที่: '))
    distanace = float(input('ระยะทาง: '))

    insert_New_Node(None ,from_node, to_node, distanace, marker_ID)

marker.mapOjp
marker.mapOjp.save("index.html")