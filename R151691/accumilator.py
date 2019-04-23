#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:03:08 2019

@author: rgukt
"""

import numpy as np
import scipy
from matplotlib import pyplot as plt
x=input ("Enter x:")
plt.subplot (211)
plt.title ("Input")
plt.stem (x)
print ("output y[k]")
k=input ("Enter k:")
y=0
b=[]
for i in range (0,k+1,1):
    y=y+x[i]
    b.append(y)
plt.subplot (212)
plt.title ("Output")
plt.stem (b)