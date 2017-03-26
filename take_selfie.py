<<<<<<< HEAD
from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    imwrite("../faces/currentimage.jpg",img) #save image
=======
#!/usr/bin/env python

from picamera import PiCamera
import time
def main():
	count = 2
	camera = PiCamera()

	print '[+] A photo will be taken in 10 seconds...'

	for i in range(count):
    	print (count - i)
    	time.sleep(1)

	milli = int(round(time.time() * 1000))
	image = '/home/pi/pi-detector/faces/image_%r.jpg' % milli
	camera.capture(image)
	print 'Your image was saved to %s' % image
	return image

if __name__ == '__main__':
	main()
>>>>>>> d86c510e2fb486d84f29686ea994608ae5453312
