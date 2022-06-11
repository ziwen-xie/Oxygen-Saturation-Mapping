import tkinter as tk
from tkinter.font import Font
import os
from record_start import record_start
from PIL import ImageTk, Image
from threading import Thread
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
from record_start import record_start
from ana2 import ana2
from ana4 import ana4
from ana3 import ana3
from time import strftime
from plot3 import plot3
from darknoise import darknoise


STATE_0 = 0
STATE_QUIT = 1
STATE_REC = 2
STATE_R1 = 3
STATE_N1 = 4
STATE_R1S = 5
STATE_N1S = 6
STATE_TEST = 7
STATE_ANA = 8
STATE_ANAN = 9
STATE_SELECT = 10
state = STATE_0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(13,GPIO.OUT, initial = GPIO.LOW)
pwm = GPIO.PWM(19,500)
pwm2 = GPIO.PWM(13,500)

#CREATE WINDOW
root = tk.Tk()
root.geometry("700x700")

f = Font(
    family = 'Piboto Thin',
    size = 15
    )

def pre():
    camThread = Thread(target = camera_handle)
    camThread.start()
    
def q():
    global state
    state = STATE_QUIT
    
    global root
    root.destroy()

def start():
    global state
    state = STATE_REC
    
def R1():
    global state
    state = STATE_R1
    
def N1():
    global state
    state = STATE_N1
    
def R1S():
    global state
    state = STATE_R1S
    
def N1S():
    global state
    state = STATE_N1S



def save_as():
    day = strftime("%d")
    month = strftime("%B")
    wholedate = strftime("%m_%d_%y_%H_%M_%S%p")
    print(wholedate)
    
    n = wholedate
    if (folder_n.get() != ""):
        n = folder_n.get()
    current_dir = os.getcwd()
    red = "red.h264"
    redi = "red.jpg"
    nir = "nir.h264"
    niri = "nir.jpg"
    white = "white.jpg"
    red_p = os.path.join(current_dir,red)
    nir_p = os.path.join(current_dir,nir)
    redi_p = os.path.join(current_dir,redi)
    niri_p = os.path.join(current_dir,niri)
    white_p = os.path.join(current_dir,white)
    
    if (os.path.exists(n) == False):
        dest_path = os.path.join(current_dir,n)
        os.mkdir(dest_path)
    shutil.copy(red_p,dest_path)
    shutil.copy(nir_p,dest_path)
    shutil.copy(niri_p,dest_path)
    shutil.copy(redi_p,dest_path)
    shutil.copy(white_p,dest_path)
 
def ana():
    global state
    state = STATE_ANA
    
def anan():
    global state
    state = STATE_ANAN

def testtest():
    global state
    state = STATE_TEST

def sel():
    global state
    state = STATE_SELECT
    
def blink():
    i = 0
    while i<11:
        GPIO.output(19,GPIO.HIGH)
        pwm.start(10)
        pwm.ChangeDutyCycle(30)
        sleep(1)
        pwm.stop()
        GPIO.output(19,GPIO.LOW)
        sleep(1)
        i = i + 1
        
prev = tk.Toplevel(root)
previewPanel = tk.Label(prev)
previewPanel.pack()

submit = tk.Button(root,text = "Start Recording", bg = 'black',fg = "white",command = start)
submit.grid(row = 0,column = 0)

quit_button = tk.Button(root,text = "quit", bg = 'black',fg = "white",command = q)
quit_button.grid(row = 0,column = 1)

LED_control_R_1 = tk.Button(root,text = "Open RED(640nm)", bg = 'black',fg = "white",command = R1)
LED_control_R_1.grid(row = 1,column = 0)

LED_control_N_1 = tk.Button(root,text = "Open NIR(940nm)", bg = 'black',fg = "white",command = N1)
LED_control_N_1.grid(row = 1,column = 2)

LED_stop_R_1 = tk.Button(root,text = "Stop Red(640nm)", bg = 'black',fg = "white",command = R1S)
LED_stop_R_1.grid(row = 1,column = 1)

LED_stop_N_1 = tk.Button(root,text = "Stop NIR(940nm)", bg = 'black',fg = "white",command = N1S)
LED_stop_N_1.grid(row = 1,column = 3)

analyze = tk.Button(root,text = "Analyze", bg = 'black',fg = "white",command = ana)
analyze.grid(row = 2,column = 0)

analyze2 = tk.Button(root,text = "Analyze", bg = 'black',fg = "white",command = anan)
analyze2.grid(row = 2,column = 1)

save_video = tk.Button(root,text = "Save Video", bg = 'black',fg = "white",command = save_as)
save_video.grid(row = 0,column = 3)

folder_n = tk.Entry(root,font =f)
folder_n.grid(row = 0,column = 2)

