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
from skimage import io, img_as_float
import skimage.color
import skimage.io
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib import image as mpimg
from threading import Thread
import io
import sys
import cv2

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.144])

def ana3():
    count  = 0
        
    current_dir = os.getcwd()
    red = "red.h264"
    nir = "nir.h264"
    red_v = os.path.join(current_dir,red)
    nir_v = os.path.join(current_dir,nir)
    cap = cv2.VideoCapture(nir)
    frameRate = cap.get(5)

    ret,frame = cap.read()


    y = np.zeros(900)

    t = np.arange(900)



    while ret:
            count = count +1
            crop_frame = frame[40:88,60:72]
            
            im = rgb2gray(crop_frame)
            #gray = rgb2gray(crop_frame)
            #gray = img_as_float(crop_frame)
            ##img = Image.fromarray(crop_frame,'RGB')
            ##gray = img.convert('LA')
            #data = np.array(gray)
            #print(crop_frame)
            #gray = cv2.cvtColor(crop_frame,cv2.COLOR_BGR2GRAY)
            #print(gray)
            y[count] = np.mean(np.mean(im))
            ret,frame = cap.read()
    #cv2.imshow('image',crop_frame)
           
    #cv2.waitKey(0)
    # print(crop_frame)
    #print(frameRate)
    ylength = y.shape
    y = y[1:count]
    t = t[1:count]
    t=t/60
    #print(ylength)
    plt.plot(t,y)
    #ymin = min(y)
    #ymax = max(y)
    ax = plt.gca()
    ax.axis('auto')
    ax.set_autoscaley_on(True)
    #plt.ylim([50,150])
    plt.show()
    print(frameRate)
        

        
