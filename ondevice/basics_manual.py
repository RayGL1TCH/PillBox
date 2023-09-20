import serial
import time

ser = serial.Serial('/dev/cu.usbmodem2101', 9600)

def send_command(command):
    ser.write(command.encode())

try:
    while True:
        cmd = input("Enter command:")
        if cmd == 'Q':
            break
        elif cmd in ['1', '2', '-1','-2','0']:
            send_command(cmd)
        else:
            print("Invalid command.")
except KeyboardInterrupt:
    pass

ser.close()
