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

def ana2():
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
            im = rgb2gray(frame)
            yred[count] = np.mean(np.mean(im))
    
            ret,frame = cap.read()
    

    yred = yred[1:count]
    tred = tred[1:count]
    tred = tred/60
    
    
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
            im2 = rgb2gray(frame2)
            ynir[count2] = np.mean(np.mean(im2))
            ret2,frame2 = cap2.read()
    
    ylength = ynir.shape
    fig = plt.figure()
    
    ynir = ynir[1:count2]
    tnir = tnir[1:count2]
    tnir = tnir/60
    ax1 = fig.add_subplot(211)
    ax1.plot(tnir,ynir)
    ax1.title.set_text("NIR")
    ax2 = fig.add_subplot(212)
    ax2.plot(tred,yred)
    ax2.title.set_text("RED")
    
    
    ax = plt.gca()
    ax.axis('auto')
    ax.set_autoscaley_on(True)
    
    
    
    plt.show()
    print(frameRate)
        
