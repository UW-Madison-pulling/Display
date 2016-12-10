import serial
import json
import math
import csv

# CONFIG VARS
baud_rate = 19200
serial_location = '/dev/cu.usbmodem1421'
filename = "radar_test"

ser = serial.Serial(serial_location, baud_rate)

print "Starting"
with open(filename + '.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while True:
        try:
            data = json.loads(ser.readline()[:-2])  # output serial data
            print data
            writer.writerow(data["time"], data["frequency"], data["pulse_count"], data["duration"])
        except:
            continue
