from time import sleep
import picamera
from picamera import PiCamera
import RPi.GPIO as GPIO
import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(12,GPIO.OUT, initial = GPIO.LOW)

ca=picamera.PiCamera()
ca.resolution = (640,480)
ca.capture('white.jpg')

GPIO.output(12,GPIO.HIGH)
pwm = GPIO.PWM(12,60)
pwm.start(10)
pwm.ChangeDutyCycle(30)
sleep(1)
ca.capture('red.jpg')
sleep(1)
ca.start_recording('red.h264')
ca.wait_recording(10)
ca.stop_recording()
GPIO.output(12,GPIO.LOW)


GPIO.output(18,GPIO.HIGH)
pwm = GPIO.PWM(18,60)
pwm.start(10)
pwm.ChangeDutyCycle(100)
sleep(1)
ca.capture('nir.jpg')
sleep(1)
ca.start_recording('nir.h264')
ca.wait_recording(10)
ca.stop_recording()
GPIO.output(18,GPIO.LOW)

image = skimage.io.imread(fname = '/home/pi/SD/red.jpg',as_gray = True)

fig,ax = plt.subplots(4)
ax[0].imshow(image, cmap='gray')

histogram, bin_edges = np.histogram(image,bins = 256,range=(0,1))
ax[1].plot(bin_edges[0:-1],histogram)

image2 = skimage.io.imread(fname = '/home/pi/SD/nir.jpg',as_gray = True)
ax[2].imshow(image, cmap='gray')

histogram, bin_edges = np.histogram(image2,bins = 256,range=(0,1))
ax[3].plot(bin_edges[0:-1],histogram)


plt.show()


