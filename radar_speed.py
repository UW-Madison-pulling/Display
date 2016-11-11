import serial
import json
import math

# CONFIG VARS
filename = "rada_data"
baud_rate = 19200
serial_location = '/dev/cu.usbmodem1421'

# CALIBRATION VARS
f_d = 10
speed_of_light = 0
angle = 35

ser = serial.Serial(serial_location, baud_rate)

print "Starting"
while True:
    try:
        data = json.loads(ser.readline()[:-2])  # output serial data
    except:
        continue
    if not math.isinf(data["frequency"]) and data["frequency"] > 0:
        f_not = data["frequency"]
        speed = (f_d * speed_of_light) / (2 * f_not * math.cos(math.radians(angle)))
        print speed
