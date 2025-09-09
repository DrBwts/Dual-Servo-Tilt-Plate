# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:04:21 2018

@author: Nic Bwts
"""

from tkinter import *
import serial
import struct

usbport    = 'COM3'
ser        = serial.Serial(usbport, 9600, timeout=1)
slider_min = 0
slider_max = 180
midway     = int(slider_max / 2)

def init():
    print("Started")

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        self.scale1 = Scale(master, from_=slider_min, to=slider_max, command=lambda ev: self.getAngle(0), bd=5, bigincrement=2, length=360, width=30, label='Servo 0')
        self.scale1.set(111)
        self.scale1.pack(side=LEFT)
        self.scale2 = Scale(master, from_=slider_min, to=slider_max, command=lambda ev: self.getAngle(1), bd=5, bigincrement=2, length=360, width=30, label='Servo 1')
        self.scale2.set(111)
        self.scale2.pack(side=LEFT)

        self.centre = Button(frame, text="Centre All", command=self.centre)
        self.centre.pack(side=TOP)
        self.zero = Button(frame, text="Zero All", command=self.zero)
        self.zero.pack(side=LEFT)
        self.maximum = Button(frame, text="Max All", command=self.maximum)
        self.maximum.pack(side=RIGHT)
        
        # for i in range(1, 4):
            
            # ser.write(struct.pack('>B', 255))
            # ser.write(struct.pack('>B', i))
            # ser.write(struct.pack('>B', midway))
            
    def getAngle(self, slider):
        
        if slider == 0:
            ang = self.scale1.get()
            
        if slider == 1:
            ang = self.scale2.get()  
            
#        if slider==3:
#            brt = self.scale3.get()
            
        ser.write(struct.pack('>B', 255))
        ser.write(struct.pack('>B', slider))
        ser.write(struct.pack('>B', ang))
        
#        print('slider', slider, bytes(slider), '\n')
#        print('brt', brt, bytes(brt), '\n')

    def centre(self):
        
        for servo in range(0, 2):
            
            ser.write(struct.pack('>B', 255))
            ser.write(struct.pack('>B', servo))
            ser.write(struct.pack('>B', midway))

            
        self.scale1.set(midway)
        self.scale2.set(midway)

    def zero(self):
        
        for servo in range(0, 1):
            
            ser.write(struct.pack('>B', 255))
            ser.write(struct.pack('>B', servo))
            ser.write(struct.pack('>B', 0))
            
        self.scale1.set(0)
        self.scale2.set(0)
        
    def maximum(self):
        
        for servo in range(0, 2):
            
            ser.write(struct.pack('>B', 255))
            ser.write(struct.pack('>B', servo))
            ser.write(struct.pack('>B', slider_max))
            
        self.scale1.set(slider_max)
        self.scale2.set(slider_max)


init()
root = Tk()
app = App(root)
root.mainloop()