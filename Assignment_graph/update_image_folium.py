import sqlite3

sqlfile = 'ETO_DB.db'

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def update_image (marker_ID, image):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update marker set image = ? where marker_ID = ?"""
        
        image = convertToBinaryData(image)
        data = (image, marker_ID)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")

update_image(1,'E:\Problem Solving\Problem-Solving\Assignment_graph\image\ป่านันทนาการน้ำตกเขาอีโต้.jpg')
