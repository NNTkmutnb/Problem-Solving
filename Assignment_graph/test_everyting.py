def compare_list_to_dict(data_list, data_dict):
    # สร้าง list เพื่อเก็บค่า value ที่สอดคล้องกับเงื่อนไข
    result_list = []
    
    # ใช้ for loop เพื่อวนลูปผ่านข้อมูลใน list
    for item in data_list:
        # เช็คว่าข้อมูลใน list เป็น key ใน dictionary หรือไม่
        if item in data_dict:
            # หากเป็น key ใน dictionary ให้นำค่า value มาเพิ่มใน result_list
            result_list.append(item)
            result_list.append(data_dict[item])
    
    return result_list

# ตัวอย่างการใช้งานฟังก์ชัน
data_list = [1, 2, 3, 4]
data_dict = {1: 1, 2: 2, 3: 3}

result = compare_list_to_dict(data_list, data_dict)
print("ผลลัพธ์:", result)
