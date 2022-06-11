import tkinter as tk
from tkinter.font import Font
import os
from PIL import ImageTk, Image
from time import sleep
import picamera
from picamera import PiCamera
import RPi.GPIO as GPIO
import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt
from threading import Thread
import io
import shutil
import sys
from time import strftime



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(13,GPIO.OUT, initial = GPIO.LOW)
pwm = GPIO.PWM(19,500)
pwm2 = GPIO.PWM(13,500)

frames = 300
def filename1():
    frame = 0
    while frame <frames:
        yield './nirnir/image%02d.jpg'%frame
        frame +=1
def filename2():
    frame = 0
    while frame <frames:
        yield './redred/image%02d.jpg'%frame
        frame +=1        
        
ca = picamera.PiCamera()
ca.framerate = 60
#ca.video_stabilization = False
#ca.iso = 600
#ca.analog_gain = 1
ca.iso = 400

ca.exposure_compensation = 0
#ca.rotation = 0
ca.resolution = (300,300)    
ins1 = 30
ins2 = 100

print("Capture")
GPIO.output(19,GPIO.HIGH)
pwm.start(10)
pwm.ChangeDutyCycle(ins1)

ca.start_preview()

sleep(2)     


ca.capture_sequence(filename2(),use_video_port=True)
            
pwm.stop()
GPIO.output(19,GPIO.LOW)
GPIO.output(13,GPIO.HIGH)
pwm2.start(10)
pwm2.ChangeDutyCycle(ins2)
sleep(1)
            

sleep(2)
ca.capture_sequence(filename1(),use_video_port=True)
           
pwm2.stop()
GPIO.output(13,GPIO.LOW)
ca.stop_preview()
print('end')