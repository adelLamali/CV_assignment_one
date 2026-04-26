import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Task Five Generate Gaussian Noise:

# loc = mean, scale = standard deviation, size = number of samples
noise = np.random.normal(loc=0.0, scale=1.0, size=10000)

# 2. Display the histogram
plt.figure(figsize=(10, 6))
plt.hist(noise, bins=50, density=True, alpha=0.7, color='blue', edgecolor='black')

# Add labels and title
plt.title('Histogram of Gaussian Noise ($\mu=0, \sigma=1$)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(axis='y', alpha=0.5)

# Show plot
plt.show()
