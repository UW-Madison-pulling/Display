import serial
import json
import csv
import math

# CONFIG VARS
filename = "rada_data"
baud_rate = 19200
serial_location = '/dev/cu.usbmodem1421'

ser = serial.Serial(serial_location, baud_rate)

print "Starting"
with open(filename + '.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while True:
        try:
            data = json.loads(ser.readline()[:-2])  # output serial data
        except:
            continue
        if not math.isinf(data["frequency"]) and data["frequency"] > 0:
            print data["frequency"]
            writer.writerow(data["time"], data["frequency"])

# ser.write('5')  # write through serial
