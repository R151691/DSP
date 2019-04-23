#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 23:51:19 2019

@author: rgukt
"""

import numpy as np
import scipy
from matplotlib import pyplot as plt
t=np.linspace(0,100,100)
x=np.sin (2*3.14*t)
plt.subplot (311)
plt.plot (t,x)
plt.subplot (312)
plt.stem (t,x)
p=input ("Enter order of the system:")
b=[]
for i in range (0,100,1):
    y=0
    for k in range (0,p-1,1):
        if ((i-k)<0):
            x[i-k]=0
        y=y+(x[i-k])
    y=float(y)/p
    b.append(y)
plt.subplot (313)
plt.stem (t,b)