#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 23:33:24 2019

@author: rgukt
"""

import numpy as np
import scipy.io.wavfile as wav 
from matplotlib import pyplot as plt
t=np.linspace(0,100,100)
r,data = wav.read ('/home/apiiit-rkv/Desktop/R151440/Engineering/E2/E2 SEM-2/DSP/Lab/Lab-3/myvoice.wav')
r=np.float (r)
q = np.random.rand (data.shape[0])
x=q+data
wav.write ('noisyvoice.wav',r,x)
p=input ("Enter order of the system:")
y=np.zeros(48000)
for i in range (0,48000,1):
    sum=0
    for k in range (0,p-1,1):
        if ((i-k)<0):
            x[i-k]=0
        sum=sum+(x[i-k])
    y[i]=float(sum)/p
wav.write ('voi.wav',r,y)
