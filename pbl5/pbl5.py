import mysql.connector
import serial
import time


db = mysql.connector.connect(
    host="localhost",           
    user="root",                
    password="",                
    database="sv"    
)


ser = serial.Serial('COM5', 9600)  # Thay đổi cổng serial tùy thuộc vào Arduino của bạn

def get_data_from_db(name):
    cursor = db.cursor()
    query = "SELECT Tên, Lớp FROM sv WHERE MSSV = %s LIMIT 1"
    cursor.execute(query, (name,))
    row = cursor.fetchone()
    cursor.close()
    return row
def send_data_to_arduino(data):
    if data:
        ten, lop = data
        ser.write(f"{ten}\n".encode())  # Gửi MSSV
        time.sleep(1)  # Đợi một chút để Arduino xử lý dữ liệu
        ser.write(f"{lop}\n".encode())  # Gửi lớp
        time.sleep(1)  # Đợi một chút để Arduino xử lý dữ liệu


time.sleep(2)


MSSV = input("MSSV: ")


data = get_data_from_db(MSSV)
if data:
    send_data_to_arduino(data)
    print("Data sent to Arduino:", data)
else:
    print("Không tìm thấy dữ liệu cho MSSV:", MSSV)


ser.close()
db.close()
