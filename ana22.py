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
import clique
import cv2
import glob



def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.144])

def ana22(r):
    count  = 0
    images = [cv2.imread(file) for file in glob.glob("./nirnir/*.jpg")]
    print(len(images[0][0][0]))
    #RED
    
    yred = np.zeros(900)
    tred = np.arange(900)
   
    for i in range(len(images[0])):
            count = count +1
            crop_frame = images[i][int(r[0]):int(r[0]+10),int(r[1]):int(r[1]+10)]
            im = rgb2gray(crop_frame)
            yred[count] = np.mean(np.mean(im))
    

    

    yred = yred[1:count]
    tred = tred[1:count]
    tred = tred/60
    
    

    imagered = [cv2.imread(file) for file in glob.glob("./redred/*.jpg")]
    ynir = np.zeros(900)
    tnir = np.arange(900)
    count2 = 0
    for j in range(len(imagered[0])):
            count2 = count2 +1
            crop_frame = imagered[j][int(r[0]):int(r[0]+10),int(r[1]):int(r[1]+10)]
            im = rgb2gray(crop_frame)
            ynir[count2] = np.mean(np.mean(im))
    
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
     
r = [100,100]
ana22(r)