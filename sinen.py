import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,100,1)
x1=np.sin(2*np.pi*t)
plt.stem(t,x1)
plt.title("sine graph")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()