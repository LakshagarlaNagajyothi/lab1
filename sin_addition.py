import matplotlib.pyplot as plt
import numpy as np
fs=1000
f1=f2=200
n=100
x=np.arange(n)
a=np.sin(2*np.pi*f1/fs*x)
c=10*a
plt.subplot(311)

plt.plot(x,c)
b=np.sin(2*np.pi*f2/fs*x)
d=5*b
plt.subplot(312)
plt.plot(x,d)
e=c+d
plt.subplot(313)
plt.plot(x,e)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
plt.show( )
