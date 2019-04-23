#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:09:44 2019

@author: apiiit-rkv
"""

import numpy as np
from matplotlib import pyplot as plt
import cmath as c
def dft (x):
    j=c.sqrt (-1)
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
    return b

