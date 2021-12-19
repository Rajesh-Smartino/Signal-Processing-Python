import matplotlib.pyplot as plt
import numpy as np


x1 = np.arange(0, 4*np.pi, 0.5)
y1 = np.sin(x1)
plt.subplot(3, 1, 1)
plt.stem(x1, y1)
plt.title('Sampled sinusoidal signal')
plt.xlabel('radians')
plt.ylabel('Amplitute')


x2 = np.arange(start=0, stop=int(4*np.pi), step=0.5)
y2 = []
for i in x2:
    if i >= 4.5 and i<=8.5:
        y2.append(1)
    else:
        y2.append(0)

plt.subplot(3, 1, 2)
plt.stem(x2, y2)
plt.title('Rectangular window')
plt.xlabel('radians')
plt.ylabel('Amplitute')


x = x2
y = []
for i in range(len(x)):
    if x[i] >= 4.5 and x[i]<=8.5:
        y.append(y1[i])
    else:
        y.append(0)
 
plt.subplot(3, 1, 3)
plt.stem(x,y)
plt.title('Windowed sinusoidal signal')
plt.xlabel('radians')
plt.ylabel('Amplitute')
plt.tight_layout()
plt.show()
