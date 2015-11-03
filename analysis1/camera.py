import numpy as np
import matplotlib.pyplot as plt

# load in data
camera_1d = np.loadtxt('camera.txt')

# reshape long 1D array
newcam = camera_1d.reshape(512,512)

# look at the image
plt.imshow(newcam.T)

# show in grayscale
plt.imshow(newcam.T, cmap = 'gray')

plt.show()
