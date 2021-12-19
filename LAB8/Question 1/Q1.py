from scipy import signal
import numpy as np 
import matplotlib.pyplot as plt


# Unit Impulse signal
y = signal.unit_impulse(110, 'mid')
plt.stem(np.arange(-10, 100), y)
plt.xlabel('Time [n]')
plt.ylabel('Amplitude')
plt.title('Unit Impulse Signal')
plt.grid()
plt.show()


# Unit Step signal
n = range(-10, 100, 1)
y = []
for i in range(len(n)):
    temp = (1 if n[i]>=0 else 0)
    y.append(temp)

plt.stem(n, y)
plt.grid()
plt.xlabel('  n--->  ')
plt.ylabel('Amplitude ----> ')
plt.title('Unit step Signal')
plt.show()

# Unit Ramp signal
n = range(-10, 100, 1)
y = []
for i in range(len(n)):
    temp = (n[i] if n[i]>=0 else 0)
    y.append(temp)
    
plt.stem(n, y)
plt.xlabel('  n--->  ')
plt.ylabel('Amplitude ----> ')
plt.title('Unit ramp Signal')
plt.grid(True)
plt.show()