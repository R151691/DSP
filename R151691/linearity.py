import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def add(x,y):
	N=len(x)
	z=np.zeros(N)
	for i in range(N):
		z[i]=x[i]+y[i]
	return z
def mul(x,y):
	N=len(x)
	z=np.zeros(N)
	for i in range(N):
		z[i]=x[i]*y[i]
	return z
def circonv(x,h):
	N=len(x)
	z=np.zeros(N)
	for i in range(N):
		for j in range(N):
			z[(i+j)%N]+=x[i]*h[j]
	return z
def zeropad(x,N):
	l=len(x)
	if(l<N):
		for i in range(N-l):
			x.append(0)
	return x
def dft(x,N):
	l=len(x)
	j=cm.sqrt(-1)
	X_W=[]
	for m in range(N):
		s=0
		for t in range (N):
			s+=(x[t]*np.exp(-2*np.pi*m*j*(t)/N))
		X_W.append(s)
	return X_W
x=input("Enter first  signal : ")
y=input("Enter Second signal : ")
N=input("Enter N :")
x=zeropad(x,N)
y=zeropad(y,N)
#z=add(x,y)
#z=mul(x,y)
z=circonv(x,y)
k=np.linspace(0,N-1,N)
'''plt.subplot(331)
plt.stem(k,x)
plt.subplot(334)
plt.stem(k,dft(x,N))
plt.subplot(332)
plt.stem(k,y)
plt.subplot(335)
plt.stem(k,dft(y,N))
plt.subplot(333)'''
plt.stem(k,z)
#plt.subplot(336)
'''plt.stem(k,dft(z,N))
plt.subplot(337)
plt.stem(k,np.angle(dft(x,N)))
plt.subplot(338)
plt.stem(k,np.angle(dft(y,N)))
plt.subplot(339)
plt.stem(k,np.angle(dft(z,N)))'''
plt.show()
