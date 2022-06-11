import tkinter as tk
from tkinter.font import Font
import os
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

count  = 0 
def process(name,name2):
    count  = 0
    current_dir = os.getcwd()
    red = name
    nir = "nir.h264"
    red_v = os.path.join(current_dir,name)
    nir_v = os.path.join(current_dir,nir)
    cap = cv2.VideoCapture(red)
    frameRate = cap.get(5)

    ret,frame = cap.read()


    y = np.zeros(400)

    t = np.arange(400)
    im = cv2.imread(name2)
    r = cv2.selectROI(im)
    print(r)
    cv2.destroyAllWindows()

    while ret:
            count = count +1
            crop_frame = frame[int(r[0]):int(r[0]+10),int(r[1]):int(r[1]+10)]
                
                #gray = rgb2gray(crop_frame)
                #gray = img_as_float(crop_frame)
            img = Image.fromarray(crop_frame,'RGB')
            gray = img.convert('LA')
                #data = np.array(gray)
                #print(crop_frame)
                #gray = cv2.cvtColor(crop_frame,cv2.COLOR_BGR2GRAY)
                #print(gray)
            y[count] = np.mean(gray)
            ret,frame = cap.read()
    t = np.arange(400)
    t = t[1:count]
    t = t/30
    y = y[1:count]
    return y,count,t
#cv2.imshow('image',crop_frame)
           
#cv2.waitKey(0)
    # print(crop_frame)
    #print(frameRate)
t = np.arange(400)
t = t[1:300]
t = t/30

def filter1nd(y,count):
    
    ylength = y.shape
    y = y[1:count]
    
    #print(ylength)

    order = 6
    fs = 30
    cutoff  = 2

    b,a = signal.butter(2,2,fs=30)
    z = signal.filtfilt(b,a,y)
    return z
   
nir_black,count,t1 = process("nirblack.h264","redblack.jpg")
#nir_black = filter1nd(nir_black,count)
nir_hand,count,t2 = process("nirhand.h264","redhand.jpg")
#nir_hand = filter1nd(nir_hand,count)
nir_white,count,t3 = process("nirwhite.h264","redwhite.jpg")
#nir_white = filter1nd(nir_white,count)

ax = plt.gca()
ax.axis('auto')
ax.set_autoscaley_on(True)

plt.plot(t1,nir_black,label = "black")
plt.plot(t2,nir_hand,label = "hand")
plt.plot(t3,nir_white,label = "white")

#handles,labels = plt.get_legend_labels()

#plt.plot(t,y)
#plt.plot(t,z)

    #ymin = min(y)
    #ymax = max(y)
ax = plt.gca()
ax.axis('auto')
ax.set_autoscaley_on(True)
plt.legend(loc="upper left")
    #plt.ylim([50,150])
plt.show()
print(frameRate)
