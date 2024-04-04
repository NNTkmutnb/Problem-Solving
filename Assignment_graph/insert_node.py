import sqlite3

sqlfile = 'ETO_DB.db'

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
