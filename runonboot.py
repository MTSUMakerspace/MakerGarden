import time
import os

cmnd = "sudo python3 /home/pi/grdnPI/sparkle.py &"
cmnd2 = "sudo python3 /home/pi/grdnPI/daily_report.py &"

dt = time.asctime().split()
t = dt[3].split(":")
h = int(t[0])

#os.system(cmnd2)

if h >= 6 and h < 18:
	os.system(cmnd)
	exit()
else:
	exit()
