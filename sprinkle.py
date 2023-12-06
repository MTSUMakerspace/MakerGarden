import time
import RPi.GPIO as GPIO

PIN = 26

with open('config.txt', 'r') as f:
    data = f.readlines()
    f.close()

params = []
for i in range(3):
    params.append(int(data[i].strip().split(":")[1]))

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.LOW)


print("Turning pump on")
GPIO.output(PIN, GPIO.HIGH)
time.sleep(params[2])
print("Turning pump off")
GPIO.output(PIN, GPIO.LOW)

print("Process finished")
exit()
