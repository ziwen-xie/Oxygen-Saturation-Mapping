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
    r, g, b = rgb[:,:,0],rgb[:,:,1],rgb[:,:,2]
    gray = 0.2989*r + 0.5870*g + 0.1140*b
    return gray

def ana4():
    count  = 0
    im = cv2.imread("red.jpg")
    r = cv2.selectROI(im)
    print(r)    
    current_dir = os.getcwd()
    red = "red.h264"
    nir = "nir.h264"
    red_v = os.path.join(current_dir,red)
    nir_v = os.path.join(current_dir,nir)
    cv2.destroyAllWindows()
    
    #RED
    cap = cv2.VideoCapture(red)
    frameRate = cap.get(5)
    ret,frame = cap.read()

    yred = np.zeros(900)
    tred = np.arange(900)
    while ret:
            count = count +1
            crop_frame = frame[int(r[0]):int(r[0]+10),int(r[1]):int(r[1]+10)]
            img = Image.fromarray(crop_frame,'RGB')
            gray = img.convert('LA')
            yred[count] = np.mean(gray)
            ret,frame = cap.read()
    

    yred = yred[1:count]
    tred = tred[1:count]
    tred = tred/60
    b,a = signal.butter(2,2,fs=30)
    zred = signal.filtfilt(b,a,yred)

    
    #NIR
    count2 = 0
    cap2 = cv2.VideoCapture(nir)
    frameRate2 = cap2.get(5)
    ret2,frame2 = cap2.read()

    ynir = np.zeros(900)
    tnir = np.arange(900)
    while ret2:
            count2 = count2 +1
            crop_frame2 = frame2[int(r[0]):int(r[0]+10),int(r[1]):int(r[1]+10)]
            img2 = Image.fromarray(crop_frame2,'RGB')
            gray2 = img2.convert('LA')
            ynir[count2] = np.mean(gray2)
            ret2,frame2 = cap2.read()
    
    ylength = ynir.shape
    fig = plt.figure()
    
    ynir = ynir[1:count2]
    tnir = tnir[1:count2]
    tnir = tnir/60
    b,a = signal.butter(2,2,fs=30)
    znir = signal.filtfilt(b,a,ynir)

    ax1 = fig.add_subplot(211)
    ax1.plot(tnir,znir)
    ax1.title.set_text("NIR")
    ax2 = fig.add_subplot(212)
    ax2.plot(tred,zred)
    ax2.title.set_text("RED")
    
    
    ax = plt.gca()
    ax.axis('auto')
    ax.set_autoscaley_on(True)
    
    
    
    plt.show()
    print(frameRate)
        

