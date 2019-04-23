#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 23:21:09 2019

@author: rgukt
"""

import numpy as np
import scipy
from matplotlib import pyplot as plt
t=np.linspace(0,100,100)
r=np.sin (2*3.14*t)
q=np.random.rand(r.shape[0])
x=r+q
plt.subplot (511)
plt.plot (t,r)
plt.subplot (512)
plt.plot (t,q)
plt.subplot (513)
plt.plot (t,x)
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
plt.subplot (514)
plt.plot (t,b)