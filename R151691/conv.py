#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:02:40 2019

@author: rgukt
"""

import numpy as np
from matplotlib import pyplot as plt
import scipy
x=input ("Enter x:")
h=input ("Enter h:")
def con (x,h):
    c=len(x)
    d=len(x)+len(h)-1
    b=[]
    y=0
    s=np.zeros (d-c)
    x.extend(s)
    h.extend(s)
    for i in range (0,d,1):
        y=0
        for j in range (0,c,1):
            if (i-j<0):
                h[i-j]=0
            y=y+(x[j]*h[i-j])
        b.append(y)
    plt.subplot (311)
    plt.stem (x)
    plt.subplot (312)
    plt.stem (h)
    plt.subplot (313)
    plt.stem (b)
con (x,h)
    
    