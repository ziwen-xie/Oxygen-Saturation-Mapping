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
from scipy import signal
import glob



def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.144])
def butter_lowpass(cutoff,fs,order):
    return butter(order,cutoff,fs=fs,btype='low',analog=False)

def butter_lowpass_filter(data,cutoff,fs,order):
    b,a = butter_lowpass(cutoff,fs,order = order)
    y = lfilter(b,a,data)
    return y

def ana22(r,step):
    count  = 0
    images = [cv2.imread(file) for file in glob.glob("./redred/*.jpg")]
    #print(len(images[0][0][0]))
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
    b,a = signal.butter(2,2,fs=30)
    zred = signal.filtfilt(b,a,yred)
    
    maxredl = signal.argrelextrema(yred,np.greater)
    minredl = signal.argrelextrema(yred,np.less)
    length = min(maxredl[0].size,minredl[0].size)
    if (maxredl[0][0] < minredl[0][0]):
        maxred = yred[maxredl]
        minred = yred[minredl]
    else:
        maxred = yred[maxredl]
        minred = yred[minredl]
        maxred = maxred[1:maxred.size]
        
    lengthr = min(maxred.size,minred.size)
    maxred = maxred[1:lengthr]
    minred = minred[1:lengthr]
    ACDCred = abs(maxred-minred)/minred
    ACDCred = np.mean(ACDCred)
    
    
    

    imagered = [cv2.imread(file) for file in glob.glob("./nirnir/*.jpg")]
    ynir = np.zeros(900)
    tnir = np.arange(900)
    count2 = 0
    for j in range(len(imagered[0])):
            count2 = count2 +1
            crop_frame = imagered[j][int(r[0]):int(r[0]+10),int(r[1]):int(r[1]+10)]
            im = rgb2gray(crop_frame)
            ynir[count2] = np.mean(np.mean(im))
    
    ylength = ynir.shape
    
    
    ynir = ynir[1:count2]
    tnir = tnir[1:count2]
    tnir = tnir/60
    maxnirl = signal.argrelextrema(ynir,np.greater)
    minnirl = signal.argrelextrema(ynir,np.less)
    length = min(maxnirl[0].size,minnirl[0].size)
    if (maxnirl[0][0] < minnirl[0][0]):
        maxnir = ynir[maxnirl]
        minnir = ynir[minnirl]
    else:
        maxnir = ynir[maxnirl]
        minnir = ynir[minnirl]
        maxnir = maxnir[1:maxnir.size]
    length = min(maxnir.size,minnir.size)
    maxnir = maxnir[0:length]
    minnir = minnir[0:length]
    ACDCnir = abs(maxnir-minnir)/minnir
    ACDCnir = np.mean(ACDCnir)
    #print(ACDCnir)
    #print(ACDCred)
    R = ACDCnir/ACDCred
    
    return R

def mapping():
    step = 150
    countx = 0
    county = 0
    R1 = np.zeros((int(300/step),int(300/step)))
    print(R1)
    """
    im = cv2.imread("red.jpg")
    r = cv2.selectROI(im)
    cv2.destroyAllWindows()
    e624 = [774,5906.8]
    e940 = [1214,693.44]
    R = ana22(r)
    R = R*0.98
    SAO2 = (e624[1]-R*e940[1])/((R*e940[0]-R*e940[1])+(e624[1]-e624[0]))

    R1 = np.zeros((300,300))
    """

    for x in range(0,int(300/step)):
        #print(x)
        county = 0
        for y in range(0,int(300/step)):
            r = [x*step,y*step]
            e624 = [774,5906.8]
            e940 = [1214,693.44]
            R = ana22(r,step)
            #print(countx)
            #print(county)
            R1[countx][county] = 0.9*(e624[1]-R*e940[1])/((R*e940[0]-R*e940[1])+(e624[1]-e624[0]))
            print(R1)
            county = county+1
        countx = countx+1  

    R1 = R1[0:countx,0:county]
    #print(R1)
            
    #print(r)
    #print(SAO2)
    #plt.rcParams["figure.figsize"]=[7.00,3.50]
    #plt.rcParams["figure/autolayout"]=True
    plt.imshow(R1,extent=[0,300,0,300])
    plt.colorbar()
    plt.show()


