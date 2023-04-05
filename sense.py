import os
import serial
from datetime import datetime

ser = serial.Serial('/dev/ttyUSB0', 9600)
data = str(ser.readline())
ser.close()
now = datetime.now()
dat = now.strftime("%m/%d/%Y***%H:%M:%S")
ln = dat + "***" + data + "\n"

with open("/home/pi/MakerGarden/sensor.log", 'a') as f:
	f.write(ln)
	f.close()

