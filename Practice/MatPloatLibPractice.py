import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * np.pi, 0.1)
print(x)
y = np.sin(x)
plt.plot(x, y)
plt.show()

y = np.cos(x)
plt.plot(x, y)
plt.show()

x = np.arange(0, 50, 1)
y = x ** 2
plt.scatter(x, y, color='r')
plt.show()

x = np.arange(0, 50, 1)
y = x ** 3
plt.bar(x, y, color='g')
plt.show()
