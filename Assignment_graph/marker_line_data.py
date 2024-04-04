import sqlite3

# เชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect('ETO_DB.db')
cursor = conn.cursor()

# สร้าง list เพื่อเก็บข้อมูล
data_list = []

# ส่งคำสั่ง SQL ไปยังฐานข้อมูล
cursor.execute('SELECT latitude, longitude FROM marker')

# ใช้ for loop เพื่อเข้าถึงข้อมูลใน cursor
for row in cursor.fetchall():
    # นำข้อมูลที่ได้เข้ามาเก็บใน list
    data_list.append(row)

# ปิดการเชื่อมต่อฐานข้อมูล
conn.close()

# แสดงข้อมูลที่อยู่ใน list
# print(data_list)
