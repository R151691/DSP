#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:45:50 2019

@author: rgukt
"""
import numpy as np
import scipy
from matplotlib import pyplot as plt
x=input ("Enter x:")
def time_rev (x):
    c=len(x)
    y=np.zeros (c)
    for i in range (0,c,1):
        y[c-i-1]=x[i]
    print y
time_rev (x)
    
    
