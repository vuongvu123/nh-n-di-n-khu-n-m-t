import serial
import time

def send_data_to_arduino(data, port='COM3', baudrate=9600):
    try:
        # Kết nối với Arduino qua cổng serial
        arduino = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # Đợi cho kết nối ổn định

        # Gửi dữ liệu đến Arduino
        arduino.write(data.encode())
        print(f"Gửi dữ liệu: {data}")

        # Đọc phản hồi từ Arduino (nếu có)
        response = arduino.readline().decode().strip()
        if response:
            print(f"Phản hồi từ Arduino: {response}")

        # Đóng kết nối
        arduino.close()
    except serial.SerialException as e:
        print(f"Lỗi kết nối serial: {e}")
    except Exception as e:
        print(f"Lỗi: {e}")

# Ví dụ sử dụng
send_data_to_arduino("Hello, Arduino!")
