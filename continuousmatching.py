#!/usr/bin/env python
# GPIO access
import add_image
import facematch
import take_selfie
import RPi.GPIO as GPIO

# Get the time and convert it to string
import time
from time import strftime, gmtime

# To run command (raspistill)
from subprocess import call

# To connect to FTP
from ftplib import FTP

# To run code on interrupt
#import signal
#import sys

#def cleanup(signal, frame):
#	print("Cleaning up...")
#	ftp.quit()

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#ftp = FTP("192.168.43.224")
#ftp.login("robot","robohacks")
#ftp.cwd("face-request")

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        image = take_selfie.main()
        facematch.main(image)

	
	#ftp.
        time.sleep(0.2)
