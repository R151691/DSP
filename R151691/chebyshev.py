import numpy as np
from matplotlib import pyplot as plt
dp=np.float (input ("Enter dp:"))
ds=np.float (input ("ENter ds:"))
wp=np.float (input ("ENter wp:"))
ws=np.float (input ("ENter ws:")) 
e=np.sqrt ((1/dp**2)-1)
y=(1/e)*np.sqrt ((1/ds**2)-1)
x=(ws/wp)
c=np.zeros (200)
c[0]=1.0
c[1]=x
N=100
for i in range (2,N,1):
	c[i]=2*c[1]*c[i-1]-c[i-2]
	if (c[i]>=y):
		break
print "The order of the system is",i
w=np.arange (0,10000,1)
x1=w/wp
for j in range (1,10000,1):
	if (w[j]<wp):
		cn=np.cos (i*np.arccos(x1))
	elif (w[j]>wp):
		cn=np.cos (i*np.arccosh(x1))
H=np.sqrt (1/(1+(e**2)*(cn**2)))
H=np.abs (H)
plt.plot (w,H)
plt.show()
