import sqlite3

sqlfile = 'ETO_DB.db'

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


delete_node = int(input('What node do you want to delete: '))

del_node(delete_node)