import numpy as np
import matplotlib.pyplot as plt
rxx=[]
x=np.array(input('enter seq 1='))
l1=len(x)
for l in range(-(l1-1),l1,1):
s=0
for n in range(0,l1,1):
if(n+l>=0 and n+l<l1):
s=s+x[n+l]*x[n]
rxx=np.append(rxx,s)
print rxx
n=np.linspace(-(l1-1),l1-1,2*l1-1)
plt.figure(1)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("cross correlation")
plt.stem(n,rxx)