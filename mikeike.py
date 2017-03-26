import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
mikeike = GPIO.PWM(17, 100)
mikeike.start(5)

print("Dispensing mikeike")
for i in range(0,100):
	mikeike.ChangeDutyCycle(i)
	time.sleep(0.2)
for i in range(100,0):
	mikeike.ChangeDutyCycle(i)
	time.sleep(1)
		


