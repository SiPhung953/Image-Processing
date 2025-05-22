import numpy as np
import matplotlib.pyplot as plt

M = np.array([[123, 127, 128, 119, 115, 130],
              [140, 145, 148, 153, 167, 172],
              [133, 154, 183, 192, 194, 191],
              [194, 199, 207, 210, 198, 195],
              [164, 170, 175, 162, 173, 151]])

histogram = np.array([])

for i in range(115, 210):
    histogram = np.append(histogram, np.sum(M == i))

print(histogram)
print(np.cumsum(histogram))
print(np.sum(histogram))
histogram_eq = np.cumsum(histogram) / np.sum(histogram)

plt.bar(np.arange(115, 210), histogram_eq)
plt.show()