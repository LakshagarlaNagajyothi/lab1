import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,10,0.1)
x1=np.cos(2*np.pi*t)
plt.plot(t,x1)
plt.title("cosine graph")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()