from scipy import signal
import matplotlib.pyplot as plt

# h(n) = a^n u(n)and x(n) = u(n)
# Applying ZT
# H(z) = z/(z-a) and X(z) = z/(z-1)
# Y(z) = H(z)*x(z)
# Y(z) = z^2/(z-a)(z-1) = z^2/(z^2-1.5z+0.5)

system = ([1, 0, 0], [1, -1.5, 0.5])

t, y = signal.impulse(system)
plt.stem(t, y)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Impuse Response of z^2/(z-a)(z-1)')
plt.grid()
plt.show()