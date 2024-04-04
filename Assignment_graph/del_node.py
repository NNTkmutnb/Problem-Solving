import sqlite3
import marker

sqlfile = 'ETO_DB.db'
def del_node_comman():
    def get_ETO_node():
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            # print("Connected to SQLite")
            sqlite_select_query = """SELECT marker_ID, from_node, to_node
                                        FROM ETO;"""
            cursor.execute(sqlite_select_query)
            record = cursor.fetchall()
            ETO_node  = []
            for i in record:
                ETO_node.append(i)
        except sqlite3.Error as error:
            print("Failed to read single row from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                # print("The SQLite connection is closed")
                return (ETO_node)
            
    ETO_node = get_ETO_node()
    # print(marker_name)

    ETO_node_list = {}

    for key, value1, value2 in ETO_node:
        ETO_node_list[key] = value1, value2


    print('== Node ทั้งหมดในฐานข้อมูล ==')
    for i in ETO_node:
        print(f'หมายเลข node:{i[0]} จาก:{i[1]} ไป:{i[2]}')

    def del_node(NodeID):
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sql_update_query = """DELETE from ETO where marker_ID = ?"""
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


    delete_node = int(input('คุณต้องการลบ Node หมายเลขใด: '))

    del_node(delete_node)

marker.mapOjp
marker.mapOjp.save("index.html")