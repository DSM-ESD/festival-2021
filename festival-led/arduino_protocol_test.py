import serial
from time import sleep

ser = serial.Serial( # 아두이노와 연결된 Serial 설정
	port='COM17',
	baudrate=115200, 
	parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

if __name__ == "__main__":
    while True:
        ser.write(b'\x021111\x03')
        sleep(2)

        ser.write(b'\x020000\x03')
        sleep(2)