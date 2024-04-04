import sqlite3
import marker

sqlfile = 'ETO_DB.db'
def del_marker_comman():
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


    def del_node(NodeID):
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sql_update_query = """DELETE from marker where marker_ID = ?"""
            cursor.execute(sql_update_query, (NodeID,))
            sqliteConnection.commit()
            print("Record deleted successfully")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")


    delete_node = int(input('คุณต้องการลบ Marker ใด: '))

    del_node(delete_node)

marker.mapOjp
marker.mapOjp.save("index.html")