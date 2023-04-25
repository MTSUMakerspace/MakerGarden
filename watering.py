import os

threshold = 600
cmnd = "python3 /home/pi/MakerGarden/sprinkle.py"

with open("sensorlog.txt", 'r') as f:
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

if y[-1] >= threshold:
	os.system(cmnd)

