import tkinter as tk
from tkinter.font import Font
import os
from record_start import record_start
from PIL import ImageTk, Image, ImageOps
from threading import Thread
from time import sleep
import picamera
from picamera import PiCamera
import RPi.GPIO as GPIO
import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib import image as mpimg
from threading import Thread
import io
import sys
import cv2
from record_start import record_start

from threading import Thread
import io
import sys
import cv2
from scipy import signal

def butter_lowpass(cutoff,fs,order):
    return butter(order,cutoff,fs=fs,btype='low',analog=False)

def butter_lowpass_filter(data,cutoff,fs,order):
    b,a = butter_lowpass(cutoff,fs,order = order)
    y = lfilter(b,a,data)
    return y

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.144])
def ana():
    count  = 0
            
    current_dir = os.getcwd()
    red = "nir.h264"
    nir = "nir.h264"
    red_v = os.path.join(current_dir,red)
    nir_v = os.path.join(current_dir,nir)
    cap = cv2.VideoCapture(red)
    frameRate = cap.get(5)

    ret,frame = cap.read()


    y = np.zeros(900)

    t = np.arange(400)
    im = cv2.imread("nir.jpg")
    r = cv2.selectROI(im)
    print(r)


    while ret:
            count = count +1
            crop_frame = frame[int(r[0]):int(r[0]+10),int(r[1]):int(r[1]+10)]
             im = rgb2gray(crop_frame)
             y[count] = np.mean(np.mean(im))
            ret,frame = cap.read()
    

    ylength = y.shape
    y = y[1:count]
    t = t[1:count]
    t = t/30
        #print(ylength)

    order = 6
    fs = 30
    cutoff  = 2

    b,a = signal.butter(2,2,fs=30)
    z = signal.filtfilt(b,a,y)



    plt.plot(t,y)
    plt.plot(t,z)

        #ymin = min(y)
        #ymax = max(y)
    ax = plt.gca()
    ax.axis('auto')
    ax.set_autoscaley_on(True)
        #plt.ylim([50,150])
    plt.show()
    print(frameRate)
    plt.plot(t,z)
    plt.show()
