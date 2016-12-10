import serial
import json
import csv
import math

# CONFIG VARS
filename = "rada_data"
baud_rate = 19200
serial_location = '/dev/cu.usbmodem1421'

# CALIBRATION VARS
speed = 10
speed_of_light = 0
angle = 35

# ser = serial.Serial(serial_location, baud_rate)

print "Starting"
print "Ctrl+C to start"
try:
    while True:
        i = 0
except KeyboardInterrupt:
    pass

f_not_list = []
f_d_list = []
while True:
    try:
        data = json.loads(ser.readline()[:-2])  # output serial data
        if not math.isinf(data["frequency"]) and data["frequency"] > 0:
            f_not = data["frequency"]
            f_d = 2 * speed * (f_not / speed_of_light) * math.cos(math.radians(angle))
            print f_not + ", " + f_d
            f_not_list.append(f_not)
            f_d_list.append(f_d)
    except:
        continue

try:
    while True:
        i = 0
except KeyboardInterrupt:
    pass

with open(filename + '.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for item in zip(f_d_list, f_not_list):
        writer.writerow(data["time"], item["f_d"], item["f_not"])
