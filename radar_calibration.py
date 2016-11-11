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

ser = serial.Serial(serial_location, baud_rate)

print "Starting"
with open(filename + '.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while True:
        try:
            data = json.loads(ser.readline()[:-2])  # output serial data
        except:
            continue
        if not math.isinf(data["frequency"]) and data["frequency"] > 0:
            f_not = data["frequency"]
            f_d = 2 * speed * (f_not / speed_of_light) * math.cos(math.radians(angle))
            print f_d
            writer.writerow(data["time"], f_d, f_not)
