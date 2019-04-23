#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:14:49 2019

@author: rgukt
"""
import numpy as np
import matplotlib.pyplot as plt

p=float(input('Delta p'))
s=float(input('Delta s'))
wp=float(input('w p'))
ws=float(input('w s'))
x=np.log(((1/(np.square(p)))-1)/((1/(np.square(s)))-1))
y=np.log(wp/ws)
n=0.5*(x/y)
N=np.ceil(n)
print N
wc = (wp/((1/(np.square(p))-1)**(1/(2*N))))
print (np.ceil(wc))
w=np.linspace(0,31400,200)
h=(1/(1+((w/wc)**(2*N))**(0.5)))
plt.plot(w,h)
plt.show()