import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

### READ DATA LOG AND PRODUCE PLOTS
with open("/home/pi/grdnPI/sensor.log", 'r') as f:
	text = f.readlines()
	f.close()
x = []
y = []
for i in range(len(text)):
	data = text[i].split("***")
	dt = data[0] + " " + data[1]
	sm = int(data[-1].split()[-1].strip()[:-5])
	x.append(dt)
	y.append(sm)


# Create and save plot for last 3 days
fig1, ax1 = plt.subplots(1)
fig1.autofmt_xdate()
plt.title("Maker Garden 3-Day Moisture Log")
plt.xlabel("Date & Time")
plt.ylabel("Moisture Reading")
plt.plot(x[-36:], y[-36:])
plt.savefig("/home/pi/grdnPI/plot1.png")

# Create and save all-time data plot
fig1, ax1 = plt.subplots(1)
fig1.autofmt_xdate()
plt.title("Maker Garden Moisture Log")
plt.xlabel("Date & Time")
plt.ylabel("Moisture Reading")
plt.plot(x, y)
plt.savefig("/home/pi/grdnPI/plot2.png")

cmnd = "sudo python3 /home/pi/grdnPI/notify.py"
#os.system(cmnd)





