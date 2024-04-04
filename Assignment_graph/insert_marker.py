import sqlite3
import marker

sqlfile = 'ETO_DB.db'
def insert_marker_comman():
    def insert_New_marker(marker_ID, marker_name, latitude, longitude, mardiscriptionker_ID, link, marker_color, icon):
        try:
            sqliteConnection = sqlite3.connect(sqlfile)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO 'marker'
                            ('marker_ID','marker_name','latitude','longitude','discription', 'link', 'marker_color', 'icon') 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""

            data_tuple = (marker_ID, marker_name, latitude, longitude, mardiscriptionker_ID, link, marker_color, icon)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("New marker insert successfully \n")
            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")


    marker_name = input('กรอกชื่อสถานที่ใหม่ที่คุณต้องการเพิ่มเข้าไปในฐานข้อมูล: ')
    latitude = float(input('ตำแหน่งละติจูด (สามารถ copy ได้จาก Google Map): '))
    longitude = float(input('ตำแหน่งลองจิจูด (สามารถ copy ได้จาก Google Map): '))
    discription = input('กรอกรายละเอียดหรือช่องทางการติดต่อ: ')
    link = input('ลิงค์เว็บไซต์ต่างๆ เช่น ลิงค์ Facebook: ')
    marker_color = input('กรอกสี Marker **เป็นภาษาอังกฤษ**: ')
    icon = input('กรอกชื่อไอคอน **สามารถเข้าไปหา icon ได้ที่เว็บไซต์นี้ (https://getbootstrap.com/docs/3.3/components/)**: ')

    insert_New_marker(None ,marker_name, latitude, longitude, discription, link, marker_color, icon)

marker.mapOjp
marker.mapOjp.save("index.html")