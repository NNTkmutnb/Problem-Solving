import sqlite3
# import del_marker
import marker

sqlfile = 'ETO_DB.db'


def update_marker_comman():
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

    marker_ID = int(input('ต้องการแก้ไขข้อมูลใด: '))
    marker_name = input('กรอกชื่อสถานี่ใหม่ (จำเป็น): ')
    discription = input('รายละเอียด: ')
    link = input('ลิงค์เว็บไซต์: ')
    image = input('ลิงค์ที่อยู่รูปภาพ: ')

    update_maker_name(marker_ID, marker_name, discription, link, image)
    
marker.mapOjp
marker.mapOjp.save("index.html") 