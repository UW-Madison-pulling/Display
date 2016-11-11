import serial
import json
import math

# CONFIG VARS
baud_rate = 19200
serial_location = '/dev/cu.usbmodem1421'

ser = serial.Serial(serial_location, baud_rate)

print "Starting"
while True:
    try:
        data = json.loads(ser.readline()[:-2])  # output serial data
    except:
        continue
    if not math.isinf(data["frequency"]) and data["frequency"] > 0:
        print data["frequency"]

# ser.write('5')  # write through serial
