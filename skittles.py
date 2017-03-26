import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)
skittles = GPIO.PWM(27, 100)
skittles.start(5)

for i in range(0,100):
	skittles.ChangeDutyCycle(i)
	time.sleep(0.2)
for i in range(100,0):
	skittles.ChangeDutyCycle(i)
	time.sleep(1)


		


