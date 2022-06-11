from time import sleep
import picamera
from picamera import PiCamera
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(12,GPIO.OUT, initial = GPIO.LOW)

ca=picamera.PiCamera()
ca.resolution = (640,480)
ca.capture('white.jpg')

GPIO.output(12,GPIO.HIGH)
sleep(120)
ca.capture('red.jpg')
sleep(1)
ca.start_recording('red.h264')
ca.wait_recording(10)
ca.stop_recording()
GPIO.output(12,GPIO.LOW)


GPIO.output(18,GPIO.HIGH)
ca.capture('nir.jpg')
sleep(1)
ca.start_recording('nir.h264')
ca.wait_recording(10)
ca.stop_recording()
GPIO.output(18,GPIO.LOW)



