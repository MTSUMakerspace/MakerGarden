import time
import RPi.GPIO as GPIO

PIN = 26
DUR = 45

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.LOW)


print("Turning pump on")
GPIO.output(PIN, GPIO.HIGH)
time.sleep(DUR)
print("Turning pump off")
GPIO.output(PIN, GPIO.LOW)

print("Process finished")
exit()
