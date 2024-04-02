import sqlite3

sqlfile = 'ETO_DB.db'

def get_node():
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
         

distance = get_node()
print(distance)