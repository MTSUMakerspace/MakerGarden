from rpi_ws281x import *
import time

LED_COUNT = 256
LED_PIN = 21
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
st = 1
r = 255
g = 0
b = 0
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

while True:
	while r > 0:
		for x in range(0, LED_COUNT):
			strip.setPixelColor(x, Color(r, g, b))
		strip.show()
		time.sleep(0.1)
		r = r - 1
		b = b + 1
	while b > 0:
		for x in range(0, LED_COUNT):
			strip.setPixelColor(x, Color(r, g, b))
		strip.show()
		time.sleep(0.1)
		r = r + 1
		b = b - 1
