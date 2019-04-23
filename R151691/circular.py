import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dft(x,N):
	j=cm.sqrt(-1)
	X=np.zeros(N)
	for k in range(N):
		for n in range (N):
			X[k]+=x[n]*np.exp(-2*np.pi*k*j*n/N)
	return X
t=np.linspace(0,1000,1000)
x=np.cos(2*np.pi*(500/6000)*t)
y=np.cos(2*np.pi*(1/6000)*t)
N=len(x)
k=np.linspace(0,N-1,N)
z=x+y
X=dft(x,N)
Y=dft(y,N)
Z=dft(z,N)
plt.subplot(611)
plt.plot(k,x)
plt.subplot(612)
plt.plot(k,X)
plt.subplot(613)
plt.plot(k,y)
plt.subplot(614)
plt.plot(k,Y)
plt.subplot(615)
plt.plot(k,z)
plt.subplot(616)
plt.plot(k,Z)
plt.show()
