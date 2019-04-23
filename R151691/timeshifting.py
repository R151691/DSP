import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
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
			s+=(x[t]*np.exp(-2*np.pi*m*j*(t-3)/N))
		X_W.append(s)
	return X_W
x=input("Enter first  signal : ")
y=input("Enter Second signal : ")
N=input("Enter N :")
x=zeropad(x,N)
y=zeropad(y,N)
k=np.linspace(0,N-1,N)
plt.subplot(221)
plt.stem(x[0:N])
plt.subplot(222)
plt.stem(k,dft(x,N))
plt.subplot(223)
plt.stem(k,np.abs(dft(x,N)))
plt.subplot(224)
plt.stem(k,np.angle(dft(x,N)))
plt.show()
