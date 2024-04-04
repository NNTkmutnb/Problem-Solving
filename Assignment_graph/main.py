import find_shortest_distance
import insert_marker
import insert_node
import update_marker
import del_marker
import del_node
import marker


# go_back = 'y'

def main():
    
    # while go_back.lower() == 'y':
        print('==== โปรแกรมระบบตัวช่วยนำเที่ยวป่านันทนาการน้ำตกเขาอีโต้ ====')
        print('''- กรุณาเลือกหัวข้อที่ต้องการ -
        1. คำนวนหาเส้นทางและระยะทางที่สั้นที่สุด
        2. เพิ่มข้อมูลสถานที่
        3. เพิ่มข้อมูลระยะทางของสถานที่
        4. แก้ไขข้อมูลสถานที่
        5. ลบข้อมูลสถานที่
        6. ลบข้อมูลระยะทางของสถานที่
        7. ออกจากโปรแกรม''')

        select_options = int(input('เลือกหัวข้อที่ต้องการ 1,2,3,4,5,6,7 : '))
        if select_options == 1:
            find_shortest_distance.find_shortest_comman()
            marker.mapOjp.save("index.html")  
        elif select_options == 2:
            insert_marker.insert_marker_comman()
        elif select_options == 3:
            insert_node.insert_Node_comman()
        elif select_options == 4:
            update_marker.update_marker_comman()
            marker.mapOjp.save("index.html")
        elif select_options == 5:
            del_marker.del_marker_comman()  
        elif select_options == 6:
            del_node.del_node_comman()
        print()
        
marker.mapOjp.save("index.html")
main()





