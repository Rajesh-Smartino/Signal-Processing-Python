import matplotlib.pyplot as plt
import numpy as np


fs = 20
ts = 1/fs
k = np.arange(0, 20*4*np.pi, 10)
n = ts*k
a = np.sin(n)
plt.stem(n, a)
plt.title('Sinusoidal signal sampled at 20hz: 2 cycles')
plt.xlabel('radians')
plt.ylabel('Amplitute')
plt.show()


k = np.arange(0, 10*4*np.pi, 10)
n = ts*k
a = np.sin(n)
plt.stem(n, a)
plt.title('Sinusoidal signal sampled at 20hz: 1 cycle')
plt.xlabel('radians')
plt.ylabel('Amplitute')
plt.show()

k = np.arange(0, 5*4*np.pi, 10)
n = ts*k
a = np.sin(n)
plt.stem(n, a)
plt.title('Sinusoidal signal sampled at 20hz: 1/2 cycle')
plt.xlabel('radians')
plt.ylabel('Amplitute')
plt.show()