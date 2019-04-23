import matplotlib.pyplot as plt
import numpy as np
fs=50
f=7
sample=100
a=np.arange(sample)
b=np.sin(2*np.pi*f*a/fs)
plt.subplot(411)
plt.plot(a,b)
fs1=75
f1=8
k=np.arange(sample)
l=np.sin(2*np.pi*f*a/fs1+180)
plt.subplot(412)
plt.plot(k,l)

c=b+l
plt.subplot(413)
plt.plot(k,c)
plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()

