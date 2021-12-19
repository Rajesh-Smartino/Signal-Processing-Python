from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


# y(n) = 0.8y(n-1)+x(n)
# H(z) = z/(z-0.8)
# For frequency response z = e^jw


w, h = signal.freqz([1, 0], [1, -0.8])

fig, ax1 = plt.subplots()
ax1.set_title('Frequency Magnitude response')

ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')

plt.grid()
plt.show()



fig, ax1 = plt.subplots()
ax1.set_title('Magitude & Phase response')

ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.grid()
ax2.axis('tight')
plt.show()


'''
HIGH FREQUENCY SINUSOIDAL RESPONSE
'''
# for high frequency sinusoid x(n) = sin(pi)wn
# w = large say pi/2
# Y(z) = z^2/(z^3-0.8z^2+z-0.8) and z = e^jw


w, h = signal.freqz([0, 1, 0, 0], [1, -0.8, 1, -0.8])


fig, ax1 = plt.subplots()
ax1.set_title('High frequency sinusoid')


ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')

plt.grid()
plt.show()

'''
LOW FREQUENCY SINUSOIDAL RESPONSE
'''
from scipy import signal
import matplotlib.pyplot as plt


# for low frequency sinusoid x(n) = sin(pi)wn
# w = pi leads 0 always, choosing least value for w so sinw exists. say w=0.001
# Y(z) = z^2/(z^3-2.8z^2+2.6z-0.8) and z = e^jw


w, h = signal.freqz([0, 0.001, 0, 0], [1, -2.8, 2.6, -0.8])


fig, ax1 = plt.subplots()
ax1.set_title('Low frequency sinusoid')


ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')

plt.grid()
plt.show()