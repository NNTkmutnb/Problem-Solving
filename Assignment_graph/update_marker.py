import sqlite3
import del_marker

sqlfile = 'ETO_DB.db'


def update_maker_name (marker_ID, marker_name, discription, link, image):
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update marker set marker_name = ?, discription = ?, link = ?, image = ? where marker_ID = ?"""
        
        data = (marker_name, discription, link, image, marker_ID)
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


del_marker.marker_list()
marker_ID = int(input('ต้องการแก้ไขข้อมูลใด: '))
marker_name = input('กรอกชื่อสถานี่ใหม่ (จำเป็น): ')
discription = input('รายละเอียด: ')
link = input('ลิงค์เว็บไซต์: ')
image = input('ลิงค์ที่อยู่รูปภาพ: ')

update_maker_name(marker_ID, marker_name, discription, link, image)

