import serial
import time

ser = serial.Serial('/dev/cu.usbmodem101', 9600)

def send_command(command):
    ser.write(command.encode('ascii'))
    time.sleep(0.3)  

# send_command('4')

try:
    while True:
        cmd = input("Enter command:")
        if cmd == 'Q':
            break
        elif cmd in ['1', '2', '3','4','5','6','0']:
            send_command(cmd)
        else:
            print("Invalid command.")
except KeyboardInterrupt:
    pass

ser.close()
