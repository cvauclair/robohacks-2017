import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
tictac = GPIO.PWM(4, 100)
tictac.start(5)

GPIO.setup(27, GPIO.OUT)
skittles = GPIO.PWM(27, 100)
skittles.start(5)

GPIO.setup(17, GPIO.OUT)
mikeike = GPIO.PWM(17, 100)
mikeike.start(5)

#med = sys.argv[0]

for arg in sys.argv[1:]:
	if arg == "tictac":
		print("Dispensing tic tac")
		for i in range(0,100):
			tictac.ChangeDutyCycle(i)
			time.sleep(0.2)
		for i in range(100,0):
			tictac.ChangeDutyCycle(i)
			time.sleep(1)
	if arg == "skittles":
		print("Dispensing skittles")
		for i in range(0,100):
			skittles.ChangeDutyCycle(i)
			time.sleep(0.2)
		for i in range(100,0):
			skittles.ChangeDutyCycle(i)
			time.sleep(1)
	if arg == "mikeike":
		print("Dispensing mikeike")
		for i in range(0,100):
			mikeike.ChangeDutyCycle(i)
			time.sleep(0.2)
		for i in range(100,0):
			mikeike.ChangeDutyCycle(i)
			time.sleep(1)
		


