import serial


# CONFIG VARS
baud_rate = 19200
serial_location = '/dev/tty.usbserial'

ser = serial.Serial(serial_location, baud_rate)

while True:
    print ser.readline()  # output serial data
    # ser.write('5')  # write through serial
