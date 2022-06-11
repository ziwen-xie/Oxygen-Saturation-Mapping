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
import sys
from record_start import record_start
STATE_0 = 0
STATE_QUIT = 1
STATE_REC = 2
state = STATE_0


def camera_handle():
    global state
    state = STATE_0
    
    ca = picamera.PiCamera()
    ca.sharpness = 0
    ca.contrast = 0
    ca.brightness = 50
    ca.saturation = 0
    ca.ISO = 0
    ca.video_stabilization = False
    ca.exposure_compensation = 0
    ca.rotation = 0
    ca.resolution = (640,480)
    
    while state != STATE_QUIT:
        if state == STATE_REC:
            print("Capture")
            state = STATE_0
            record_start()
        else:
            ca.sharpness = sharp.get()
            ca.contrast = contrast.get()
            ca.brightness = bright.get()
            ca.saturation = sat.get()
            ca.exposure_compensation = exp.get()
            
            stream = io.BytesIO()
            ca.capture(stream, format = 'jpeg')
            stream.seek(0)
            temp = Image.open(stream)
            temp2 = ImageTk.PhotoImage(tempImage)
            previewPanel.configure(image = temp2)
            
            