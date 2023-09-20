from urllib.request import urlopen
import datetime
from datetime import datetime, date
import datetime
import serial
import time
import json

ser = serial.Serial('/dev/cu.usbmodem101', 9600)

def send_command(command):
    ser.write(command.encode('ascii'))
    time.sleep(0.2)

def preprocess_hack(pre_command):
    if pre_command in ['1', '2', '3','4','5','6','0']:
        send_command(pre_command)
# Debug function
def load_schedule(file_path):
    with open(file_path, 'r') as file:
        schedule = json.load(file)
    return schedule

def get_current_day():
    return time.strftime("%A")

# A,B,C,D=1,2,3,4,5,6
def open_a():
    preprocess_hack('1')
    print('Sent command: 1')
    time.sleep(1)
    preprocess_hack('5')
def open_b():
    preprocess_hack('3')
    print('Sent command: 3')
    time.sleep(1)
    preprocess_hack('6')
def close_a():
    preprocess_hack('2')
    print('Sent command: 2')
    time.sleep(1)
    preprocess_hack('5')
def close_b():
    preprocess_hack('4')
    print('Sent command: 4')
    time.sleep(1)
    preprocess_hack('6')
    

id = 2
url = "http://127.0.0.1:5000/device_data/" + str(id)

response = urlopen(url)
data = json.loads(response.read())
print("Data received from server:")
print(data)
# {'medication1': {'name': 'test', 'times': ['9:00', '8:00'], 'gap_days': '1'}, 
# 'medication2': {'name': 'best', 'times': ['8:00'], 'gap_days': '2'}, 'todays_date': '2023-09-21'}
try:
    # schedule = load_schedule('schedule.json')
    while True:
        ondevice_date = date.today()
        json_date = date.fromisoformat(data['todays_date'])
        # current_day = get_current_day()
        date_difference = ondevice_date - json_date
        current_time = datetime.datetime.now()
        if date_difference.days % (int(data['medication1']['gap_days'])+1) == 0:
            print("medication 1 due for today")
            for time_str in data['medication1']['times']:
                # time_object = datetime.datetime.strptime(time_str, '%H:%M')
                time_process=datetime.datetime.strptime(time_str, '%H:%M').time()
                time_object = datetime.datetime.combine(datetime.date.today(),time_process)
                # if current_time == time:
                if abs(current_time-time_object)<datetime.timedelta(minutes=1):
                    print('Opening box A')
                    open_a()

        if date_difference.days % (int(data['medication2']['gap_days'])+1) == 0:
            print("medication 2 due for today")
            for time_str in data['medication2']['times']:
                # time_object = datetime.datetime.strptime(time_str, '%H:%M')
                time_process=datetime.datetime.strptime(time_str, '%H:%M').time()
                time_object = datetime.datetime.combine(datetime.date.today(),time_process)
                # if current_time == time:
                if abs(current_time-time_object)<datetime.timedelta(minutes=1):
                    print('Opening box B')
                    open_b()
        time.sleep(40)
        
        # if current_time in schedule[current_day]:
        #     send_command(schedule[current_day][current_time])
        #     print('Sent command: ' + schedule[current_day][current_time])
        # time.sleep(40)
except KeyboardInterrupt:
    pass
ser.close()
