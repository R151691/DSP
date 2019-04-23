import numpy as np
import matplotlib.pyplot as plt
x=input("Enter first signal : ")
p=input("Enter second signal : ")
n=len(x)
m=len(p)
h=p[::1]
y=np.zeros(m+n-1)
for i in range(n):
	for j in range(m):
		y[i+j]=y[i+j]+x[i]*h[j]
for i in range(m-1):
	x.append(0)
for j in range(n-1):
	p.append(0)
t=np.linspace(0,m+n-2,m+n-1)
plt.subplot(311)
plt.stem(t,x)
plt.subplot(312)
plt.stem(t,p)
plt.subplot(313)
plt.stem(t-n+1,y)
plt.show()
