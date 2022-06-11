from time import sleep
import picamera
from picamera import PiCamera
import RPi.GPIO as GPIO
import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt

ca=picamera.PiCamera()
ca.resolution = (640,480)
ca.capture('white.jpg')

ca.start_recording('nir_test.h264')
ca.wait_recording(10)
ca.stop_recording()