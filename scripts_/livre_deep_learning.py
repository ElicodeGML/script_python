import matplotlib.pyplot as plt
import numpy as np
import random

data = np.linspace(1, 10, 900)
data = data.reshape(30, 30)

data_bruit = 3 + 4*data + np.random.randn(30, 30)

print(data, "\n\n",  data_bruit)

plt.scatter(data[0], data_bruit[0])
plt.show()

x = np.arange(0, 5, 0.1)
y = np.sin(x)
point_x = x[16]
point_y = y[16]
plt.scatter(point_x, point_y)
plt.plot(x, y)
plt.plot([point_x, point_x], [-1.25, point_x])
plt.plot([0, point_x], [point_y, point_y])
plt.title(""" le sinus de 1.7 est 1
        l'echel est decale de 0.1""")
plt.ylabel("sinus de x")
plt.xlabel("x")
plt.legend()
 #plt.show()

z = (y-x).round(2)
z1 = (y[1].mean()-x[1].mean()).round()
# print(y[0], "y", y[1], "y2", x[0], "x", x[1], "x2", z1, "z")
print()