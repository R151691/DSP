#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:58:22 2019

@author: apiiit-rkv
"""

from DFT_func import dft
import numpy as np
import cmath as c
from matplotlib import pyplot as plt
t=np.linspace (0,2,50)
x=np.sin (2*np.pi*t)
y=np.sin (2*2*np.pi*t)
xy=np.add (x,y)
x1=dft (x)
y1=dft (y)
r=np.add (x1,y1)
r=np.abs(r)
re=dft (xy)
re=np.abs(re)
plt.subplot (211)
plt.stem (r)
plt.subplot (212)
plt.stem (re)
plt.show()
