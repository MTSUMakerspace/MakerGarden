import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

### READ DATA LOG AND PRODUCE PLOTS
with open("/home/pi/MakerGarden/sensor.log", 'r') as f:
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
#fig1.autofmt_xdate(rotation=90)
ax1.set_xticks([23, 47, 71, 95, 119, 143, 167])
ax1.set_xticklabels(['1', '2', '3' ,'4', '5', '6', '7'])
plt.title("Maker Garden 7-Day Moisture Log")
plt.xlabel("Days")
plt.ylabel("Moisture Reading")
plt.plot(x[-168:], y[-168:])
plt.savefig("/home/pi/MakerGarden/plot1.png")

# Create and save all-time data plot
fig1, ax1 = plt.subplots(1)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.title("Maker Garden Moisture Log (all data)")
plt.xlabel("Date Range: " + x[0] + " - " + x[-1])
plt.ylabel("Moisture Reading")
plt.plot(x, y)
plt.savefig("/home/pi/MakerGarden/plot2.png")