select = tk.Button(root,text = "plot3", bg = 'black',fg = "white",command = sel)
select.grid(row = 2,column = 3)

test1 = tk.Button(root,text = "test", bg = 'black',fg = "white",command = testtest)
test1.grid(row = 2,column = 2)


w = 300

sp = tk.Scale(
    root,
    from_ = 0,to = 33333,
    length = w,
    orient = tk.HORIZONTAL,
    label = "sharp"
   )
sp.set(16666.5)
sp.grid(row = 3,column = 0,columnspan = 2)

contrast = tk.Scale(
    root,
    from_ = -100,to = 100,
    length = w,
    orient = tk.HORIZONTAL,
    label = "contrast"
   )
contrast.set(0)
contrast.grid(row = 4,column = 0,columnspan = 2)

bright = tk.Scale(
    root,
    from_ = 0,to = 100,
    length = w,
    orient = tk.HORIZONTAL,
    label = "bright"
   )
bright.set(50)
bright.grid(row = 5,column = 0,columnspan = 2)


sat = tk.Scale(
    root,
    from_ = -100,to = 100,
    length = w,
    orient = tk.HORIZONTAL,
    label = "sat"
   )
sat.set(0)
sat.grid(row = 6,column = 0,columnspan = 2)

exp = tk.Scale(
    root,
    from_ = 100,to = 800,
    length = w,
    orient = tk.HORIZONTAL,
    label = "ISO"
   )
exp.set(600)
exp.grid(row = 7,column = 0,columnspan = 2)


intensity1 = tk.Scale(
    root,
    from_ = 0,to = 100,
    length = w,
    orient = tk.HORIZONTAL,
    label = "red intensity"
   )
intensity1.set(30)
intensity1.grid(row = 8,column = 0,columnspan = 2)

intensity2 = tk.Scale(
    root,
    from_ = 0,to = 100,
    length = w,
    orient = tk.HORIZONTAL,
    label = "nir intensity"
   )
intensity2.set(100)
intensity2.grid(row = 9,column = 0,columnspan = 2)

#functions



