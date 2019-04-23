#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:04:01 2019

@author: rgukt
"""

import numpy as np
import scipy
from matplotlib import pyplot as plt
t=np.linspace (0,100,100)
x=np.sin (2*3.14*t)
plt.subplot (311)
plt.title ("Input")
plt.plot (t,x)
plt.subplot (312)
plt.stem (t,x)
y=0
b=[]
for i in range (0,100,1):
    y=y+x[i]
    b.append(y)
plt.subplot (313)
plt.title ("Output")
plt.stem (t,b)

