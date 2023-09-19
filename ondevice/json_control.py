import serial
import time
import json

ser = serial.Serial('/dev/cu.usbmodem2101', 9600)

def send_command(command):
    ser.write(command.encode())

def load_schedule(file_path):
    with open(file_path, 'r') as file:
        schedule = json.load(file)
    return schedule

def get_current_day():
    return time.strftime("%A")


try:
    schedule = load_schedule('schedule.json')
    while True:
        current_day = get_current_day()
        current_time = time.strftime("%H:%M:%S")
        if current_time in schedule[current_day]:
            send_command(schedule[current_day][current_time])
            print('Sent command: ' + schedule[current_day][current_time])
        time.sleep(60)
except KeyboardInterrupt:
    pass
ser.close()
