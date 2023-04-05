from rpi_ws281x import *
import time
import os

LED_COUNT = 256
LED_PIN = 21
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
st = 1

cmnd = "sudo kill $(pgrep -f '/usr/bin/python3 /home/pi/grdnPI/sparkle.py')"
os.system(cmnd)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

for i in range(LED_COUNT):
	strip.setPixelColor(i, Color(0, 0, 0))
strip.show()
exit()
