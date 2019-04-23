#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:09:44 2019

@author: apiiit-rkv
"""

import numpy as np
from matplotlib import pyplot as plt
import cmath as c
j=c.sqrt (-1)
t=np.linspace (0,2,50)
x=np.sin (2*np.pi*t)
#x=[1,2,3,4,5]
def dft (x):
    l= len (x)
    b=[]
    p=[]
    q=[]
    for k in range (0,l,1):
        s=0
        for i in range (0,l,1):
            s=s+((x[i]*(np.exp (-j*2*np.pi*k*i/l))))
        b.append (s)
        p.append (abs(s))
        q.append (np.angle(s))
dft(x)
plt.subplot (411)
plt.stem (t,x)
plt.subplot (412)
plt.stem (b)
plt.subplot (413)
plt.stem (p)
plt.subplot (414)
plt.stem (q)