def camera_handle():
    global state
    state = STATE_0
    
    ca = picamera.PiCamera()
    #ca.framerate = 30
    #ca.ISO = 800
    ca.video_stabilization = False
    ca.exposure_compensation = 0
    ca.rotation = 0
    ca.resolution = (300,300)
    
    ins1 = intensity1.get()
    ins2 = intensity2.get()
    
    
    
    while state != STATE_QUIT:
        if state == STATE_REC:
            print("Capture")
            #ca.shutter_speed = sp.get()
            #ca.contrast = contrast.get()
            #ca.brightness = bright.get()
            #ca.saturation = sat.get()
            ca.ISO = exp.get()
            #ca.video_denoise = True
            
            #ca.iso = 400
            
            #ca.exposure_mode = 'off'
            
            state = STATE_0
            #ins1 = intensity1.get()
            #ins2 = intensity2.get()
            

            
            ca.capture('white.jpg')

            GPIO.output(19,GPIO.HIGH)
            pwm.start(10)
            pwm.ChangeDutyCycle(ins1)
            sleep(1)
            ca.capture('red.jpg')
            sleep(2)
            ca.start_recording('red.h264')
            #ca.start_preview()
            ca.wait_recording(4)
            ca.stop_recording()
            #ca.stop_preview()
            pwm.stop()
            GPIO.output(19,GPIO.LOW)
            GPIO.output(13,GPIO.HIGH)
            pwm2.start(10)
            pwm2.ChangeDutyCycle(ins2)
            sleep(1)
            ca.capture('nir.jpg')
            sleep(2)
            ca.start_recording('nir.h264')
            #ca.start_preview()
            ca.wait_recording(4)
            ca.stop_recording()
            #ca.stop_preview()
            pwm2.stop()
            GPIO.output(13,GPIO.LOW)
            """
            image = skimage.io.imread(fname = '/home/pi/SD/red.jpg',as_gray = True)

            fig,ax = plt.subplots(4)
            ax[0].imshow(image, cmap='gray')

            histogram, bin_edges = np.histogram(image,bins = 256,range=(0,1))
            ax[1].plot(bin_edges[0:-1],histogram)

            image2 = skimage.io.imread(fname = '/home/pi/SD/nir.jpg',as_gray = True)
            ax[2].imshow(image, cmap='gray')

            histogram, bin_edges = np.histogram(image2,bins = 256,range=(0,1))
            ax[3].plot(bin_edges[0:-1],histogram)


            plt.show()
            """
        elif state == STATE_TEST:
            state = STATE_0
            sleep(1)
            GPIO.output(19,GPIO.HIGH)
            pwm.start(10)
            pwm.ChangeDutyCycle(ins1)
            ca.capture('redblack.jpg')
            sleep(0.1)
            ca.start_recording('redblack.h264')
            ca.wait_recording(5)
            ca.stop_recording()
            pwm.stop()
            GPIO.output(19,GPIO.LOW)
            print("NIREND")
            GPIO.output(13,GPIO.HIGH)
            pwm2.start(10)
            pwm2.ChangeDutyCycle(ins1)
            ca.capture('nirblack.jpg')
            sleep(0.1)
            ca.start_recording('nirblack.h264')
            ca.wait_recording(5)
            ca.stop_recording()
            pwm2.stop()
            GPIO.output(13,GPIO.LOW)
            
            print("change to white")
            sleep(4)
            
            GPIO.output(19,GPIO.HIGH)
            pwm.start(10)
            pwm.ChangeDutyCycle(ins1)
            ca.capture('redwhite.jpg')
            sleep(0.1)
            ca.start_recording('redwhite.h264')
            ca.wait_recording(5)
            ca.stop_recording()
            pwm.stop()
            GPIO.output(19,GPIO.LOW)
            print("NIRend")
            GPIO.output(13,GPIO.HIGH)
            pwm2.start(10)
            pwm2.ChangeDutyCycle(ins1)
            ca.capture('nirwhite.jpg')
            sleep(0.1)
            ca.start_recording('nirwhite.h264')
            ca.wait_recording(5)
            ca.stop_recording()
            pwm2.stop()
            GPIO.output(13,GPIO.LOW)
            
            print("cahnge to hand")
            sleep(4)
            
            GPIO.output(19,GPIO.HIGH)
            pwm.start(10)
            pwm.ChangeDutyCycle(ins1)
            ca.capture('redhand.jpg')
            sleep(0.1)
            ca.start_recording('redhand.h264')
            ca.wait_recording(5)
            ca.stop_recording()
            pwm.stop()
            GPIO.output(19,GPIO.LOW)

            GPIO.output(13,GPIO.HIGH)
            pwm2.start(10)
            pwm2.ChangeDutyCycle(ins1)
            ca.capture('nirhand.jpg')
            sleep(0.1)
            ca.start_recording('nirhand.h264')
            ca.wait_recording(5)
            ca.stop_recording()
            pwm2.stop()
            GPIO.output(13,GPIO.LOW)
        elif state == STATE_SELECT:
            state = STATE_0
            ca.ISO = exp.get()
            state = STATE_0
            ca.capture('white.jpg')

            GPIO.output(19,GPIO.HIGH)
            pwm.start(10)
            pwm.ChangeDutyCycle(ins1)
            sleep(1)
            ca.capture('red.jpg')
            sleep(2)
            ca.start_recording('red.h264')
            #ca.start_preview()
            ca.wait_recording(3)
            ca.stop_recording()
            #ca.stop_preview()
            pwm.stop()
            GPIO.output(19,GPIO.LOW)
            GPIO.output(13,GPIO.HIGH)
            pwm2.start(10)
            pwm2.ChangeDutyCycle(ins2)
            sleep(1)
            ca.capture('nir.jpg')
            sleep(2)
            ca.start_recording('nir.h264')
            #ca.start_preview()
            ca.wait_recording(3)
            ca.stop_recording()
            #ca.stop_preview()
            pwm2.stop()
            GPIO.output(13,GPIO.LOW)

            
            darknoise() 
    
        
            
        else:
            
                
            #ca.shutter_speed = sp.get()
            #ca.contrast = contrast.get()
            ca.brightness = bright.get()
            #ca.saturation = sat.get()
            ca.ISO = exp.get()
            
            stream = io.BytesIO()
            ca.capture(stream, format = 'jpeg')
            stream.seek(0)
            temp = Image.open(stream)
            temp2 = ImageTk.PhotoImage(temp)
            previewPanel.configure(image = temp2)
            
            if state == STATE_R1:
                ins1 = intensity1.get()
         
                GPIO.output(19,GPIO.HIGH)
                pwm.start(10)
                pwm.ChangeDutyCycle(ins1)
            
            elif state == STATE_N1:
                ins2 = intensity2.get()
                GPIO.output(13,GPIO.HIGH)
                pwm2.start(10)
                pwm2.ChangeDutyCycle(ins2)
                
            elif state == STATE_R1S:
                GPIO.output(19,GPIO.LOW)
                pwm.stop()
                state = STATE_0
                
            elif state == STATE_N1S:
                GPIO.output(13,GPIO.LOW)
                pwm2.stop()
                state = STATE_0
            
            elif state == STATE_ANA:
                state = STATE_0
                ana2()
            elif state == STATE_ANAN:
                state = STATE_0
                ana4()
            

            

pre()
root.mainloop()
    
