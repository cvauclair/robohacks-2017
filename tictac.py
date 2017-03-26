import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
tictac = GPIO.PWM(4, 100)
tictac.start(5)

print("Dispensing tic tac")
for i in range(100,0):
	tictac.ChangeDutyCycle(i)
	time.sleep(1)
for i in range(0,100):
	tictac.ChangeDutyCycle(i)
	time.sleep(0.2)

