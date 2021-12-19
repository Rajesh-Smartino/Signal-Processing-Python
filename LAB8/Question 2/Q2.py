import numpy as np
import matplotlib.pyplot as plt


# Considered y1 = n[u(n)-u(n-10)]
# y2 = 10 e^(-0.3(n-10))(u(n-10)-u(n-20)

x1 = np.arange(0, 10)
y1 = [i for i in x1]

x2 = np.arange(10, 20)
y2 = [10*np.exp(-0.3*(i-10)) for i in x2]

x = np.append(x1, x2)
y = y1+y2
plt.stem(x, y)
plt.xlabel('time n')
plt.ylabel('Amplitude')
plt.title('n[u(n)-u(n-10)]+10e^(-0.3(n-10))(u(n-10)-u(n-20)')
plt.show()