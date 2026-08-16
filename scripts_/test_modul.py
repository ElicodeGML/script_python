import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([7, 8, 9])
y = np.zeros((3, 3))
z = np.linspace(1, 10, 9)
a = z.reshape((3, 3))
b = 3 + 4*a + np.random.randn(3, 3)

print(z)
plt.scatter(a, b, c=z)
plt.show()