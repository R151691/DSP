#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:38:27 2019

@author: rgukt
"""

import numpy as np
from matplotlib import pyplot as plt
import scipy
t=linspace (0,100,100)
x=np.sin (1000*np.pi*t)
h=np.sin (3000*np.pi*t)
def con (x,h):
    c=100
    d=199
    b=[]
    y=0
    for i in range (0,d,1):
        y=0
        for j in range (0,c,1):
            if (i-j<0):
                h[i-j]=0
            y=y+(x[j]*h[i-j])
        b.append(y)
    plt.subplot (311)
    plt.stem (t,x)
    plt.subplot (312)
    plt.stem (t,h)
    plt.subplot (313)
    plt.stem (t,b)
def time_rev (x):
    c=len(x)
    y=np.zeros (c)
    for i in range (0,c,1):
        y[c-i-1]=x[i]
    print y
time_rev (x)
con (x,time_rev(x))