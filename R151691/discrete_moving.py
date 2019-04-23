import numpy as np
import matplotlib.pyplot as plt
x=input("Enter a signal : ")
p=input("Enter order of MAS : ")
m=len(x)

y=np.zeros(3*p+m)
for i in range(3*p+m):
	if(i<p):
		continue
	for j in range(p+1):
		y[i]=y[i]+x[i-j]
	y[i]=(y[i]*1.0/p)
plt.subplot(211)
plt.plot(n,x)
plt.subplot(212)
plt.stem(n,y)
