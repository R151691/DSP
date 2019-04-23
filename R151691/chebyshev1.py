import numpy as np
import matplotlib.pyplot as plt
import cmath as c
wp=np.float(input("give pass band frequency:"))
ws=np.float(input("give stop band frequency:"))
dp=np.float(input("give pass band gain :"))
ds=np.float(input("give stop band gain :"))
a=((1/dp**2)-1)
b=((1/ds**2)-1)
e=np.sqrt(a)
w=ws/wp
n=np.ceil((np.arccosh(np.sqrt(b/a)))/np.arccosh(w))
print n
print e
w=np.arange (0,10000,1)
if (np.mod(w/wp)<1):
	cn=np.cos (n*np.arccos(w/wp))
if (np.mod(w/wp)>1):
	cn=np.cos (n*np.arccosh(w/wp))
plt.plot (w,cn)
plt.show()
