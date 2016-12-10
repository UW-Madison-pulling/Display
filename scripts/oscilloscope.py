import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import json
import math
import time


# CONFIG VARS
baud_rate = 19200
serial_location = '/dev/cu.usbmodem1421'

ser = serial.Serial(serial_location, baud_rate)

def get_serial_data():
    stop = False
    while not stop:
        try:
            data = json.loads(ser.readline()[:-2])  # output serial data
        except:
            continue
        if not math.isinf(data["frequency"]) and data["frequency"] > 0:
            stop = True
            return data["time"], data["frequency"]

plt.ion() ## Note this correction
fig=plt.figure()
plt.axis([0,1000,0,800])

i=0
x = list()
y = list()

while i <1000:
    temp_x, temp_y = get_serial_data()
    x.append(i);
    y.append(temp_y);
    print temp_y
    plt.scatter(i,temp_y);
    i+=1;
    plt.show()
    plt.pause(0.0001) #Note this correction
