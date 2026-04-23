import cv2 as cv


#Task Five Generate Gaussian Noise:

samples = np.random.normal(loc=0.0, scale=1.0, size=10000)
#samples_hist = cv.calcHist(samples,[0],None,[50],[256],None)
plt.figure(figsize=(10, 6))
samples_hist = plt.hist(samples, bins=50, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.title('Samples Histogram')
plt.xlabel('Bins')
plt.ylabel('Pixels')
plt.plot(samples_hist)
plt.xlim([0,256])
plt.show()
