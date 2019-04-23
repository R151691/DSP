#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:24:09 2019

@author: apiiit-rkv
"""

from DFT_func import dft
import numpy as np
from matplotlib import pyplot as plt
import cmath as c
j=c.sqrt (-1)
x=input ("Enter x:")
n=len(x)
l=input ("Enter shift value:")
y=input ("Shifted input:")
x1=dft(x)*(np.exp(-2*np.pi*j/n))
x1=np.abs(x1)
y1=dft (y)
y1=np.abs (y1)
plt.subplot (211)
plt.stem (x1)
plt.subplot (212)
plt.stem (y1)
 