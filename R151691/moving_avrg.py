#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:42:22 2019

@author: rgukt
"""

import numpy as np
from matplotlib import pyplot as plt
import scipy
x=input ("Enter input x:")
n=input ("No. of samples in x:")
p=input ("Enter order of the system:")
b=[]
y=0
for i in range (0,n+1,1):
    y=0
    for k in range (0,p,1):
        if ((i-k)<0):
            x[i-k]=0
        y=y+(x[i-k])
    y=float(y)/p
    b.append(y)
plt.subplot (211)
plt.title ("Input")
plt.stem (x)
plt.subplot (212)
plt.title ("Output")
plt.stem (b)