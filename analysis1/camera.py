# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Load data
camera_1d = np.loadtxt('camera.txt')

# Number of pixels
P = camera_1d.size

# Find dimensions (is it a square?)
# Make sure N is an integer
N = int(np.sqrt(P))

# Reshape long 1D array to 2D
camera_2d = camera_1d.reshape(N,N)

# Transpose the image
camera_2dT = camera_2d.T

# Show in grayscale
plt.show(camera_2dT, cmap = 'gray')

# Show the image
plt.show()
